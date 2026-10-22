# Filtering full-length molecules

How to keep only the full-length molecules, those whose 3′ and 5′ ends were both sequenced,
from the stitched BAM written by the BaseCode Processing Pipeline. For what each tag means,
see [BAM file tags](functions.md).

## Why filter

The stitched BAM contains every reconstructed molecule, including partial ones whose ends were
not sequenced. Filtering keeps a smaller, high-confidence set of full-length molecules for
analyses where the ends matter, such as isoforms, start and end sites, or transcript length.

In the [BaseCode IsoQuant Pipeline](isoquant.md), set `full_length_only: True` instead (see
[Input](isoquant-input.md)).

## What counts as full-length

A molecule is full-length when it has at least one 3′ read (`TC` > 0) and one 5′ read
(`FC` > 0), the same test the run report uses for end-to-end molecules. Both ends were
observed, but the region between them can still contain unsequenced gaps, shown as CIGAR
deletion (`D`) blocks.

## Prerequisites

samtools 1.12 or later, for filter expressions.

```bash
# Install samtools. We recommend using conda for this.
conda install bioconda::samtools
```

## Script

Download [filter_full_length.sh](https://basecode.readthedocs.io/en/latest/downloads/filter_full_length.sh),
or from the command line:

```bash
curl -LO https://basecode.readthedocs.io/en/latest/downloads/filter_full_length.sh
```

::::{dropdown} Show the script
:::{literalinclude} _static/downloads/filter_full_length.sh
:lang: bash
:::
::::

## Running it

```bash
bash filter_full_length.sh results/{name}.stitched.molecules.sorted.bam
```

This writes `{name}.stitched.molecules.sorted.full_length.bam` and its index to the current
folder. A second argument sets a different output path. The output keeps the header, the sort
order and all tags.

### Other selections

Replace the expression in the `samtools view` line:

| Keep | Expression |
| --- | --- |
| Full-length molecules | `[TC]>0 && [FC]>0` |
| Full-length molecules of one sample | `[TC]>0 && [FC]>0 && [SM]=="SAMPLE_ID"` |
