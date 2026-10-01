# Output

A folder named `results/` contains the output from the pipeline. The main result is
`{name}.stitched.molecules.sorted.bam`: the BaseCode Synthetic Long Reads, one record per
reconstructed molecule, and the input to the [BaseCode IsoQuant Pipeline](isoquant.md). Gene
counts per sample are in `QC_files/counts/`, and `{name}_run_report.pdf` summarises the run.
The tree below outlines the files and folders that can be expected after a successful run.

Throughout, `{name}` is the `name` set in the configuration file and `{sample}` is a `SAMPLE_ID`
from the sample sheet.

```
├─ BaseCode/
│  ├─ results/
│     ├─ benchmarks/
│     ├─ checksums/
│     ├─ dones/
│     ├─ intermediate/
│     ├─ logs/
│     ├─ metadata/
│     ├─ QC_files/
│     │  ├─ conversion_rates/
│     │  ├─ counts/
│     │  ├─ fastq/
│     │  ├─ gene_reconstruction_status/
│     │  ├─ {name}_long_form_reconstruction_stats.csv.gz
│     │  └─ {name}_summary_stats.csv
│     ├─ read_flow_files/
│     ├─ summaries/
│     ├─ {name}_run_report.pdf
│     ├─ {name}.stitched.molecules.sorted.bam
└─    └─ {name}.stitched.molecules.sorted.bam.bai
```

| File/Folder | Description |
|----------------------|-------------|
| benchmarks/ | Run time, memory and CPU use of each step. |
| checksums/ | `{name}_checksums.md5`: MD5 checksums of the stitched BAM, its index and the long-form reconstruction stats, for checking copies. |
| dones/ | Markers the pipeline uses to track finished steps. Not needed for analysis. |
| intermediate/ | The aligned reads before and after reconstruction, and per-sample reconstruction and stitching records. Detailed below. |
| logs/ | Logs for each step. `run_manifest.json` records the pipeline version, configuration and tool versions of the run, `run_history.jsonl` has one line per start or restart, and `tool_options/` records the options each tool ran with, see [Tool options](input.md#input-tool-options). |
| metadata/ | Sample information derived from the sample sheet: sample barcodes, sample map and read type map. |
| QC_files/ | Quality control tables, the per-molecule reconstruction stats and the gene counts in `counts/`. Detailed below. |
| read_flow_files/ | Read counts per sample barcode at the stages the pipeline tracks. `comprehensive` mode adds more stages. |
| summaries/ | Summaries written by Cutadapt (trimming), HISAT-3N (mapping) and featureCounts (gene assignment). |
| {name}_run_report.pdf | PDF report of the run: the samples, read counts, detected genes, reconstruction, end-to-end molecules and their lengths, and transcript coverage. |
| {name}.stitched.molecules.sorted.bam | The BaseCode Synthetic Long Reads: one record per molecule, mapped to the reference genome and sorted by position. Its tags are described in [BAM file tags](functions.md). |
| {name}.stitched.molecules.sorted.bam.bai | BAM index file. |

## QC files

```
├─ QC_files/
│  ├─ conversion_rates/
│  ├─ counts/
│  ├─ fastq/
│  ├─ gene_reconstruction_status/
│  ├─ {name}_long_form_reconstruction_stats.csv.gz
└─ └─ {name}_summary_stats.csv
```

| File/Folder | Description |
|------|-------------|
| conversion_rates/ | Mismatch rates for every base substitution, per sample barcode, read type and strand (`{name}_conversion_rates.csv`) and per sample barcode (`{name}_summary_conversion_rates.csv`). |
| counts/ | Gene counts. Detailed below. |
| fastq/ | FastQC and fastp reports for the raw reads. |
| gene_reconstruction_status/ | Per gene and sample, how many reads of each type (3′, internal, 5′) ended up in molecules, and why the others did not. |
| {name}_long_form_reconstruction_stats.csv.gz | One row per record in the stitched BAM: sample, gene, reads per compartment (`TC`, `IC`, `FC`), aligned length (`QL`), number of unsequenced gaps (`GAPS`), end flags (`T1`, `F1`) and `ST`, which says whether the record was built from several fragments (`Molecule`) or is a single read pair (`ReadPair`) or single read (`ReadSingleton`). |
| {name}_summary_stats.csv | One row per sample with the headline metrics of the run report: 3′, internal and 5′ read counts, genes detected, molecules by end coverage, the percentage of end-to-end molecules and their median length, and the conversion rate. |

### Gene counts

The `counts/` folder holds conventional gene-level counts, taken from the aligned reads before
stitching. The unit is the **read pair**, not the molecule: every read pair assigned to a gene
is counted, whether or not it became part of a molecule. Read pairs assigned to more than one
gene are not counted, and a read pair with both exonic and intronic evidence counts as
exonic. For molecule- and isoform-level counts, use the
[BaseCode IsoQuant Pipeline](isoquant.md).

| File | Description |
|------|-------------|
| {name}_exonic_counts_matrix.csv | Genes × samples matrix of exonic read pairs. The first two columns are `gene_id` and `gene_name`, followed by one column per `SAMPLE_ID`. |
| {name}_exonic_counts_per_gene.csv | The exonic counts in long format: one row per sample barcode and gene. |
| {name}_intronic_counts_matrix.csv | Genes × samples matrix of intronic read pairs, laid out like the exonic matrix. |
| {name}_intronic_counts_per_gene.csv | The intronic counts in long format. |
| {name}_total_counts_matrix.csv | Genes × samples matrix of exonic plus intronic read pairs. |

## Intermediate files

Most intermediate files are deleted during the run. These are kept:

```
├─ intermediate/
│  ├─ reconstruct/{name}/
│  │  └─ {sample}.merged_genes.csv
│  ├─ stitch/{name}/
│  │  ├─ {sample}.stitched_deletions.tsv
│  │  └─ {sample}.stitched_error.log
│  ├─ {name}.reads.aligned.trimmed.genetagged.sorted.bam
│  ├─ {name}.reads.aligned.trimmed.genetagged.sorted.bam.bai
│  ├─ {name}.reads.aligned.trimmed.genetagged.sorted.reconstructed.sorted.bam
└─ └─ {name}.reads.aligned.trimmed.genetagged.sorted.reconstructed.sorted.bam.bai
```

| File | Description |
|------|-------------|
| reconstruct/{name}/{sample}.merged_genes.csv | Groups of overlapping genes that share reads and were reconstructed together, with the number of reads they share. |
| stitch/{name}/{sample}.stitched_deletions.tsv | Every deletion in a stitched molecule, and whether the molecule's reads show a real deletion (`is_true_deletion`) or an unsequenced gap. |
| stitch/{name}/{sample}.stitched_error.log | Molecules that could not be stitched and were left out of the stitched BAM, one per line. |
| {name}.reads.aligned.trimmed.genetagged.sorted.bam | The aligned, trimmed reads with their gene assignment, before reconstruction. |
| {name}.reads.aligned.trimmed.genetagged.sorted.bam.bai | BAM index file. |
| {name}.reads.aligned.trimmed.genetagged.sorted.reconstructed.sorted.bam | The same reads after reconstruction, each tagged with the molecule it belongs to. This is the input to stitching. Detailed below. |
| {name}.reads.aligned.trimmed.genetagged.sorted.reconstructed.sorted.bam.bai | BAM index file. |

### Reconstructed reads

Each read in the reconstructed BAM carries these tags, among others:

| Tag | Description |
|-----|-------------|
| `SM` | Sample name |
| `SB` | Sample barcode the read was sequenced with |
| `XX` | Read type: `TP_read` (3′), `internal` or `FP_read` (5′) |
| `GE`, `GI` | Gene the read was assigned to by exon or intron overlap |
| `RM` | Molecule the read belongs to. It matches `RM` in the stitched BAM, so reads can be joined to their molecule. |
| `ST` | Reconstruction status |

Reads with `ST` set to `Molecule`, `ReadPair` or `ReadSingleton` are in the stitched BAM: as part of
a molecule built from several fragments, as a single read pair, or as a single read. Reads with
any other status were not placed in a molecule, for example `InsufficientConversions` (too few
conversions to match) or `CollisionWhileBuilding` (matched more than one molecule).
`QC_files/gene_reconstruction_status/` counts the reads of each status per gene.

## Comprehensive mode

With `mode: comprehensive`, the run also writes:

| File/Folder | Description |
|------|-------------|
| downstream/ | Poly-A sites and transcription start sites (BED and bedGraph), from molecules with an observed 3′ or 5′ end. |
| QC_files/fastq/multiqc/ | A MultiQC report across the FASTQ QC. |
| QC_files/gene_body_coverage/ | Coverage of molecules along gene bodies. |
| QC_files/general_stats/ | Read types and mapping categories. |
| QC_files/insert_overlap_sizes/ | Insert, mate overlap and aligned sizes, and TSO capture. |
| QC_files/mapping_quality/ | Mapping quality, overall and per read type. |
| QC_files/molecule_coverage/ | Coverage per molecule. |
| QC_files/molecule_discordance/ | Per-molecule consistency of the conversion pattern across its reads. |
