# Basic Genomics Pipelines

<div class="hero">

Documentation

RNA BaseCode is a library preparation chemistry that marks every RNA molecule with its own
pattern, so that reads coming from the same original molecule can be recognised in ordinary
short-read sequencing and stitched back into a full-length transcript. This site documents
the analysis side: the pipelines that take the reads from an RNA BaseCode library,
reconstruct them into **BaseCode Synthetic Long Reads**, and quantify isoforms from them.

</div>

```{mermaid}
flowchart LR
  FQ["Sequencer reads<br/>(FASTQ)"]:::io --> P1["BaseCode<br/>Processing Pipeline"]:::pipe
  P1 --> BAM["BaseCode Synthetic<br/>Long Reads (BAM)"]:::io
  BAM --> P2["BaseCode<br/>IsoQuant Pipeline"]:::pipe
  BAM -.-> OTHER["Other downstream<br/>analyses"]:::opt
  P2 --> OUT["Isoform counts and TPM<br/>(TSV, MuData)"]:::io
  classDef pipe fill:#EC008C,stroke:#EC008C,color:#FFFFFF,font-weight:600
  classDef io fill:#F3F4F6,stroke:#9CA3AF,color:#111317
  classDef opt fill:#FFFFFF,stroke:#9CA3AF,color:#4B5563,stroke-dasharray:4 3
```

## How it works

Reverse transcription leaves every RNA molecule with its own signature of mismatches. Reads
carrying the same signature came from the same molecule, so they can be grouped and stitched
back into a full-length transcript.
[Try the interactive explainer](how-it-works.md).

## Pipelines

::::{grid} 1 1 2 2

:::{card} BaseCode Processing Pipeline
:link: overview.md

Turns unmapped reads from a compatible sequencer into **BaseCode Synthetic Long Reads**
mapped to the reference genome, together with quality control metrics for overall assay
quality.
:::

:::{card} BaseCode IsoQuant Pipeline
:link: isoquant.md

Takes the BaseCode Synthetic Long Reads from the processing pipeline and performs
isoform-level assignment, transcript discovery and quantification against a reference
annotation.
:::

::::

<div class="statusbar">

| Pipeline | Image | Current release |
| --- | --- | --- |
| BaseCode Processing Pipeline | [`basicgenomics/basecode`](https://hub.docker.com/r/basicgenomics/basecode) | [![](https://img.shields.io/docker/v/basicgenomics/basecode?sort=semver&label=%20&color=EB0079)](https://hub.docker.com/r/basicgenomics/basecode/tags) |
| BaseCode IsoQuant Pipeline | [`basicgenomics/basecode_isoquant`](https://hub.docker.com/r/basicgenomics/basecode_isoquant) | [![](https://img.shields.io/docker/v/basicgenomics/basecode_isoquant?sort=semver&label=%20&color=EB0079)](https://hub.docker.com/r/basicgenomics/basecode_isoquant/tags) |

</div>

## Community

<div class="community">

![Slack](images/slack-mark.png)

**Join the BaseCode Community on Slack**, where users and the Basic Genomics team discuss
analysis, share approaches and answer each other's questions.

<a href="https://join.slack.com/t/basecodecommunity/shared_invite/zt-46ew1ilgw-CFRpfscTeyPlml7FJM0XSA"
   class="brand-button">
  Join on Slack
</a>

</div>

## Getting oriented

- **New to the assay?** Start with the [BaseCode Processing Pipeline overview](overview.md).
- **Have a question?** The [FAQ](faq.md) covers the questions that come up most often when
  analysing BaseCode data.
- **Looking for the Docker images?** See [Container images](containers.md).
- **Going further with your results?** The [Vignettes](vignettes.md) are standalone guides
  for analyses built on top of pipeline output, such as working with the BAM tags and
  visualisation. Instructions for running each pipeline live in that pipeline's own section.
