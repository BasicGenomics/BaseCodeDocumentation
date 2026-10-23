# Overview

**IsoViewer** turns the results of the [BaseCode IsoQuant Pipeline](isoquant.md) into one
interactive HTML report. The report is a single file: it opens in any web browser, works
offline and needs no server, so it can be shared by email or archived together with the run.

IsoViewer is a single program for Linux with nothing else to install. It runs where the
results are, typically on the machine that ran the pipelines. See
[Installation](isoviewer-install.md) and [Building a report](isoviewer-build.md).

## The report

| Page | What it shows |
| --- | --- |
| **Overview** | Headline figures, and where every molecule went: counted or dropped. |
| **QC: BaseCode** | Reads, reconstruction and end-to-end molecules. |
| **QC: IsoQuant** | How molecules were assigned to genes and transcripts. |
| **Genes** | All genes to filter and sort; open one to see its transcript variants. |
| **Transcripts** | The same, per transcript. |
| **Samples** | Totals, correlation, PCA and clustering per sample. |
| **Compare groups** | Two groups of samples compared. |
| **Run & provenance** | Versions, references and settings of the run. |

Three settings at the top of the report apply to every page:

- **Mode.** Reference mode shows the quantification of the existing annotation. Discovery
  mode shows the transcript models IsoQuant built from the reads.
- **Samples.** The samples included in every figure and table.
- **Stringency.** The minimum number of counted molecules a gene needs to count as
  quantified.

A short guided tour in the report walks through these settings and the main pages. Hover any
ⓘ for the definition of a figure.

## Viewing and sharing a report

Open the report in a current version of Chrome, Edge, Firefox or Safari. It loads nothing from
the internet, so it also works on a computer without a network connection.

The report contains the results of the run, gene by gene and sample by sample. Share it as you
would share the results themselves.
