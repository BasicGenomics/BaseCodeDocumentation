# Third-party notices (IsoViewer)

**IsoViewer**, version 2.4.1, for Linux (x86_64)  
© 2026 Basic Genomics AB. All rights reserved.

This page lists the third-party software components distributed with IsoViewer, together
with their licences. The full, verbatim licence text of each component is reproduced under
[Licence texts (IsoViewer)](licence-texts-isoviewer.md); the Licence file column links to it.
The same list and texts are supplied in the download as `THIRD-PARTY-NOTICES.txt`.

Nothing in this document modifies the licence of any listed component. Each component
remains subject to its own licence terms.

## 1. The Python runtime and its libraries

The program carries its own Python interpreter, so no Python installation is needed. These libraries are part of that interpreter.

| Component | Version | Licence | Copyright holder | Used for | Licence file |
| --- | --- | --- | --- | --- | --- |
| Python | 3.12.14 | PSF-2.0 | Python Software Foundation | the interpreter that runs the program; includes third-party code such as libmpdec, listed in its own licence document | [python-psf.txt](licence-texts-isoviewer.md#lic-iv-python-psf), [python-third-party.txt](licence-texts-isoviewer.md#lic-iv-python-third-party) |
| OpenSSL | 3.6.5 | Apache-2.0 | The OpenSSL Project Authors | hash functions of the Python standard library | [openssl.txt](licence-texts-isoviewer.md#lic-iv-openssl) |
| SQLite | 3.53.4 | Public domain | dedicated to the public domain by its authors | reading the annotation database | [sqlite.txt](licence-texts-isoviewer.md#lic-iv-sqlite) |
| libffi | 3.7.0 | MIT | Anthony Green, Red Hat, Inc. and others | Python's ctypes module | [libffi.txt](licence-texts-isoviewer.md#lic-iv-libffi) |
| Expat | 2.8.5 | MIT | Thai Open Source Software Center Ltd; Clark Cooper; Expat maintainers | Python's XML parser | [expat.txt](licence-texts-isoviewer.md#lic-iv-expat) |
| XZ Utils (liblzma) | 5.8.3 | 0BSD | The XZ Utils authors and contributors | Python's lzma module | [xz.txt](licence-texts-isoviewer.md#lic-iv-xz) |
| bzip2 | 1.0.8 | bzip2-1.0.6 | Julian R Seward | Python's bz2 module | [bzip2.txt](licence-texts-isoviewer.md#lic-iv-bzip2) |
| libuuid (util-linux) | 2.42.4 | BSD-3-Clause | Theodore Ts'o | Python's uuid module | [libuuid.txt](licence-texts-isoviewer.md#lic-iv-libuuid) |

## 2. Python libraries

Compiled into the program together with IsoViewer's own code.

| Component | Version | Licence | Copyright holder | Used for | Licence file |
| --- | --- | --- | --- | --- | --- |
| NumPy | 2.4.1 | BSD-3-Clause (bundled code 0BSD, MIT, Zlib, CC0-1.0) | NumPy Developers | numerical arrays | [numpy.txt](licence-texts-isoviewer.md#lic-iv-numpy) |
| OpenBLAS | 0.3.30 | BSD-3-Clause | The OpenBLAS project | linear algebra, shipped inside NumPy | [numpy.txt](licence-texts-isoviewer.md#lic-iv-numpy) |
| LAPACK | inside OpenBLAS | BSD-3-Clause-Open-MPI | The University of Tennessee and others | linear algebra, shipped inside NumPy | [numpy.txt](licence-texts-isoviewer.md#lic-iv-numpy) |
| GCC runtime library (libgfortran) | from the NumPy wheel | GPL-3.0-or-later WITH GCC-exception-3.1 | Free Software Foundation, Inc. | runtime support for OpenBLAS, shipped inside NumPy | [numpy.txt](licence-texts-isoviewer.md#lic-iv-numpy) |
| libquadmath | from the NumPy wheel | LGPL-2.1-or-later | Free Software Foundation, Inc. | runtime support for OpenBLAS, shipped inside NumPy | [numpy.txt](licence-texts-isoviewer.md#lic-iv-numpy) |
| pandas | 2.3.3 | BSD-3-Clause | AQR Capital Management, LLC; Lambda Foundry, Inc.; PyData Development Team; open source contributors | tables | [pandas.txt](licence-texts-isoviewer.md#lic-iv-pandas) |
| python-dateutil | 2.9.0.post0 | Apache-2.0 AND BSD-3-Clause | Gustavo Niemeyer; Paul Ganssle; dateutil contributors | dates, used by pandas | [python-dateutil.txt](licence-texts-isoviewer.md#lic-iv-python-dateutil) |
| pytz | 2026.5 | MIT | Stuart Bishop | time zones, used by pandas | [pytz.txt](licence-texts-isoviewer.md#lic-iv-pytz) |
| six | 1.17.0 | MIT | Benjamin Peterson | compatibility helpers, used by python-dateutil | [six.txt](licence-texts-isoviewer.md#lic-iv-six) |

## 3. Compiler runtime

IsoViewer is compiled with Nuitka. The compiler adds its runtime library to the program; the Nuitka Runtime Library Exception allows a program built this way to be distributed under terms of its author's choice.

| Component | Version | Licence | Copyright holder | Used for | Licence file |
| --- | --- | --- | --- | --- | --- |
| Nuitka runtime library | 4.3 | AGPL-3.0-or-later WITH Nuitka Runtime Library Exception 1.0 | Kay Hayen | runtime code the compiler links into the program | [nuitka-runtime.txt](licence-texts-isoviewer.md#lic-iv-nuitka-runtime), [nuitka-agpl-3.0.txt](licence-texts-isoviewer.md#lic-iv-nuitka-agpl-3.0) |
| Zstandard | 1.4.7 | BSD-3-Clause | Meta Platforms, Inc. (Facebook) | unpacking the program when it starts | [zstd.txt](licence-texts-isoviewer.md#lic-iv-zstd) |

## 4. In every report

These are written into each HTML report the program builds, so they travel with every report you share. Their copyright notices are kept inside the report.

| Component | Version | Licence | Copyright holder | Used for | Licence file |
| --- | --- | --- | --- | --- | --- |
| plotly.js | 2.35.2 | MIT (bundled code under MIT, BSD-3-Clause, ISC and others) | Plotly, Inc. | charts | [plotly.txt](licence-texts-isoviewer.md#lic-iv-plotly) |
| D3 | 7.9.0 | ISC | Mike Bostock | charts | [d3.txt](licence-texts-isoviewer.md#lic-iv-d3) |
| Mona Sans | – | OFL-1.1 | GitHub, Inc. | typeface | [mona-sans.txt](licence-texts-isoviewer.md#lic-iv-mona-sans) |

## 5. First-party software

IsoViewer's own program code, including the code that displays each report, is Basic
Genomics AB's own software and is covered by the Basic Genomics [licence terms](legal.md#licence-terms).

## 6. Scope

This document was generated from the compiled IsoViewer 2.4.1 program: every library and
package inside it is listed above, and the licence texts are those supplied with the
versions it contains.
