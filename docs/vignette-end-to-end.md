# Filtering end-to-end molecules

How to keep only the end-to-end molecules, those whose 3′ and 5′ ends were both sequenced,
from the stitched BAM written by the BaseCode Processing Pipeline. For what each tag means,
see [BAM file tags](functions.md).

## Why filter

The stitched BAM contains every reconstructed molecule, including partial ones whose ends were
not sequenced. Filtering keeps a smaller, high-confidence set of end-to-end molecules for
analyses where the ends matter, such as isoforms, start and end sites, or transcript length.

In the [BaseCode IsoQuant Pipeline](isoquant.md), set `full_length_only: True` instead (see
[Input](isoquant-input.md)).

## What counts as end-to-end

A molecule is end-to-end when it has at least one 3′ read (`TC` > 0) and one 5′ read
(`FC` > 0), the same test the run report uses. Both ends were observed, but the region between
them can still contain unsequenced gaps, shown as CIGAR deletion (`D`) blocks.

## Prerequisites

samtools 1.12 or later, for filter expressions.

```bash
# Install samtools. We recommend using conda for this.
conda install bioconda::samtools
```

## Script

Download [filter_end_to_end.sh](https://basecode.readthedocs.io/en/latest/downloads/filter_end_to_end.sh),
or from the command line:

```bash
curl -LO https://basecode.readthedocs.io/en/latest/downloads/filter_end_to_end.sh
```

::::{dropdown} Show the script
:::{literalinclude} _static/downloads/filter_end_to_end.sh
:lang: bash
:::
::::

## Running it

```bash
bash filter_end_to_end.sh results/{name}.stitched.molecules.sorted.bam
```

This writes `{name}.stitched.molecules.sorted.end_to_end.bam` and its index to the current
folder. A second argument sets a different output path. The output keeps the header, the sort
order and all tags.

### Other selections

Replace the expression in the `samtools view` line:

| Keep | Expression |
| --- | --- |
| End-to-end molecules | `[TC]>0 && [FC]>0` |
| End-to-end molecules of one sample | `[TC]>0 && [FC]>0 && [SM]=="SAMPLE_ID"` |
