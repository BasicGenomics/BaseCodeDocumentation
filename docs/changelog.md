# Changelog

Newest first. Each release says whether existing results need regenerating.

:::{div}
:class: table-centered

| Label | Meaning |
| --- | --- |
| <span class="rerun rerun-none">No rerun</span> | Results are unchanged. Use the new version for new runs. |
| <span class="rerun rerun-compare">Rerun for comparability</span> | Results shift slightly. Keep one study on one version. |
| <span class="rerun rerun-recommended">Rerun recommended</span> | Analysis logic changed. Rerun affected samples. |

:::

Rerunning the Processing Pipeline also means rerunning IsoQuant. Not the reverse.

## BaseCode Processing Pipeline

### 1.4.0 “Kebnekaise”

<span class="rerun rerun-compare">Rerun for comparability</span>

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

<span class="rerun rerun-none">No rerun</span>

- Reconstruction now enforces its memory budget (`max-concurrent-reads`, 5 M reads by
  default), and the prescan peaks about 40% lower.
- Up to 10 samples are reconstructed at the same time by default (`parallel_slots`).
- An interrupted reconstruction resumes from its checkpoint after an image update.

### 1.3.1

Where this changelog starts. Earlier releases are not listed.

## BaseCode IsoQuant Pipeline

### 1.4.3

<span class="rerun rerun-none">No rerun</span>

- Lower peak memory: the annotated BAM and variant support are now built one chromosome at a
  time.
- `{name}.adapted_molecules.tsv` is now written gzipped, as `{name}.adapted_molecules.tsv.gz`.

### 1.4.2

<span class="rerun rerun-none">No rerun</span>

- `basecode_no_context_resolve` renamed to `basecode_context_resolve`, meaning inverted. Same
  default; the old option still works.
- `annotate_bam` and `include_imputed` now default to `True`.
- `CV` tag dropped from the annotated BAM.

### 1.4.1

Where this changelog starts. Earlier releases are not listed.
