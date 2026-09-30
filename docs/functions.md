# BAM file tags
## Tag reference
The processed data BAM file contains the following tags:

| Tag | Type    | Description                        |
|-----|---------|------------------------------------|
| `SM` | String | Sample name                        |
| `XT` | String | Gene name or ID                    |
| `RM` | String | Molecule identifier                |
| `BC` | String | Sample name and the read class the molecule was built from: `{SM}_` for 3′ reads, `{SM}_INT` for internal, `{SM}_FP` for 5′ |
| `NR` | Integer| Number of reads used to stitch     |
| `NF` | Integer| Number of fragments (read pairs) used to stitch |
| `ER` | Integer| Number of reads covering an exon   |
| `IR` | Integer| Number of reads covering an intron |
| `FC` | Integer| Number of 5' reads                 |
| `IC` | Integer| Number of internal reads           |
| `TC` | Integer| Number of 3' reads                 |
| `T1` | String | `Y` if at least one 3' read has the expected orientation, confirming the 3' end, otherwise `N` |
| `F1` | String | `Y` if at least one 5' read has the expected orientation, confirming the 5' end, otherwise `N` |
| `CV` | String | Read depth along the molecule, as `start-end:depth` runs separated by `;`, counted in bases from the molecule's first aligned position |

A molecule counts as end-to-end in the run report when `TC` > 0 and `FC` > 0. `T1` and `F1`
are a stricter, orientation-checked version of the same test.

The BAM also carries `NP`, `NS`, `PC`, `PD`, `SC`, `CC` and `SP`. These are diagnostic and may
change between releases.

Practical recipes that use these tags, such as splitting a BAM by sample and inspecting tags
in IGV, are in the vignette [Working with BAM tags](vignette-bam-tags.md).
