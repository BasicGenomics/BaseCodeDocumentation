# Input

## Where it sits in the workflow

The pipeline reads the sorted BAM of stitched molecules written by the BaseCode Processing
Pipeline, and writes everything it produces into a new `isoquant/` subfolder of that same
`results/` folder:

```
results/
├─ {name}.stitched.molecules.sorted.bam   ⟵ produced by the BaseCode Processing Pipeline
└─ isoquant/                              ⟵ produced by the BaseCode IsoQuant Pipeline
```

:::{important} Use the same `name` for both pipelines
The BaseCode IsoQuant Pipeline locates its input as
`results/{name}.stitched.molecules.sorted.bam`, where `{name}` is the `name` option in its
own configuration file. If the two pipelines are given different names, the BAM produced by
the first is not found by the second and the run fails immediately.

Set `name` to the same value in both configuration files: `config/config.yaml` for the
processing pipeline and `config_isoquant/config.yaml` for this one.
:::

## Input overview

The BaseCode IsoQuant Pipeline requires the following input:

- **[Stitched molecule BAM](output.md)**: `results/{name}.stitched.molecules.sorted.bam`,
  produced by the [BaseCode Processing Pipeline](overview.md). Nothing needs to be copied or
  renamed, because the same `results/` folder is mounted into both containers.
- **[Genome reference and annotations](input.md#input-reference)**: the same
  `genome_references/` resource directory used by the processing pipeline. The reference FASTA
  and the GFF3 gene annotation are both read from it.
- **[Configuration file](#iq-config)**: points the pipeline at the reference and defines how
  reads are assigned and quantified.

The configuration file is placed in a `config_isoquant/` folder on the host, kept separate
from the processing pipeline's `config/` folder so the two configurations cannot be confused.
It is mounted as the container's `config/` folder (see
[Starting the Pipeline](isoquant-pipeline.md)).

The proposed directory structure:

```
├─ BaseCode/
│  ├─ config/
│     ├─ config.yaml                ⟵ BaseCode Processing Pipeline configuration
│     ├─ SampleSheet.xlsx
│  ├─ config_isoquant/
│     ├─ config.yaml                ⟵ BaseCode IsoQuant Pipeline configuration
│  ├─ fastq/
│  ├─ results/
│     ├─ {name}.stitched.molecules.sorted.bam
│     ├─ isoquant/                  ⟵ results of the BaseCode IsoQuant Pipeline appear here
├─ BaseCode_resources/
│  ├─ genome_references/
│     ├─ Homo_sapiens/
│        ├─ reference.fa
│        ├─ geneannotations*
│     ├─ ...
```

(iq-config)=
## Configuration file

The configuration file (`config_isoquant/config.yaml`) contains all the information needed to
run the BaseCode IsoQuant Pipeline and uses the YAML language. Only `name` and `reference`
are required; every other option has a carefully chosen default tuned for BaseCode data.

>**IMPORTANT** The paths specified in the configuration file are relative paths in the Docker
container, not the paths on your host machine. The paths on your host machine are specified
when running the pipeline (see [Starting the Pipeline](isoquant-pipeline.md)).

The [configuration builder](config-builder.md) can generate this file, and the matching
`docker run` command, from a form.

Minimal configuration file (`config.yaml`):

```yaml
name: 'TEST_RUN'
reference: 'Homo_sapiens'
```

Configuration file with every option written out explicitly. This mirrors the configuration
shipped with the pipeline, and every value is the pipeline default. Set `annotate_bam` and
`include_imputed` to `True` if you want the annotated BAM:

```yaml
name: 'TEST_RUN'
reference: 'Homo_sapiens'
full_length_only: False
collapse_annotation: True
collapse_mode: cds
collapse_representative: canonical
basecode_max_gap: 550
basecode_correct: False
basecode_keep_ambiguous_imputation: True
basecode_no_context_resolve: False
basecode_end_resolve: True
basecode_intron_resolve: True
data_type: pacbio_ccs
matching_strategy: precise
delta: auto
transcript_quantification: unique_only
gene_quantification: unique_splicing_consistent
model_construction_strategy: default_pacbio
polya_requirement: auto
annotate_bam: False
duplicate_mode: all
include_imputed: False
assess_variant_support: True
variant_support_mode: both
```

(basecode-options)=
## Why BaseCode data needs its own options

BaseCode Synthetic Long Reads are *reconstructed* molecules, not natively sequenced long
reads, and they differ from what IsoQuant normally sees in two ways that matter:

- **They contain unsequenced inner gaps.** A molecule is stitched together from reads
  covering parts of it, so the region between two covered stretches may never have been
  sequenced. In the BAM this appears as a CIGAR deletion (`D`) block. Standard IsoQuant would
  read such a block as evidence of a genuine deletion rather than missing information.
- **Their ends are recorded, not inferred.** The processing pipeline records whether a
  molecule's 3′ and 5′ ends were actually observed, so full-length status is a measured
  property rather than something guessed from the alignment. The two ends are not equally
  strong evidence, however. The 3′ end is anchored by poly-dT priming at the poly-A tail,
  whereas the 5′ end marks only where reverse transcription and template switching stopped.

**BaseCode mode** (the `--basecode` flag, always enabled by this pipeline) addresses the
first point: it imputes exon structure across unsequenced inner-mate gaps and disables
IsoQuant's exon corrector, which would otherwise try to "fix" alignments that are already
correct. The `basecode_*` options below tune how aggressively that imputation and the
resulting isoform assignment are resolved. Without the flag, behaviour is identical to
upstream IsoQuant.

## Configuration file options

In the following description, *Required* means the configuration option must be specified in
the `config.yaml` file. *Optional* means that the configuration option is either not strictly
necessary or has a carefully chosen default value which can be overridden by specifying
another value in `config.yaml`.

### Run and reference

| Configuration option | Description |
|----------------------|-------------|
| **name** | **Required.** String. Name of the run. **Must be identical to the `name` used in the BaseCode Processing Pipeline**, as it is used to locate `results/{name}.stitched.molecules.sorted.bam`. |
| **reference** | **Required.** String. Name of the folder in the specified `.../BaseCode_resources/genome_references/` path containing the required genome reference and annotation files. |
| **read_group** | **Optional.** String. BAM tag used to group reads for per-sample quantification. Appears in output filenames with `:` replaced by `_` (so `tag:SM` produces `..._grouped_tag_SM_counts.tsv`). [**Default:** `tag:SM`]. |

### Molecule preparation

| Configuration option | Description |
|----------------------|-------------|
| **full_length_only** | **Optional.** Boolean. If `True`, only full-length molecules (`TC` > 0 and `FC` > 0, i.e. both ends observed) are passed to IsoQuant; all others are discarded. Useful for a strict, high-confidence isoform analysis at the cost of depth. [**Default:** `False`]. |

(annotation-collapsing)=
### Annotation collapsing

Reconstructed molecules often cannot distinguish between reference isoforms that differ only
in their UTRs. Collapsing groups such transcripts and keeps one representative, so reads are
not split across near-duplicate isoforms.

| Configuration option | Description |
|----------------------|-------------|
| **collapse_annotation** | **Optional.** Boolean. If `True`, the reference annotation is collapsed before use and the collapsed GFF3 is used for assignment and quantification. If `False`, the reference annotation is used unchanged. [**Default:** `True`]. |
| **collapse_mode** | **Optional.** String, one of `chain`, `cds`, `chain_cds`. What counts as "the same body" when grouping transcripts. `chain` groups by the intron chain implied by the exon coordinates, `cds` groups by the CDS block coordinates, and `chain_cds` requires both to match. See [Choosing a collapse mode](#collapse-mode-detail) for what this means in practice. [**Default:** `cds`]. |
| **collapse_representative** | **Optional.** String, one of `canonical`, `longest`. Which transcript to keep per group: `canonical` keeps the best-tagged transcript, tie-broken by longest span; `longest` keeps the longest span (longest UTRs), so molecules with long UTRs still fit inside it, tie-broken by tag. [**Default:** `canonical`]. |

(collapse-mode-detail)=
#### Choosing a collapse mode

`chain` and `cds` look at different parts of a transcript, and neither is simply stricter than
the other.

- `chain` uses the introns implied by the exon coordinates. Only the gaps between
  consecutive exons enter the key, so the transcript's outer start and end are ignored: two
  transcripts whose UTRs differ only in length still group together. Any difference in
  splicing does separate them, including an intron inside a UTR.
- `cds` uses the CDS block coordinates themselves. Identical CDS blocks imply identical
  gaps between them, so the intron structure of the coding region is captured too; what
  `cds` cannot see is splicing in the UTRs. The positions where coding starts and stops are
  part of the key. Transcripts with no CDS fall back to their intron chain and are never
  merged with coding transcripts.

The cases where the two disagree:

| Two transcripts that... | `chain` | `cds` |
| --- | --- | --- |
| have the same CDS but differently spliced UTRs | kept separate | grouped |
| have the same intron chain but a different annotated ORF | grouped | kept separate |
| are one coding and one non-coding, sharing an intron chain | grouped | kept separate |

Because UTR differences are the dominant source of near-duplicate isoforms, `cds` groups far
more than `chain` in practice, and `chain_cds` requires both keys to match so it groups the
least. `cds` is the default because UTR boundaries are precisely what reconstructed molecules
cannot pin down.

Single-exon transcripts are handled separately. Under `chain` none of them have an intron
chain, so all are clustered by overlapping span instead. Under `cds` only the non-coding ones
are; a single-exon coding transcript still has CDS blocks and is grouped by those.

### BaseCode mode

These options control how unsequenced inner gaps are imputed and how ambiguous isoform
assignments are resolved. They exist because BaseCode molecules carry information that native
long reads do not. See [above](#basecode-options).

| Configuration option | Description |
|----------------------|-------------|
| **basecode_max_gap** | **Optional.** Integer. Maximum unsequenced exonic gap, in base pairs, that will be imputed as a contiguous exon when no annotated intron matches it. Molecules with larger gaps are skipped. [**Default:** `550`]. |
| **basecode_keep_ambiguous_imputation** | **Optional.** Boolean. If `True`, molecules whose gap imputation was not unique are kept rather than skipped. Molecules that impute to no exons at all are still dropped either way. [**Default:** `True`]. |
| **basecode_no_context_resolve** | **Optional.** Boolean. Disables context-constrained imputation. By default, when a gap cannot be filled uniquely across the whole gene, the molecule's *sequenced* introns are used to narrow the candidates to compatible isoforms and the gap is resolved from those. Setting this to `True` reverts to gene-wide-only imputation. [**Default:** `False`]. |
| **basecode_intron_resolve** | **Optional.** Boolean. When a molecule is consistent with several isoforms, resolve to the isoform(s) whose **intron chain** matches most exactly, ignoring terminal and UTR differences. This prevents an end-truncated molecule from being pulled to a near-duplicate isoform by a coincidental TSS or poly-A match when its splice chain uniquely identifies another isoform. [**Default:** `True`]. |
| **basecode_end_resolve** | **Optional.** Boolean. For full-length molecules (`TC` > 0 and `FC` > 0) that still match several isoforms, keep only exact full-splice matches and drop the longer isoforms that the molecule is merely nested inside. Uses the validated molecule ends to break end-containment ambiguity. [**Default:** `True`]. |
| **basecode_correct** | **Optional.** Boolean. Also run IsoQuant's exon corrector. BaseCode mode disables it by design, because BaseCode alignments do not need correcting. For comparison and experiments only. [**Default:** `False`]. |

### Assignment and quantification

These are standard IsoQuant options; the defaults below are the values Basic Genomics has
found appropriate for BaseCode data.

| Configuration option | Description |
|----------------------|-------------|
| **data_type** | **Optional.** String. IsoQuant data type profile. BaseCode Synthetic Long Reads are accurate, so the PacBio HiFi profile is used. [**Default:** `pacbio_ccs`]. |
| **matching_strategy** | **Optional.** String, one of `exact`, `precise`, `default`, `loose`. How strictly a molecule's splice sites must match an isoform. `precise` suits the low error rate of BaseCode molecules. [**Default:** `precise`]. |
| **delta** | **Optional.** Integer or `auto`. Allowed deviation, in base pairs, when comparing splice sites. `auto` lets IsoQuant derive it from `data_type` and `matching_strategy`. [**Default:** `auto`]. |
| **transcript_quantification** | **Optional.** String. Which read assignments count towards a transcript. `unique_only` counts only molecules assigned unambiguously to a single isoform, which keeps transcript-level counts conservative. [**Default:** `unique_only`]. |
| **gene_quantification** | **Optional.** String. Which read assignments count towards a gene. `unique_splicing_consistent` additionally accepts molecules that are ambiguous between isoforms of the same gene but consistent with its splicing, since the gene assignment is unambiguous. [**Default:** `unique_splicing_consistent`]. |
| **model_construction_strategy** | **Optional.** String. How novel transcript models are built. [**Default:** `default_pacbio`]. |
| **polya_requirement** | **Optional.** String. How strictly a poly-A tail is required when building and assigning models. Molecules whose 3′ end was observed carry a synthetic poly-A tail added during molecule preparation, so `auto` is appropriate. [**Default:** `auto`]. |

### Annotated BAM

| Configuration option | Description |
|----------------------|-------------|
| **annotate_bam** | **Optional.** Boolean. If `True`, write `results/isoquant/{name}.annotated.sorted.bam`, a copy of the molecules carrying their IsoQuant assignment in custom tags. See [BAM file tags](isoquant-tags.md). [**Default:** `False`]. |
| **duplicate_mode** | **Optional.** String, one of `first`, `best`, `all`. How to record a molecule that is compatible with more than one isoform: `first` keeps the first row, `best` keeps the highest-priority assignment type (one isoform), `all` records every compatible isoform with the `ZI` and `ZE` tags `;`-joined and positionally aligned. [**Default:** `all`]. |
| **include_imputed** | **Optional.** Boolean. If `True`, each molecule's CIGAR in the annotated BAM is rewritten to its imputed exon/intron structure, so the reconstructed structure is what a genome browser displays. The original CIGAR is preserved in the `OC` tag and `IM` marks whether it changed. [**Default:** `False`]. |

### Variant support

| Configuration option | Description |
|----------------------|-------------|
| **assess_variant_support** | **Optional.** Boolean. If `True`, compute per-variant read support for transcripts. [**Default:** `True`]. |
| **variant_support_mode** | **Optional.** String, one of `discovered`, `reference`, `both`. Which transcript set to assess. [**Default:** `both`]. |

The file **must** be named `config.yaml`, since that is what the pipeline reads from the configuration folder you mount. The folder itself can be called anything; this documentation calls it `config_isoquant/` to keep it apart from the processing pipeline's configuration:

```
mkdir config_isoquant
cp /path/to/config.yaml config_isoquant/
```
