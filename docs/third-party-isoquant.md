# Third-party notices (IsoQuant)

**BaseCode IsoQuant Pipeline**, version 1.4.2 ("Midsommar")  
IsoQuant engine build `3.13.0.bg`  
© 2026 Basic Genomics AB. All rights reserved.

This page lists the third-party software components distributed with, or invoked by, the
BaseCode IsoQuant Pipeline, together with their licences. The full, verbatim licence text
of each component is reproduced under
[Licence texts (IsoQuant)](licence-texts-isoquant.md); the
Licence file column links to it.

Nothing in this document modifies the licence of any listed component. Each component
remains subject to its own licence terms.

## 1. The IsoQuant engine

The pipeline runs IsoQuant, which is licensed under the **GNU General Public License,
version 2**. Basic Genomics distributes a modified build (`3.13.0.bg`) that adds the
`--basecode*` options used by this pipeline. Those modifications are a derivative work of
IsoQuant and are therefore also governed by the GPL-2.0.

| Component | Licence | Copyright holder | Used for | Licence file |
| --- | --- | --- | --- | --- |
| [IsoQuant](https://github.com/ablab/IsoQuant) 3.13.0.bg | GPL-2.0-only | University of Helsinki (2022–2026); Saint Petersburg State University (2020–2022) | isoform assignment, quantification and transcript discovery, run as `IsoQuant/isoquant.py` from `run_isoquant.smk` | [isoquant.txt](licence-texts-isoquant.md#lic-iq-isoquant), [isoquant-gpl-2.0.txt](licence-texts-isoquant.md#lic-iq-isoquant-gpl-2-0) |

## 2. Python libraries (pipeline)

Declared in `workflow/envs/requirements.txt` and installed into the pipeline container.

| Component | Requirement | Licence | Copyright holder | Used by | Licence file |
| --- | --- | --- | --- | --- | --- |
| [gffutils](https://github.com/daler/gffutils) | `>=0.10.1` | MIT | Ryan Dale | GFF/GTF database access in `collapse_annotation.py`, `make_mudata.py` | [gffutils.txt](licence-texts-isoquant.md#lic-iq-gffutils) |
| [Biopython](https://github.com/biopython/biopython) | `>=1.76` | Biopython License Agreement | The Biopython Contributors | sequence utilities (via IsoQuant) | [biopython.txt](licence-texts-isoquant.md#lic-iq-biopython) |
| [pandas](https://github.com/pandas-dev/pandas) | `>=1.0.1` | BSD-3-Clause | AQR Capital Management, LLC; Lambda Foundry, Inc.; PyData Development Team; open source contributors | tabular I/O in `make_mudata.py`, `assess_variant_support.py` | [pandas.txt](licence-texts-isoquant.md#lic-iq-pandas) |
| [pybedtools](https://github.com/daler/pybedtools) | `>=0.8.1` | MIT | Ryan Dale | interval operations | [pybedtools.txt](licence-texts-isoquant.md#lic-iq-pybedtools) |
| [pysam](https://github.com/pysam-developers/pysam) | `>=0.15` | MIT | Genome Research Ltd. and contributors | BAM access in `modify_bam.py`, `annotate_bam.py`, `assess_variant_support.py` | [pysam.txt](licence-texts-isoquant.md#lic-iq-pysam) |
| [packaging](https://github.com/pypa/packaging) | not pinned | Apache-2.0 OR BSD-2-Clause | Donald Stufft and individual contributors | version handling | [packaging.txt](licence-texts-isoquant.md#lic-iq-packaging) |
| [pyfaidx](https://github.com/mdshw5/pyfaidx) | `>=0.7` | BSD-3-Clause | The Johns Hopkins University | indexed FASTA access (via IsoQuant) | [pyfaidx.txt](licence-texts-isoquant.md#lic-iq-pyfaidx) |
| [PyYAML](https://github.com/yaml/pyyaml) | `>=5.4` | MIT | Ingy döt Net; Kirill Simonov | config YAML I/O | [pyyaml.txt](licence-texts-isoquant.md#lic-iq-pyyaml) |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | `>=3.1.3` | Matplotlib licence (PSF-derived, BSD-compatible) | Matplotlib Development Team; John D. Hunter | figures | [matplotlib.txt](licence-texts-isoquant.md#lic-iq-matplotlib) |
| [NumPy](https://github.com/numpy/numpy) | `>=1.18.1` | BSD-3-Clause (bundled components 0BSD, MIT, Zlib, CC0-1.0) | NumPy Developers | numerics across the workflow scripts | [numpy.txt](licence-texts-isoquant.md#lic-iq-numpy) |
| [SciPy](https://github.com/scipy/scipy) | `>=1.4.1` | BSD-3-Clause | Enthought, Inc.; SciPy Developers | statistics in `assess_variant_support.py` | [scipy.txt](licence-texts-isoquant.md#lic-iq-scipy) |
| [seaborn](https://github.com/mwaskom/seaborn) | `>=0.10.0` | BSD-3-Clause | Michael L. Waskom | figures | [seaborn.txt](licence-texts-isoquant.md#lic-iq-seaborn) |
| [AnnData](https://github.com/scverse/anndata) | `==0.11.1` | BSD-3-Clause | Philipp Angerer; Alex Wolf; the scverse contributors | annotated count matrices in `make_mudata.py` | [anndata.txt](licence-texts-isoquant.md#lic-iq-anndata) |
| [MuData](https://github.com/scverse/mudata) | not pinned | BSD-3-Clause | Danila Bredikhin and contributors | multimodal `.h5mu` output in `make_mudata.py` | [mudata.txt](licence-texts-isoquant.md#lic-iq-mudata) |
| [Snakemake](https://github.com/snakemake/snakemake) | `==9.6.0` | MIT | The Snakemake team | workflow engine that drives the entire pipeline | [snakemake.txt](licence-texts-isoquant.md#lic-iq-snakemake) |

## 3. Python libraries (additionally required by the IsoQuant engine)

Declared in `IsoQuant/requirements.txt`, on top of those in §2.

| Component | Requirement | Licence | Copyright holder | Used by | Licence file |
| --- | --- | --- | --- | --- | --- |
| [ssw-py](https://github.com/libnano/ssw-py) | `>=1.0.0` | MIT | Nick Conway; Ben Pruitt; contributors (wraps Mengyao Zhao's SSW library) | Smith-Waterman alignment inside IsoQuant | [ssw-py.txt](licence-texts-isoquant.md#lic-iq-ssw-py) |
| [editdistance](https://github.com/roy-ht/editdistance) | `>=0.8.1` | MIT | Hiroyuki Tanaka | Levenshtein distance inside IsoQuant | [editdistance.txt](licence-texts-isoquant.md#lic-iq-editdistance) |
| [Numba](https://github.com/numba/numba) | `>=0.58` | BSD-2-Clause | Anaconda, Inc. and contributors | JIT acceleration inside IsoQuant | [numba.txt](licence-texts-isoquant.md#lic-iq-numba) |

## 4. External command-line tools

Invoked as separate processes from Snakemake `shell:` directives.

| Component | Licence | Copyright holder | Invoked in | Licence file |
| --- | --- | --- | --- | --- |
| [SAMtools](https://github.com/samtools/samtools) | MIT/Expat | Genome Research Ltd.; contributors | `run_isoquant.smk`: BAM index and sort (3 call sites) | [samtools.txt](licence-texts-isoquant.md#lic-iq-samtools) |

## 5. Language runtime

| Component | Licence | Copyright holder | Licence file |
| --- | --- | --- | --- |
| [CPython](https://github.com/python/cpython) 3.10 | PSF License Agreement 2.0 | Python Software Foundation | [python-psf.txt](licence-texts-isoquant.md#lic-iq-python-psf) |

## 6. Optional utilities (IsoQuant Viewer)

The `utilities/` directory provides the optional IsoQuant Viewer, installed from its own
conda environment (`utilities/isoquant_viewer.yaml`). These components are **not** part of
the pipeline container and are only needed if the viewer is used.

| Component | Version | Licence | Copyright holder | Used by | Licence file |
| --- | --- | --- | --- | --- | --- |
| [oarfish](https://github.com/COMBINE-lab/oarfish) | `0.5.1` | BSD-3-Clause | COMBINE-lab | alternative transcript quantification | [oarfish.txt](licence-texts-isoquant.md#lic-iq-oarfish) |
| [bedtools](https://github.com/arq5x/bedtools2) | `2.31.0` | MIT | Aaron Quinlan and contributors | interval operations behind pybedtools | [bedtools.txt](licence-texts-isoquant.md#lic-iq-bedtools) |
| [Polars](https://github.com/pola-rs/polars) | `1.35.2` | MIT | Ritchie Vink and contributors | tabular I/O in the viewer | [polars.txt](licence-texts-isoquant.md#lic-iq-polars) |
| [pyGenomeTracks](https://github.com/deeptools/pyGenomeTracks) | `3.9` | GPL-3.0-or-later | Fidel Ramirez; Bjoern Gruening; deepTools contributors | genome track figures in `isoquantViewer.py` | [pygenometracks.txt](licence-texts-isoquant.md#lic-iq-pygenometracks) |
| [glue](https://github.com/tidyverse/glue) | not pinned | MIT | glue authors; Posit Software, PBC | string interpolation in `adapter_isoquantviewer.R` | [r-glue.txt](licence-texts-isoquant.md#lic-iq-r-glue) |
| [here](https://github.com/r-lib/here) | not pinned | MIT | here authors | path resolution in `adapter_isoquantviewer.R` | [r-here.txt](licence-texts-isoquant.md#lic-iq-r-here) |
| [logger](https://github.com/daroczig/logger) | not pinned | MIT | logger authors | logging in `adapter_isoquantviewer.R` | [r-logger.txt](licence-texts-isoquant.md#lic-iq-r-logger) |

## 7. First-party software

The Snakemake workflow (`workflow/Snakefile`, `workflow/rules/run_isoquant.smk`), the
scripts in `workflow/scripts/` (`modify_bam.py`, `collapse_annotation.py`,
`make_mudata.py`, `assess_variant_support.py`, `annotate_bam.py`, `bc_banner.py`), the
`BaseCodeIsoQuant` launcher and the utilities in `utilities/` are Basic Genomics AB's own
software and require no third-party notice.

The BaseCode additions inside the IsoQuant engine are the exception: as modifications to a
GPL-2.0 work they are covered by §1, not by this section.

## 8. Scope

This document was generated against the pipeline repository at version 1.4.2 with the
IsoQuant submodule pinned at `3.13.0.bg`. Version columns give the requirement declared in
the repository, which is what the container build resolves; where a requirement is a
lower bound (`>=`) the installed version may be newer.

It covers the Python libraries declared for the pipeline and for the IsoQuant engine, the
external tools invoked from Snakemake `shell:` directives, the Python runtime, and the
optional IsoQuant Viewer environment.

It does **not** cover packages contributed by the base image, which the base
distribution documents through its own licence and source infrastructure.
