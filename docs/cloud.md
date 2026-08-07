# Running in the cloud

Both pipelines are distributed as ordinary Docker images, so they run on any machine that
meets the requirements below. That includes a cloud instance on AWS, Azure or Google Cloud.
Nothing about the pipelines is cloud-specific and no cloud-specific build is needed.

:::{note} Guidance, not a managed service
This page describes how to run the container images on infrastructure you control. Basic
Genomics does not operate, provision or support cloud infrastructure on your behalf.
:::

## What the machine needs

The requirements are the same as for a local workstation, see
[Preparation](preparation.md). In a cloud setting three of them deserve particular attention.

| | Notes |
| --- | --- |
| CPU and memory | Providers quote vCPUs, which on x86 instances are threads rather than physical cores, so an instance needs roughly twice the vCPU count of the core count given in Preparation. Memory maps across directly. |
| Disk | Size generously, and attach a separate data volume rather than relying on the boot disk. A run holds the input FASTQ, intermediate files and the output at the same time, and outputs alone reach tens of gigabytes for a deeply sequenced run. Running out of space part way through is the most common way a cloud run fails, and it costs the whole run. |
| Runtime | Expect a run to occupy the instance for a substantial part of a day, longer for many samples. See [Overview](overview.md) for the per-step times. |

The genome reference and annotation bundle also has to be present on the machine, since it is
mounted into the container. See [Input](input.md).

## Choosing a service

Any service that gives you a Linux VM with Docker will do.

:::{div}
:class: providers

[Amazon Web Services](https://aws.amazon.com/ec2/)
[Microsoft Azure](https://azure.microsoft.com/en-us/products/virtual-machines)
[Google Cloud](https://cloud.google.com/compute)

:::

The equivalent services on each are:

| | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Compute | [EC2](https://aws.amazon.com/ec2/) | [Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines) | [Compute Engine](https://cloud.google.com/compute) |
| Block storage | [EBS](https://aws.amazon.com/ebs/) | [Managed Disks](https://azure.microsoft.com/en-us/products/storage/disks) | [Persistent Disk](https://cloud.google.com/persistent-disk) |
| Object storage | [S3](https://aws.amazon.com/s3/) | [Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs) | [Cloud Storage](https://cloud.google.com/storage) |

On AWS we have run the pipeline on compute-optimised `c6i` instances and on general-purpose
`m7i` instances, at the `8xlarge` and `16xlarge` sizes. Those are sizes we have run rather
than a validated minimum, so size the instance and its volume against your own data. The AMD
equivalents of these families serve just as well.

:::{note} Worth checking the processor architecture
Both images are built for x86-64, so Intel and AMD instances work happily. Just take care
with the Arm-based families, such as AWS Graviton, Azure Cobalt or Google Axion, which the
images are not built for.
:::

Batch services (AWS Batch, Azure Batch, Google Cloud Batch) can also run the images if you
already use them, though a single long-lived instance is usually simpler for a pipeline that
runs for hours rather than minutes.

## Getting data in and out

The usual pattern is to keep FASTQ files and results in object storage and pull them onto the
instance for the duration of the run:

1. Upload the FASTQ files and the reference bundle to your bucket.
2. Launch the instance, attach the data volume and install Docker.
3. Copy the inputs onto the instance using your provider's command line tools.
4. Run the pipeline exactly as documented in
   [Starting the Pipeline](pipeline.md). The
   [configuration builder](config-builder.md) will write the command for you.
5. Copy `results/` back to the bucket, then shut the instance down.

Allow time for the transfers. Moving tens of gigabytes each way is often a noticeable part of
the total, and it is worth putting the bucket in the same region as the instance.

## Handling sensitive data

Sequencing data from human samples is usually treated as sensitive, and often as personal
data. The most important structural point is this:

:::{important} Your data stays in your account
The pipelines are container images that you run on infrastructure you control. Neither
pipeline transmits sequencing data anywhere, and no data reaches Basic Genomics.
:::

Beyond that, the controls are the ones your provider already offers:

- **Encryption at rest.** Object storage is encrypted by default on all three providers, as
  are Azure Managed Disks and Google Persistent Disk. The one to check is EBS on AWS, where
  encryption is selected per volume, though it can be turned on by default for a region.
- **Encryption in transit.** The providers' own command line tools use TLS by default.
- **Key management.** Provider-managed keys are the simplest option. Where your policy
  requires it, all three support customer-managed keys through their key management services.
- **Access control.** Attach an identity scoped to the specific bucket, an instance role on
  AWS, a managed identity on Azure or a service account on Google Cloud, rather than placing
  long-lived credentials on the machine.
- **Region and residency.** Choose the region deliberately if your data is subject to
  residency requirements, and keep the bucket and instance in the same one.
- **Clean up.** Delete the data volume when the run is finished. Both the inputs and the
  outputs contain sequence data, including the BAM files.

Whether a given configuration satisfies your obligations is a decision for your own data
protection or compliance function. Basic Genomics' software is supplied for research use
only, see [Legal notices](legal.md).
