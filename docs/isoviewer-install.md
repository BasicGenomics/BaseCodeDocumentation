# Installation

IsoViewer is supplied as a single program for Linux. It carries everything it needs, so
Python, Docker, internet access and administrator rights are not required.

## Download

| Version | File | Size |
| --- | --- | --- |
| 2.3.6 | [isoviewer-2.3.6-linux-x86_64.tar.gz](https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.3.6-linux-x86_64.tar.gz) | 45 MiB |

Only the current version can be downloaded; earlier versions are not available.

## Requirements

- Linux on 64-bit Intel or AMD processors (x86_64), with glibc 2.17 or newer. This includes
  RHEL, Rocky Linux and AlmaLinux 8 and newer, Debian 10 and newer, and Ubuntu 20.04 and newer.
- Up to about 8 GB of memory for deeply sequenced runs.
- About 200 MB of free space in the temporary folder (`/tmp`, or the folder set in `TMPDIR`),
  where IsoViewer unpacks itself while it runs.

## Install

Download the program and its checksum, check the download, and unpack it:

```bash
curl -LO https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.3.6-linux-x86_64.tar.gz
curl -LO https://basecode.readthedocs.io/en/latest/downloads/isoviewer-2.3.6-linux-x86_64.tar.gz.sha256
sha256sum -c isoviewer-2.3.6-linux-x86_64.tar.gz.sha256
tar -xzf isoviewer-2.3.6-linux-x86_64.tar.gz
cd isoviewer-2.3.6-linux-x86_64
./isoviewer --version
```

The check prints `OK`, and the last command prints `IsoViewer 2.3.6`. The folder also holds
a README, the [licence terms](legal.md#licence-terms) and the
[third-party notices](third-party-isoviewer.md).

To run `isoviewer` from any folder, copy it to a folder on your `PATH`:

```bash
mkdir -p ~/.local/bin && cp isoviewer ~/.local/bin/
```

To update, install the new version the same way. To remove IsoViewer, delete the program and
its cache, `~/.cache/isoviewer/`.
