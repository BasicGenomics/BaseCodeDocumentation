# Viewing reads by tag in IGV

How to colour, group and sort molecules by BAM tag in IGV. This works on the stitched BAM from
the BaseCode Processing Pipeline and on the annotated BAM from the
[BaseCode IsoQuant Pipeline](isoquant.md). For what each tag means, see
[BAM file tags](functions.md) and [IsoQuant BAM file tags](isoquant-tags.md).

## Why use tags

A locus in the stitched BAM can hold thousands of molecules from every sample in the run.
IGV can separate them by any tag directly from its menus, so samples, genes or isoform
assignments can be inspected in one view without writing code.

## Prerequisites

- [IGV desktop](https://igv.org/doc/desktop/).
- The BAM and its index (`.bai`) in the same folder.
- In IGV, the genome assembly the pipeline aligned to.

## Colour by tag

Gives each tag value its own colour, for example to tell samples (`SM`) apart at a glance.

```
1. Load your BAM file in IGV
2. Right-click on the read track
3. Select: Color alignments by → Tag
4. Enter the tag name (e.g. SM)
5. IGV will assign a unique color per unique tag value
```

## Group by tag

Stacks molecules into separate labelled rows per tag value, for example one row per sample
(`SM`).

```
1. Right-click on the read track
2. Select: Group alignments by → Tag
3. Enter the tag name (e.g. SM)
4. Reads will be separated into labeled groups
```

## Sort by tag

Orders molecules by tag value at the centre of the view, for example by the number of reads
stitched (`NR`).

```
1. Right-click on the read track
2. Select: Sort alignments by → Tag
3. Enter the tag name (e.g. NR, FC)
4. Reads will be reordered by the tag value at the center of the current view
```

## Useful tags

| Tag | BAM | Use |
| --- | --- | --- |
| `SM` | stitched, annotated | colour or group by sample |
| `XT` | stitched, annotated | group by gene where genes overlap |
| `NR` | stitched, annotated | sort by the number of reads stitched |
| `CP` | annotated | group end-to-end molecules (`1`) apart from the rest |
| `ZA` | annotated | colour by assignment type, such as `unique` or `ambiguous` |
| `ZI` | annotated | group by assigned isoform |
