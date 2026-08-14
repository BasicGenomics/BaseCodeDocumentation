# Changelog

Release history for both pipelines, newest first. Each release carries a **rerun impact**
label saying whether existing results should be regenerated with the new version.

## Do I need to rerun?

Upgrading is always recommended, but an upgrade rarely means existing results are wrong. The
label on each release below says what an upgrade means for data you have already processed.

:::{div}
:class: table-centered

| Label | What it means | What to do |
| --- | --- | --- |
| **No rerun** | Performance, logging, packaging or output-formatting changes only. The molecules, assignments and counts a rerun would produce are identical. | Use the new version for new runs. Leave existing results as they are. |
| **Rerun for comparability** | Results change slightly, but neither version is wrong. Mixing versions within one study is what causes trouble. | Keep a study on one version. Rerun only if a study spans both. |
| **Rerun recommended** | A change to the analysis logic that alters molecules, assignments or counts in a way that materially affects interpretation. | Rerun affected samples before drawing conclusions from them. |

:::

:::{important} Version pairing
The two pipelines are versioned independently, and the BaseCode IsoQuant Pipeline reads the
BAM produced by the BaseCode Processing Pipeline. A **Rerun recommended** entry for the
Processing Pipeline therefore also invalidates the IsoQuant results derived from it, because
the molecules themselves changed. The reverse is not true: rerunning IsoQuant never requires
reprocessing.
:::

## BaseCode Processing Pipeline

### 1.2.6

**Rerun impact: No rerun**

- **Reconstruction is split by `SM` tag.** Molecule reconstruction now processes each sample
  separately rather than holding the whole run at once, which reduces peak memory and lets
  large multi-sample runs complete on smaller machines. Reads are grouped by their `SM` tag,
  so a molecule is still assembled from exactly the reads that belong to its sample and the
  reconstructed molecules are unchanged.

### 1.2.5

Baseline for this changelog. Earlier releases are not recorded here.

## BaseCode IsoQuant Pipeline

### 1.4.2

**Rerun impact: No rerun**

Small fixes and output-size reductions. No change to assignment, quantification or transcript
model construction — counts from 1.4.1 and 1.4.2 are identical.

- **`basecode_no_context_resolve` renamed to `basecode_context_resolve`**, with the meaning
  inverted so it reads positively like the other `basecode_*` options: `basecode_context_resolve: True`
  is exactly the old `basecode_no_context_resolve: False`, which was already the default. The
  old option is still accepted and translated, with a warning. See
  [Configuration file options](isoquant-input.md).
- **`annotate_bam` and `include_imputed` now default to `True`.** These were already `True` in
  the shipped `config.yaml`; the internal fallbacks disagreed, so a configuration file that
  simply omitted them behaved differently from one that spelled them out. Both paths now
  produce the annotated BAM.
- **The annotated BAM no longer carries the `CV` tag.** The per-molecule coverage-interval tag
  is the largest tag in the stitched BAM — roughly 54 MB per million molecules — and nothing
  downstream reads it. It is still present in
  `results/{name}.stitched.molecules.sorted.bam`, which remains the archival copy.
- Fixed base-quality handling when adapting the stitched BAM for IsoQuant.
- Run logging now records the pipeline version, the active mode and the version of every
  workflow script in `results/isoquant/logs/{name}.versions.log`.

### 1.4.1

Baseline for this changelog. Earlier releases are not recorded here.
