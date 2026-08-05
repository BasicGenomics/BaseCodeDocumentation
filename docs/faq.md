# FAQ

Questions that come up most often when analysing RNA BaseCode data.

Questions about the assay itself, such as RNA input amount, RNA integrity and sequencing
depth, are answered on the [Basic Genomics website](https://www.basic-genomics.com/).

This FAQ covers what the BaseCode pipelines add. For IsoQuant's own options, output formats
and algorithms, see the [official IsoQuant documentation](https://ablab.github.io/IsoQuant/).

## Running the pipelines

### Which pipeline do I run first?

The [BaseCode Processing Pipeline](overview.md) always runs first. It reads the FASTQ files
from the sequencer and produces `results/{name}.stitched.molecules.sorted.bam`, the BaseCode
Synthetic Long Reads. Everything else works from that BAM.

### Do I have to run the BaseCode IsoQuant Pipeline?

No. It is one downstream analysis, not a required step. The synthetic long reads are a
standard sorted BAM and can be used with other tools. See
[Downstream analysis](downstream.md).

### Why must `name` be the same in both configuration files?

The [BaseCode IsoQuant Pipeline](isoquant.md) locates its input as
`results/{name}.stitched.molecules.sorted.bam`, using the `name` from its own configuration
file. If the two pipelines are given different names, that file does not exist and the run
fails immediately. Set the same `name` in `config/config.yaml` and
`config_isoquant/config.yaml`.

### Why are my output files owned by `root`?

The Docker daemon runs as root by default, so files created inside the container are owned by
root. Change ownership after the run with `sudo chown -R user:group results/`. This applies to
both pipelines.

### Which image tag should I use?

Always a specific version, never `latest`. The `latest` tag does not necessarily point at the
newest release and it moves without warning. Current versions are listed on
[Container images](containers.md).

## Reference data

### Can I use my own reference genome and annotation?

Yes. As long as a genome reference and annotation are available for your species, they can be
prepared for the pipeline. See
[Generating custom genome reference and annotations](input.md).

## Working with the output

### How do I get per-sample counts rather than one number per run?

Quantification is grouped by the `SM` (sample) BAM tag by default, controlled by the
`read_group` option. Grouped files carry the tag in their name, for example
`{name}.transcript_grouped_tag_SM_counts.tsv`. All matrices are also collected into a single
`.h5mu` MuData file. See [Output](isoquant-output.md).

### Why do some reads in the annotated BAM have a sequence of all `N`?

When `include_imputed` is enabled, each molecule's alignment is rewritten to the exon
structure IsoQuant resolved, including the parts imputed across unsequenced gaps. That
structure no longer corresponds to the original read sequence base for base, so the sequence
is replaced entirely by `N` and the base qualities are flattened to a constant 30. The BAM
therefore carries the reconstructed *structure*, not the observed bases.

This applies to every rewritten molecule, not only those whose structure actually changed.
`OC` preserves the original CIGAR and `IM` records whether the CIGAR differed. Use this BAM
for inspecting structure and assignment, and the processing pipeline's BAM for anything
base-level. See [BAM file tags](isoquant-tags.md).

### Why is one molecule assigned to several isoforms?

Reconstructed molecules are often compatible with more than one annotated isoform. With the
default `duplicate_mode: all`, every compatible isoform is recorded, `;`-joined in the `ZI`
and `ZE` tags. Set `duplicate_mode` to `best` or `first` for a single isoform per molecule.

## Analysis choices

### Why does BaseCode data need its own IsoQuant options?

Reconstructed molecules differ from natively sequenced long reads in two ways: they contain
unsequenced inner gaps that appear as CIGAR deletions, and their ends are measured rather than
inferred. BaseCode mode imputes structure across those gaps and disables the exon corrector.
See [Why BaseCode data needs its own options](isoquant-input.md#basecode-options).

### Why does the pipeline collapse the reference annotation?

Reference annotations contain many transcripts that differ only marginally, most often in
their UTR boundaries, which are not precisely fixed to begin with. Without collapsing,
molecules from a single transcript are spread across several near-identical entries, diluting
the counts and making unambiguous assignments look ambiguous. Collapsing is on by default and
can be turned off. See [Annotation collapsing](isoquant-input.md#annotation-collapsing).

### Should I analyse only full-length molecules?

Only if the analysis calls for it. Setting `full_length_only` passes just the molecules whose
3′ and 5′ ends were both observed, which is stricter but reduces depth. It is off by default.
See [Input](isoquant-input.md).

## Getting help

### Something failed, where do I look?

Each pipeline writes per-step logs into its `logs/` folder inside `results/`. The IsoQuant
pipeline additionally records the resolved run configuration and component versions in
`results/isoquant/logs/{name}.versions.log`, and points at
`results/isoquant/.snakemake/log/` on failure.

### Is there a community I can join?

Yes. The **BaseCode Community** on Slack is where users and the Basic Genomics team discuss
analysis, share approaches and answer questions.

<a href="https://join.slack.com/t/basecodecommunity/shared_invite/zt-46ew1ilgw-CFRpfscTeyPlml7FJM0XSA"
   class="brand-button">
  Join the BaseCode Community on Slack
</a>

### How do I get help with my analysis?

For anything you would rather not discuss publicly, get in touch directly and we will help.

<a href="mailto:info@basic-genomics.com?subject=RNA%20BaseCode%20data%20analysis%20question&body=Hi,%0A%0AI%20have%20a%20question%20about%20analysing%20RNA%20BaseCode%20data.%0A%0AQuestion:%0A%0AKind%20regards,%0A"
   class="brand-button">
  Ask us a question
</a>
