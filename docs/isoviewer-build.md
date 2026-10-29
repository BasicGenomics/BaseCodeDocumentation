# Building a report

Go to the `BaseCode/` folder of a run that has been through the
[BaseCode IsoQuant Pipeline](isoquant-pipeline.md), and build:

```bash
cd /path/to/run/BaseCode
isoviewer build .
```

The report is written to the current folder as `{name}_isoviewer_v2.4.1.html`, where
`{name}` is the `name` of the run. To write it somewhere else, add `-o`:

```bash
isoviewer build . -o /path/to/reports/my_run.html
```

Instead of `.`, any path into the run works: the run folder, `BaseCode/`, `results/` or
`results/isoquant/`. IsoViewer only reads the run and changes none of its files.
`isoviewer inspect .` lists the files it would read, without building.

## Consistency checks

Each build ends by cross-checking totals between the IsoQuant outputs, and prints the result,
for example `11/11 reconciliation checks passed`. A failed check is reported but does not stop
the build. Add `--strict` to make IsoViewer exit with an error instead, for use in scripts.

## Cache

The first build reads the annotation database and keeps the result in `~/.cache/isoviewer/`,
so later builds of runs with the same annotation start faster. The cache can be deleted at any
time.

If IsoViewer does not start, see [Troubleshooting](troubleshooting.md#isoviewer).
