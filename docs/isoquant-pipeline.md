# Starting the Pipeline

To start the BaseCode IsoQuant Pipeline, a configuration file must be specified (see
[Input](isoquant-input.md)). In addition, three directories on the host machine must be
mounted into the Docker container. The required mount points are:

- Path to the **results folder** of the BaseCode Processing Pipeline. This is both the input
  and the output: the stitched molecule BAM is read from it, and an `isoquant/` subfolder is
  created inside it.
- Path to the **configuration folder** containing the configuration file, which is `config_isoquant/`
  on the host, mounted as the container's `config/`.
- Path to the **BaseCode resources directory**, containing the genome reference and
  annotations (the folder `genome_references/` must be present).

No FASTQ mount is needed: the pipeline works entirely from the BAM produced by the
[BaseCode Processing Pipeline](overview.md).

The pipeline is then started using `docker run`. After it has finished, the ownership of the
results folder should be changed to the current user using `chown`.

The [configuration builder](config-builder.md) writes this command for you, with the mount
paths filled in.

Example commands to start the BaseCode IsoQuant Pipeline, run from the `BaseCode/` folder:

```bash
docker run --rm --name TEST_RUN \
    --mount type=bind,src=$(pwd)/results/,dst=/usr/local/BaseCodeIsoQuant/results/ \
    --mount type=bind,src=$(pwd)/config_isoquant/,dst=/usr/local/BaseCodeIsoQuant/config/ \
    --mount type=bind,src=/path/to/BaseCode_resources/,dst=/usr/local/app/resources/ \
    basicgenomics/basecode_isoquant:1.4.1 --verbose
sudo chown -R user:group results/
```

>**IMPORTANT** The Docker daemon runs as root by default and files created by the Docker
container are owned by root. Therefore, the user which runs the BaseCode IsoQuant Pipeline
needs root access (either using `sudo` or by knowing the password to the root user) to change
file permissions of the final output.

:::{note}
The `results/` folder must already contain `{name}.stitched.molecules.sorted.bam` from a
completed BaseCode Processing Pipeline run, and `name` in `config_isoquant/config.yaml` must
match the `name` that produced it. See
[Use the same `name` for both pipelines](isoquant-input.md).
:::

The directory structure in the Docker image:

```
├─ /usr/
│  ├─ local/
│     ├─ BaseCodeIsoQuant/
│        ├─ config/          ⟵ config_isoquant/ is bound here
│        ├─ results/         ⟵ results/ is bound here
│        ├─ IsoQuant/
│        ├─ workflow/
│           ├─ envs/
│           ├─ rules/
│           ├─ scripts/
│     ├─ app/
└─       ├─ resources/       ⟵ BaseCode_resources is bound here
```
