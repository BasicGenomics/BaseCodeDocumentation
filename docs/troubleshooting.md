# Troubleshooting

Common problems and their fixes, by pipeline and tool. If yours is not listed, ask in the
[BaseCode Community](faq.md#is-there-a-community-i-can-join) or
[get in touch](faq.md#how-do-i-get-help-with-my-analysis).

## Both pipelines

| Problem | Cause and fix |
| --- | --- |
| Output files are owned by `root` | The Docker daemon runs as root, so files created inside the container are owned by root. After the run, change ownership with `sudo chown -R user:group results/`. |
| A step failed | Each pipeline writes per-step logs into its `logs/` folder inside `results/`. |

## BaseCode IsoQuant Pipeline

| Problem | Cause and fix |
| --- | --- |
| The run fails immediately because the input BAM is not found | `name` differs between `config/config.yaml` and `config_isoquant/config.yaml`. Set the same `name` in both; see [Why must `name` be the same](faq.md#why-must-name-be-the-same-in-both-configuration-files). |
| A step failed | Besides `results/isoquant/logs/`, the resolved run configuration and component versions are in `results/isoquant/logs/{name}.versions.log`, and the workflow log is in `results/isoquant/.snakemake/log/`. |

## IsoViewer

| Message | Cause and fix |
| --- | --- |
| `Error, couldn't launch child (exec): Permission denied` | The temporary folder does not allow running programs (`/tmp` is mounted `noexec`). Point `TMPDIR` to a folder that does, for example `mkdir -p ~/tmp && TMPDIR=~/tmp isoviewer build .` |
| `Error, couldn't unpack file to target path.: No space left on device` | The temporary folder has less than about 200 MB free. Free some space, or point `TMPDIR` to another folder as above. |
| `cannot execute binary file: Exec format error` | The computer is not a 64-bit Intel or AMD (x86_64) Linux machine. |
| A `GLIBC_2.…` version is `not found` | The Linux version is older than the [requirements](isoviewer-install.md#requirements). |
