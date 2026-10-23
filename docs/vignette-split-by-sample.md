# Splitting a BAM by sample

How to split the stitched BAM written by the BaseCode Processing Pipeline into one BAM per
sample, using the `SM` tag. For what each tag means, see [BAM file tags](functions.md).

## Why split

A run's stitched BAM holds the molecules of all its samples in one file, with the sample of
each molecule in the `SM` tag. Many tools, and side-by-side tracks in a genome browser, expect
one BAM per sample.

## Prerequisites

samtools.

```bash
# Install samtools. We recommend using conda for this.
conda install bioconda::samtools
```

## Script

Download [split_bam_by_sample.sh](https://basecode.readthedocs.io/en/latest/downloads/split_bam_by_sample.sh),
or from the command line:

```bash
curl -LO https://basecode.readthedocs.io/en/latest/downloads/split_bam_by_sample.sh
```

::::{dropdown} Show the script
:::{literalinclude} _static/downloads/split_bam_by_sample.sh
:lang: bash
:::
::::

## Running it

Run the script from an empty folder, since it indexes every BAM file in the folder it runs in:

```bash
mkdir per_sample && cd per_sample
bash ../split_bam_by_sample.sh ../results/{name}.stitched.molecules.sorted.bam
```

This writes `{sample}.bam` and its index for every sample, named after the `SM` value. To split
only the end-to-end molecules, filter first as in
[Filtering end-to-end molecules](vignette-end-to-end.md) and split the filtered BAM.
