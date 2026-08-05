# Output

The BaseCode IsoQuant Pipeline writes everything into an `isoquant/` subfolder of the
`results/` folder produced by the [BaseCode Processing Pipeline](overview.md). The tree below
outlines the relevant files and folders that can be expected after a successful run.

Throughout, `{name}` is the `name` set in the configuration file and `{token}` is the
`read_group` option with `:` replaced by `_`, so `tag_SM` with the default `read_group`
of `tag:SM`.

```
├─ BaseCode/
│  ├─ results/
│     ├─ {name}.stitched.molecules.sorted.bam       ⟵ input, from the BaseCode Processing Pipeline
│     ├─ isoquant/
│        ├─ {name}/
│        ├─ logs/
│        ├─ mudata/
│        │  ├─ {name}_counts.h5mu
│        ├─ {name}.adapted_molecules.tsv
│        ├─ {name}.annotated.sorted.bam
│        ├─ {name}.annotated.sorted.bam.bai
└─       └─ geneannotations_collapsed_{mode}_{representative}.db
```

| File/Folder | Description |
|----------------------|-------------|
| {name}/ | Folder with all IsoQuant results: assignments, transcript models and quantification. Detailed below. |
| logs/ | Folder with logs for each step of the BaseCode IsoQuant Pipeline, including `{name}.versions.log` recording the resolved run configuration and component versions. |
| mudata/{name}_counts.h5mu | All quantification in a single MuData file for analysis in Python. It holds four modalities: `isoform` and `gene` for the discovered features, and `reference_isoform` and `reference_gene` for the reference annotation. Each is a samples × features matrix carrying both a `count` and a `tpm` layer, with the samples taken from the `read_group` tag. |
| {name}.adapted_molecules.tsv | One row per molecule recording what molecule preparation changed: whether it had an unsequenced gap, the total gap length, whether a synthetic poly-A tail was added, whether it is full-length, and a summary in the `AD` column. |
| {name}.annotated.sorted.bam | The molecules carrying their IsoQuant assignment in custom tags. Written only when `annotate_bam` is `True`. See [BAM file tags](isoquant-tags.md). |
| {name}.annotated.sorted.bam.bai | BAM index file. |
| geneannotations_collapsed_{mode}_{representative}.db | The gene database IsoQuant built from the annotation actually used. Named after the collapsed annotation (e.g. `geneannotations_collapsed_cds_canonical.db`), or after the reference annotation when `collapse_annotation` is `False`. |

## IsoQuant results

The `{name}/` folder holds the IsoQuant output itself.

```
├─ isoquant/
│  ├─ {name}/
│     ├─ aux/
│     ├─ {name}.read_assignments.tsv.gz
│     ├─ {name}.corrected_reads.bed.gz
│     ├─ {name}.transcript_models.gtf
│     ├─ {name}.transcript_model_reads.tsv.gz
│     ├─ {name}.extended_annotation.gtf
│     ├─ {name}.novel_vs_known.SQANTI-like.tsv
│     ├─ {name}.transcript_counts.tsv
│     ├─ {name}.transcript_grouped_{token}_counts.tsv
│     ├─ {name}.discovered_transcript_grouped_{token}_counts.linear.tsv
│     ├─ {name}.gene_counts.tsv
│     ├─ {name}.exon_counts.tsv
│     ├─ {name}.intron_counts.tsv
│     ├─ {name}.variant_support.summary.txt
└─    └─ ...
```

### Assignments and models

Three of these feed the annotated BAM: `read_assignments` supplies the reference assignment
tags, `transcript_model_reads` supplies the discovered-model tag, and `corrected_reads`
supplies the imputed structure. See [BAM file tags](isoquant-tags.md).

| File | Description |
|------|-------------|
| {name}.read_assignments.tsv.gz | One row per molecule per compatible isoform, with the assignment type and the events supporting it. Source of the `ZA`, `ZE`, `ZI` and `ZG` tags in the annotated BAM. |
| {name}.corrected_reads.bed.gz | The exon/intron structure IsoQuant resolved for each molecule, including structure imputed across unsequenced gaps. Used to rewrite CIGARs, and the source of `OC` and `IM`, when `include_imputed` is `True`. |
| {name}.transcript_models.gtf | Novel transcript models constructed from the data. |
| {name}.transcript_model_reads.tsv.gz | Which molecules support each novel transcript model. Source of the `ZM` tag in the annotated BAM. |
| {name}.extended_annotation.gtf | The reference annotation extended with the discovered transcript models. |
| {name}.novel_vs_known.SQANTI-like.tsv | Per-transcript classification of discovered models against the reference, in a SQANTI-like format. |
| aux/ | Folder with IsoQuant auxiliary and intermediate files. |

### Quantification

Quantification files follow a consistent naming scheme:

```
{name}[.discovered]_<feature>[_grouped_{token}]_<counts|tpm>[.linear].tsv
```

| Name part | Meaning |
|-----------|---------|
| `discovered` | Present for novel transcript models; absent for reference annotation features. |
| `<feature>` | `transcript`, `gene`, `exon` or `intron`. |
| `grouped_{token}` | Present for per-sample matrices, grouped by the `read_group` tag. Absent for run-wide totals. |
| `counts` / `tpm` | Raw molecule counts, or TPM-normalised values. Exons and introns are counts only. |
| `.linear` | Long-format (one row per feature/group pair) rather than a wide matrix. |

Every feature type produces the same set of files, so a run with the default `read_group`
writes 26 quantification files in total:

| Feature | Files produced |
| --- | --- |
| `transcript` | counts, TPM, grouped counts (wide), grouped counts (long), grouped TPM |
| `discovered_transcript` | the same five |
| `gene` | the same five |
| `discovered_gene` | the same five |
| `exon` | counts, grouped counts (wide), grouped counts (long) |
| `intron` | counts, grouped counts (wide), grouped counts (long) |

Exons and introns are counted only; no TPM is produced for them.

All of these are also available together in `mudata/{name}_counts.h5mu`, as four modalities
(`isoform`, `gene`, `reference_isoform`, `reference_gene`) each carrying a `count` and a
`tpm` layer.

### Variant support

Written when `assess_variant_support` is `True`; which files appear depends on
`variant_support_mode`.

| File | Description |
|------|-------------|
| {name}.discovered_variant_support.per_variant.tsv | Per-variant read support for discovered transcript models. Written for mode `discovered` or `both`. |
| {name}.reference_variant_support.per_variant.tsv | Per-variant read support for reference transcripts. Written for mode `reference` or `both`. |
| {name}.variant_support.summary.txt | Summary across all assessed variants. Always written. |
