# Changelog

Newest first. Each release says whether existing results need regenerating.

:::{div}
:class: table-centered

| Label | Meaning |
| --- | --- |
| **No rerun** | Results are unchanged. Use the new version for new runs. |
| **Rerun for comparability** | Results shift slightly. Keep one study on one version. |
| **Rerun recommended** | Analysis logic changed. Rerun affected samples. |

:::

Rerunning the Processing Pipeline also means rerunning IsoQuant. Not the reverse.

## BaseCode Processing Pipeline

### 1.2.6 — No rerun

- Reconstruction is split by `SM` tag: lower peak memory, same molecules.

### 1.2.5

Where this changelog starts. Earlier releases are not listed.

## BaseCode IsoQuant Pipeline

### 1.4.2 — No rerun

- `basecode_no_context_resolve` renamed to `basecode_context_resolve`, meaning inverted. Same
  default; the old option still works.
- `annotate_bam` and `include_imputed` now default to `True`.
- `CV` tag dropped from the annotated BAM.

### 1.4.1

Where this changelog starts. Earlier releases are not listed.
