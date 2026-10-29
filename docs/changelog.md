# Changelog

Newest first. Each release says what to do with data processed with an earlier version.

:::{div}
:class: table-centered

| Label | Meaning |
| --- | --- |
| <span class="rerun rerun-none"><span class="rerun-status">No rerun needed</span></span> | Results are unchanged. Use the new version for new runs. |
| <span class="rerun rerun-compare"><span class="rerun-status">Rerun for comparability</span></span> | Results shift slightly. Keep one study on one version. |
| <span class="rerun rerun-recommended"><span class="rerun-status">Rerun recommended</span></span> | Results changed or were incomplete. Rerun affected samples. |

:::

Rerunning the Processing Pipeline also means rerunning IsoQuant. Not the reverse.

(changelog-processing)=
## BaseCode Processing Pipeline

### 1.4.2

<span class="rerun rerun-compare"><span class="rerun-label">Data from earlier versions</span><span class="rerun-status">Rerun for comparability</span></span>

- The stitched BAM's read counts (`NR`, `TC`, `IC`, `FC`, `ER`, `IR`) and end flags (`T1`, `F1`)
  now count only reads that remain in the molecule after cleanup. Some counts drop, so
  end-to-end percentages can shift slightly. Molecule sequences and alignments are unchanged.
- In `comprehensive` mode: per-molecule coverage (`QC_files/molecule_coverage/`) is no longer
  written, and gene body coverage adds a table by molecule class and length.
- In `comprehensive` mode, insert sizes now span the whole read pair instead of running from the
  start of one mate to the start of the other, and leave out spliced introns. The overlap file
  reports `inner_distance` instead of `overlap_size`.

### 1.4.1

<span class="rerun rerun-none"><span class="rerun-label">Basic-mode data</span><span class="rerun-status">No rerun needed</span></span> <span class="rerun rerun-recommended"><span class="rerun-label">Comprehensive-mode data</span><span class="rerun-status">Rerun recommended</span></span>

- Fixed: in `comprehensive` mode, 1.4.0 did not write the coverage tables
  (`QC_files/gene_body_coverage/`, `QC_files/molecule_coverage/`), because the Polars version it
  shipped failed on them. 1.4.1 writes them, and computes them faster.

### 1.4.0

<span class="rerun rerun-recommended"><span class="rerun-label">Data from earlier versions</span><span class="rerun-status">Rerun recommended</span></span>

- Overlapping genes that share reads, such as the mitochondrial genes, are reconstructed gene
  by gene instead of as one pooled group. Faster on deep samples; molecules in those genes
  change slightly.
- Reconstruction runs one convergence sweep instead of two: faster, with near-identical
  molecules.
- Any tool option can be set under `params:` in `config.yaml`. Options that differ from the
  defaults are printed at start and recorded in `results/logs/tool_options/`. See
  [Configuration file options](input.md#input-config-options).
- `r1`, `r2`, `i1` and `i2` accept several FASTQ files, as a list or a glob pattern such as
  `fastq/*_read_1.fq.gz`, so lanes no longer need to be concatenated first. See
  [FASTQ files](input.md#input-fastq).

### 1.3.2

<span class="rerun rerun-none"><span class="rerun-label">Data from earlier versions</span><span class="rerun-status">No rerun needed</span></span>

- Reconstruction now enforces its memory budget (`max-concurrent-reads`, 5 M reads by
  default), and the prescan peaks about 40% lower.
- Up to 10 samples are reconstructed at the same time by default (`parallel_slots`).
- An interrupted reconstruction resumes from its checkpoint after an image update.

### 1.3.1

Where this changelog starts. Earlier releases are not listed or available.

(changelog-isoquant)=
## BaseCode IsoQuant Pipeline

### 1.4.3

<span class="rerun rerun-none"><span class="rerun-label">Data from earlier versions</span><span class="rerun-status">No rerun needed</span></span>

- Lower peak memory: the annotated BAM and variant support are now built one chromosome at a
  time.
- `{name}.adapted_molecules.tsv` is now written gzipped, as `{name}.adapted_molecules.tsv.gz`.

### 1.4.2

<span class="rerun rerun-none"><span class="rerun-label">Data from earlier versions</span><span class="rerun-status">No rerun needed</span></span>

- `basecode_no_context_resolve` renamed to `basecode_context_resolve`, meaning inverted. Same
  default; the old option still works.
- `annotate_bam` and `include_imputed` now default to `True`.
- `CV` tag dropped from the annotated BAM.

### 1.4.1

Where this changelog starts. Earlier releases are not listed or available.

(changelog-isoviewer)=
## IsoViewer

### 2.4.1

<span class="rerun rerun-compare"><span class="rerun-label">Reports from earlier versions</span><span class="rerun-status">Rerun for comparability</span></span>

- New DTU (R) page: assign the samples to groups, then download the transcript counts, the sample
  table and an R Markdown script that runs a differential transcript usage analysis (limma
  diffSplice) in R.
- Filters in the header limit the genes on the Overview, Genes and Transcript variants pages,
  with a histogram for each filter.
- The end-to-end share is now taken of molecules with 3′ support instead of all molecules, as in
  the run report of the BaseCode Processing Pipeline.
- QC pages flag samples whose values stand out from the others (with 4 or more samples). QC:
  BaseCode adds genes detected by biotype, and compares each gene's molecule length with the
  length of its canonical transcript.
- Gene pages mark the canonical transcript (MANE Select or Ensembl canonical).
- The DESeq2 and DTU scripts include a Methods section, and Discovery mode warns that it can
  show false positives.

### 2.4.0

<span class="rerun rerun-none"><span class="rerun-label">Reports from earlier versions</span><span class="rerun-status">No rerun needed</span></span>

- New DESeq2 (R) page: choose the samples, groups and settings, then download the counts,
  the sample table and an R Markdown script that runs DESeq2 in R.
- Samples can be renamed in the Samples table.
- Gene pages show overlapping genes, the other mode's transcript models, and protein domains for
  any selected transcript variants.
- QC: BaseCode adds genes detected per sample, and per-sample tables for molecule length and
  reads per molecule.
- The gene and transcript name filters suggest names and IDs as you type.
- "End-to-end" replaces "full-length", as in the rest of this documentation.

### 2.3.6

- First release as a standalone program for Linux, downloadable from
  [Installation](isoviewer-install.md). No Python or Docker is needed to run it.

Where this changelog starts. Earlier versions are not listed or available.
