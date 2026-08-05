# BAM file tags
## Tag reference
The processed data BAM file contains the following tags:

| Tag | Type    | Description                        |
|-----|---------|------------------------------------|
| `SM` | String | Sample name                        |
| `XT` | String | Gene name or ID                    |
| `NR` | Integer| Number of reads used to stitch     |
| `ER` | Integer| Number of reads covering an exon   |
| `IR` | Integer| Number of reads covering an intron |
| `FC` | Integer| Number of 5' reads                 |
| `IC` | Integer| Number of internal reads           |
| `TC` | Integer| Number of 3' reads                 |

Practical recipes that use these tags, such as splitting a BAM by sample and inspecting tags
in IGV, are in the vignette [Working with BAM tags](vignette-bam-tags.md).
