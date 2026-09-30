# Output

A folder named `results/` contains the output from the pipeline. The tree below outlines the
relevant files and folders that can be expected after a successful run.

Throughout, `{name}` is the `name` set in the configuration file.

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
│     ├─ read_flow_files/
│     ├─ summaries/
│     ├─ {name}_run_report.pdf
│     ├─ {name}.stitched.molecules.sorted.bam
└─    └─ {name}.stitched.molecules.sorted.bam.bai
```

| File/Folder | Description |
|----------------------|-------------|
| benchmarks/ | Run time and memory use of each step. |
| checksums/ | `{name}_checksums.md5`: MD5 checksums of the stitched BAM, its index and the long-form reconstruction stats, for checking copies. |
| dones/ | Markers the pipeline uses to track finished steps. Not needed for analysis. |
| intermediate/ | Intermediate files, including the aligned reads with their reconstruction tags, before stitching. |
| logs/ | Logs for each step. `logs/tool_options/` records the options each tool ran with, see [Tool options](input.md#input-tool-options). |
| metadata/ | Sample information derived from the sample sheet: sample barcodes, sample map and read type map. |
| QC_files/ | Quality control tables and gene counts. Detailed below. |
| read_flow_files/ | Read counts at each stage of the pipeline. |
| summaries/ | Summaries written by Cutadapt (trimming), HISAT-3N (mapping) and featureCounts (gene assignment). |
| {name}_run_report.pdf | PDF report summarising the run. |
| {name}.stitched.molecules.sorted.bam | The BaseCode Synthetic Long Reads, one record per molecule. See [BAM file tags](functions.md). |
| {name}.stitched.molecules.sorted.bam.bai | BAM index file. |

## QC files

```
├─ QC_files/
│  ├─ {name}_summary_stats.csv
│  ├─ {name}_long_form_reconstruction_stats.csv.gz
│  ├─ counts/
│  ├─ gene_reconstruction_status/
│  ├─ conversion_rates/
└─ └─ fastq/
```

| File/Folder | Description |
|------|-------------|
| {name}_summary_stats.csv | One row per sample with the headline metrics of the run report: 3′, internal and 5′ read counts, genes detected, molecules by end coverage, the percentage of end-to-end molecules and their median length, and the conversion rate. |
| {name}_long_form_reconstruction_stats.csv.gz | One row per record in the stitched BAM: sample, gene, reads per compartment (`TC`, `IC`, `FC`), aligned length (`QL`), number of unsequenced gaps (`GAPS`), end flags (`T1`, `F1`) and `ST`, which says whether the record was built from several fragments (`Molecule`) or is a single read pair (`ReadPair`) or single read (`ReadSingleton`). |
| counts/ | Gene counts. Detailed below. |
| gene_reconstruction_status/ | Per gene and sample, how many reads of each type (3′, internal, 5′) ended up in molecules, and why the others did not. |
| conversion_rates/ | Mismatch rates for every base substitution, per sample barcode, read type and strand (`{name}_conversion_rates.csv`) and per sample barcode (`{name}_summary_conversion_rates.csv`). |
| fastq/ | FastQC and fastp reports for the raw reads. |

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
| {name}_intronic_counts_matrix.csv | The same for intronic read pairs. |
| {name}_total_counts_matrix.csv | Exonic plus intronic. |
| {name}_exonic_counts_per_gene.csv | The exonic counts in long format: one row per sample barcode and gene. |
| {name}_intronic_counts_per_gene.csv | The intronic counts in long format. |

## Comprehensive mode

With `mode: comprehensive`, the run also writes:

| File/Folder | Description |
|------|-------------|
| QC_files/general_stats/, QC_files/mapping_quality/ | Read types, mapping categories and mapping quality. |
| QC_files/insert_overlap_sizes/ | Insert, mate overlap and aligned sizes, and TSO capture. |
| QC_files/gene_body_coverage/, QC_files/molecule_coverage/ | Coverage of molecules along gene bodies, and per molecule. |
| QC_files/molecule_discordance/ | Per-molecule consistency of the conversion pattern across its reads. |
| QC_files/fastq/multiqc/ | A MultiQC report across the FASTQ QC. |
| downstream/ | Poly-A sites and transcription start sites (BED and bedGraph), from molecules with an observed 3′ or 5′ end. |
