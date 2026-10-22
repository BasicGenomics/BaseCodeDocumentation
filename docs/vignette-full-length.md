# Filtering full-length molecules

How to keep only the full-length molecules, those whose 3′ and 5′ ends were both sequenced,
from the stitched BAM written by the BaseCode Processing Pipeline. For what each tag means,
see [BAM file tags](functions.md).

## Why filter

The stitched BAM contains every molecule the pipeline reconstructed, complete or not. A
molecule is built from whichever of its fragments were sequenced, so many cover only part of
their transcript. They are genuine observations and suit most analyses, but where a partial
molecule starts and stops is set by the sequenced fragments, not by the transcript.

Filtering gives a high-confidence set of full-length molecules, whose start and end were
observed rather than inferred. Use it when the ends matter, for example to:

- identify isoforms, including those that differ only in where they start or end
- study transcription start sites and poly-A sites on the same molecule
- link splicing events along a whole transcript
- measure transcript length

The set is smaller than the full BAM, so it trades depth for confidence. Gene expression does
not need it; use the gene counts in `QC_files/counts/` (see [Output](output.md)).

If you run the [BaseCode IsoQuant Pipeline](isoquant.md), do not filter the BAM yourself. Set
`full_length_only: True` (see [Input](isoquant-input.md)), which applies the same test.

## What counts as full-length

Each molecule records how many 3′ reads (`TC`) and 5′ reads (`FC`) it was built from. A 3′ read
is primed by poly-dT at the poly-A tail, and a 5′ read carries the template-switching oligo
added at the 5′ end of the RNA. A molecule with `TC` > 0 and `FC` > 0 has both ends observed
and is full-length. This is the same test the run report uses for end-to-end molecules.

Two limits apply:

- Full-length means both ends were observed, not that every base between them was sequenced.
  Unsequenced inner gaps remain as CIGAR deletion (`D`) blocks. See
  [Why BaseCode data needs its own options](isoquant-input.md#basecode-options).
- The two ends are not equally strong evidence. The 3′ end is anchored at the poly-A tail,
  whereas the 5′ end marks where reverse transcription and template switching stopped.

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
| Molecules with a 3′ end | `[TC]>0` |

## Checking against the run report

The run report gives end-to-end molecules as a percentage of the molecules with a 3′ end, not
of all molecules. The same figure is `Percentage Reconstructed End-to-End Molecules (%)` in
`QC_files/{name}_summary_stats.csv`. To reproduce it per sample from the BAM:

```bash
samtools view -e '[TC]>0' results/{name}.stitched.molecules.sorted.bam | awk '
    BEGIN {print "sample\tfull_length\twith_3prime_end\tpercent"}
    {
        sm=""; fc=0
        for(i=12;i<=NF;i++){
            if($i ~ /^SM:Z:/) sm=substr($i,6)
            if($i ~ /^FC:i:/) fc=substr($i,6)
        }
        n[sm]++
        if(fc>0) fl[sm]++
    }
    END {
        for(s in n) printf "%s\t%d\t%d\t%.2f\n", s, fl[s], n[s], 100*fl[s]/n[s]
    }'
```
