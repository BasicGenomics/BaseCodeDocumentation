# Installation

IsoViewer is supplied as a single program for Linux. It carries everything it needs, so
Python, Docker, internet access and administrator rights are not required.

## Download

| Version | File | Size |
| --- | --- | --- |
| 2.4.0 | [isoviewer-2.4.0-linux-x86_64.tar.gz](https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.4.0-linux-x86_64.tar.gz) | 45 MiB |
| 2.3.6 | [isoviewer-2.3.6-linux-x86_64.tar.gz](https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.3.6-linux-x86_64.tar.gz) | 45 MiB |

What changed between versions is listed in the [Changelog](changelog.md#changelog-isoviewer).

## Requirements

- Linux on 64-bit Intel or AMD processors (x86_64), with glibc 2.17 or newer. This includes
  RHEL, Rocky Linux and AlmaLinux 8 and newer, Debian 10 and newer, and Ubuntu 20.04 and newer.
- Memory that grows with the size of the run: about 8 GB for 25 million molecules and 17 GB for
  60 million.
- About 200 MB of free space in the temporary folder (`/tmp`, or the folder set in `TMPDIR`),
  where IsoViewer unpacks itself while it runs.

## Install

Download the program and its checksum, check the download, and unpack it:

```bash
curl -LO https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.4.0-linux-x86_64.tar.gz
curl -LO https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.4.0-linux-x86_64.tar.gz.sha256
sha256sum -c isoviewer-2.4.0-linux-x86_64.tar.gz.sha256
tar -xzf isoviewer-2.4.0-linux-x86_64.tar.gz
cd isoviewer-2.4.0-linux-x86_64
./isoviewer --version
```

The check prints `OK`, and the last command prints `IsoViewer 2.4.0`. The folder also holds
a README, the [licence terms](legal.md#licence-terms) and the
[third-party notices](third-party-isoviewer.md).

To run `isoviewer` from any folder, copy it to a folder on your `PATH`:

```bash
mkdir -p ~/.local/bin && cp isoviewer ~/.local/bin/
```

To update, install the new version the same way. To remove IsoViewer, delete the program and
its cache, `~/.cache/isoviewer/`.
