# Third-party notices (BaseCode)

**BaseCode Processing Pipeline**, version 1.2.5
© 2026 Basic Genomics AB. All rights reserved.

This page lists the third-party software components distributed with, or invoked by, the
BaseCode Processing Pipeline, together with their licences. The full, verbatim licence
text of each component is reproduced under
[Licence texts (BaseCode)](licence-texts.md); the Licence file
column links to it.

This page mirrors the `THIRD_PARTY_NOTICES.md` file shipped inside the pipeline
repository and container image, which remains the authoritative copy.

Nothing in this document modifies the licence of any listed component. Each component
remains subject to its own licence terms.

## 1. Python libraries

Declared in `workflow/envs/requirements.txt` and
installed into the pipeline container.

| Component | Version | Licence | Copyright holder | Used by | Licence file |
| --- | --- | --- | --- | --- | --- |
| [cutadapt](https://github.com/marcelm/cutadapt) | 4.6 | MIT | Marcel Martin and contributors | adapter/quality trimming rules in `processing.smk` | [cutadapt.txt](licence-texts.md#lic-cutadapt) |
| [PyYAML](https://github.com/yaml/pyyaml) | 6.0.2 | MIT | Ingy döt Net; Kirill Simonov | config and stats YAML I/O across 10 scripts | [pyyaml.txt](licence-texts.md#lic-pyyaml) |
| [pandas](https://github.com/pandas-dev/pandas) | 2.3.0 | BSD-3-Clause | AQR Capital Management, LLC; Lambda Foundry, Inc.; PyData Development Team; open source contributors | tabular QC and stats across 11 scripts | [pandas.txt](licence-texts.md#lic-pandas) |
| [Polars](https://github.com/pola-rs/polars) | 1.32.3 | MIT | Ritchie Vink; NVIDIA Corporation (portions) | `run_report.py`, `summary_stats.py`, `make_sample_files.py`, `gene_body_coverage.py` | [polars.txt](licence-texts.md#lic-polars) |
| [PyArrow (Apache Arrow)](https://github.com/apache/arrow) | 20.0.0 | Apache-2.0 | The Apache Software Foundation | Arrow/Parquet backend for Polars and fastexcel | [pyarrow.txt](licence-texts.md#lic-pyarrow) |
| [pysam](https://github.com/pysam-developers/pysam) | 0.22.0 | MIT | Genome Research Ltd. and contributors | BAM/SAM access across 12 scripts | [pysam.txt](licence-texts.md#lic-pysam) |
| [joblib](https://github.com/joblib/joblib) | 1.3.0 | BSD-3-Clause | The joblib developers | parallelism in `count_status_per_gene.py`, `overlap_and_mi.py`, `reconstruction_lengths.py` | [joblib.txt](licence-texts.md#lic-joblib) |
| [pyfaidx](https://github.com/mdshw5/pyfaidx) | 0.9.0.3 | BSD-3-Clause | The Johns Hopkins University | `conversion_rates.py` | [pyfaidx.txt](licence-texts.md#lic-pyfaidx) |
| [NumPy](https://github.com/numpy/numpy) | 2.2.6 | BSD-3-Clause | NumPy Developers | numerics across 5 scripts | [numpy.txt](licence-texts.md#lic-numpy) |
| [pyfastx](https://github.com/lmdu/pyfastx) | 2.2.0 | MIT | Lianming Du | FASTQ indexing in `make_sample_files.py` | [pyfastx.txt](licence-texts.md#lic-pyfastx) |
| [fastexcel](https://github.com/ToucanToco/fastexcel) | 0.14.0 | MIT | ToucanToco | `.xlsx` samplesheet reader for Polars | [fastexcel.txt](licence-texts.md#lic-fastexcel) |
| [Snakemake](https://github.com/snakemake/snakemake) | 9.6.0 | MIT | The Snakemake team | workflow engine that drives the entire pipeline | [snakemake.txt](licence-texts.md#lic-snakemake) |
| [tabulate](https://github.com/astanin/python-tabulate) | 0.9.0 | MIT | Sergey Astanin and contributors | `summary_stats.py` | [tabulate.txt](licence-texts.md#lic-tabulate) |
| [ReportLab](https://www.reportlab.com/) | 4.4.9 | BSD-3-Clause (ReportLab) | ReportLab Inc. and contributors | PDF run report in `run_report.py` | [reportlab.txt](licence-texts.md#lic-reportlab) |
| [setuptools](https://github.com/pypa/setuptools) | 82.0.0 | MIT | Python Packaging Authority | build and install tooling | [setuptools.txt](licence-texts.md#lic-setuptools) |
| [MultiQC](https://github.com/MultiQC/MultiQC) | 1.25 | GPL-3.0-or-later | MultiQC contributors (Phil Ewels et al.) | aggregate QC report rule in `processing.smk` | [multiqc.txt](licence-texts.md#lic-multiqc) |
| [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl) | 3.1.2 | MIT | Eric Gazoni, Charlie Clark and contributors | `.xlsx` samplesheet reader for pandas | [openpyxl.txt](licence-texts.md#lic-openpyxl) |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | not pinned | Matplotlib licence (PSF-derived, BSD-compatible) | Matplotlib Development Team; John D. Hunter | figures in `run_report.py` | [matplotlib.txt](licence-texts.md#lic-matplotlib) |
| [seaborn](https://github.com/mwaskom/seaborn) | not pinned | BSD-3-Clause | Michael L. Waskom | figures in `run_report.py` | [seaborn.txt](licence-texts.md#lic-seaborn) |

## 2. External command-line tools

Invoked as separate processes from Snakemake `shell:` directives, and provided by the
pipeline container image.

| Component | Licence | Copyright holder | Invoked in | Licence file |
| --- | --- | --- | --- | --- |
| [HISAT-3N / HISAT2](https://github.com/DaehwanKimLab/hisat2) | GPL-3.0-or-later | Daehwan Kim, Chanhee Park, Ben Langmead et al. | `processing.smk`: read alignment (`binaries/hisat-3n`) | [hisat2.txt](licence-texts.md#lic-hisat2) |
| [SAMtools](https://github.com/samtools/samtools) | MIT/Expat | Genome Research Ltd.; contributors | `processing.smk`: BAM view/sort/index/flagstat (10 call sites) | [samtools.txt](licence-texts.md#lic-samtools) |
| [HTSlib](https://github.com/samtools/htslib) (`bgzip`, `tabix`) | MIT/Expat (parts BSD-3-Clause; see file) | Genome Research Ltd.; contributors | `downstream.smk`: BED compression and indexing | [htslib.txt](licence-texts.md#lic-htslib) |
| [bedtools](https://github.com/arq5x/bedtools2) | MIT | Aaron Quinlan and contributors | `downstream.smk`: `merge`, `genomecov` | [bedtools.txt](licence-texts.md#lic-bedtools) |
| [FastQC](https://github.com/s-andrews/FastQC) | GPL-3.0-or-later | Simon Andrews, Babraham Bioinformatics | `processing.smk`: raw and trimmed read QC | [fastqc.txt](licence-texts.md#lic-fastqc) |
| [Subread / featureCounts](https://subread.sourceforge.net/) | GPL-3.0-or-later | Wei Shi, Yang Liao and contributors | `processing.smk`: exon/intron gene assignment (6 call sites, run as `binaries/featureCounts`) | [subread.txt](licence-texts.md#lic-subread) |
| GNU coreutils (`sort`) and GNU awk (`awk`) | GPL-3.0-or-later | Free Software Foundation, Inc. | shell pipelines in `downstream.smk`, `processing.smk` | [GPL-3.0.txt](licence-texts.md#lic-gpl-3-0) |

## 3. First-party binaries in `binaries/`

The pipeline's compute-intensive steps run compiled binaries invoked from `shell:`
directives. `parse_fastq` (via `config[parse_fastq_bin]`), `analyze_fastq`, `move_tags`,
`rename_tags`, `basic_reconstruction` and `stitcher_rs` are Basic Genomics AB's own
software and require no third-party notice.

Note that `binaries/` also holds third-party executables: `hisat-3n` and `featureCounts`
are shipped from that directory and are covered by §2.

## 4. Language runtime

| Component | Licence | Copyright holder | Licence file |
| --- | --- | --- | --- |
| [CPython](https://github.com/python/cpython) 3.10 | PSF License Agreement 2.0 | Python Software Foundation | [python-psf.txt](licence-texts.md#lic-python-psf) |

## 5. Fonts and other assets

| Component | Licence | Copyright holder | Location | Licence file |
| --- | --- | --- | --- | --- |
| [Mona Sans](https://github.com/github/mona-sans) (Regular, Bold) | SIL Open Font License 1.1 | GitHub, Inc. (Reserved Font Name "Mona Sans") | `workflow/resources/MonaSans-Regular.ttf`, `workflow/resources/MonaSans-Bold.ttf` | [mona-sans.txt](licence-texts.md#lic-mona-sans) |

`Background_v1.1.png` and `Read_Type_Schema.png` in
`workflow/resources/` are Basic Genomics AB assets, not
third-party material.

## 6. Scope

This document was generated against the repository at version 1.2.5. It covers the
Python libraries installed from `requirements.txt`, the external tools invoked from
Snakemake `shell:` directives, the Python runtime, and the fonts shipped in
`workflow/resources/`.

It does **not** cover:

- third-party libraries compiled into the first-party binaries in `binaries/` (§3),
  whose sources are maintained outside this repository;
- packages contributed by the Ubuntu base image, which Debian/Ubuntu document through
  their own licence and source infrastructure.
