# Output

A folder named `results/` contains the output from the pipeline. The table below outlines the relevant files and folders that can be expected after the successful run.

```
├─ BaseCode/
│  ├─ results/
│     ├─ benchmarks/
│     ├─ intermediate/
│     ├─ logs/
│     ├─ metadata/
│     ├─ QC_files/
│     ├─ read_flow_files/
│     ├─ summaries/
│     ├─ {name}_run_report.pdf
│     ├─ {name}.stitched.molecules.sorted.bam
└─    └─ {name}.stitched.molecules.sorted.bam.bai
```

| File/Folder | Description |
|----------------------|-------------|
| benchmarks/ | Folder with run-time and memory usage for different steps of the BaseCode Processing Pipeline. |
| intermediate/ | Folder with intermediate files. |
| logs/ | Folder with logs for different steps of the BaseCode Processing Pipeline. |
| metadata/ | Folder with sample information files. |
| QC_files/ | Folder with quality control files. |
| read_flow_files/ | Folder with read count files for each stage of the BaseCode Processing Pipeline. |
| summaries/ | Folder with summaries from different steps of the BaseCode Processing Pipeline. |
| {name}_run_report.pdf | PDF report summarizing the run. |
| {name}.stitched.molecules.sorted.bam | BAM file containing synthetic long reads. |
| {name}.stitched.molecules.sorted.bam.bai | BAM index file. |
