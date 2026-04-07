# BAM file tags
This guide demonstrates how to sort, filter, and color reads by custom BAM tags present in the BAM file processed with the BaseCode Processing Pipeline.

---

## Tag reference

The processed data BAM file contains the following tags:

| Tag | Type    | Description                        |
|-----|---------|------------------------------------|
| `SM` | String | Sample name                        |
| `BC` | String | Cell barcode                       |
| `XT` | String | Gene name or ID                    |
| `RM` | String | UMI based on pattern               |
| `NR` | Integer| Number of reads used to stitch     |
| `ER` | Integer| Number of reads covering an exon   |
| `IR` | Integer| Number of reads covering an intron |
| `FC` | Integer| Number of 5' reads                 |
| `IC` | Integer| Number of internal reads           |
| `TC` | Integer| Number of 3' reads                 |

---

## Vignette 1: Splitting BAM by sample (`SM` tag)

### Prerequisites

```bash
# Install samtools. We recommend using conda for this:
conda install bioconda::samtools
```

### Script

```bash
#!/bin/bash
# Split a multi-sample BAM into per-sample BAM files

INPUT_BAM=$1

samtools view -h "$INPUT_BAM" | awk '
BEGIN {FS=OFS="\t"}

substr($0,1,1)=="@" {
    headers[++h]=$0
    next
}

# For each read, extract SM tag and pipe to the correct samtools process
{
    sm=""
    for(i=12;i<=NF;i++){
        if($i ~ /^SM:Z:/){
            split($i,a,":")
            sm=a[3]
            break
        }
    }
    if(sm!=""){
        file = sm ".bam"
        if(!(file in pipes)){
            cmd = "samtools view -b -o " file " -"
            pipes[file] = cmd
            for(i=1;i<=h;i++){
                print headers[i] | cmd
            }
        }
        print $0 | pipes[file]
    }
}
END {
    for(f in pipes){
        close(pipes[f])
    }
}'

for f in *.bam; do
    [[ "$f" == "$INPUT_BAM" ]] && continue
    samtools index "$f"
    echo "Written and indexed: $f"
done
```

---

## Vignette 2: IGV — visualizing reads by tag

IGV allows reads to be colored, grouped, and sorted by any BAM tag directly from the GUI. This is useful for visually inspecting assignments, barcodes, or reconstruction results without writing any code.

### Color by tag

Assigns a unique color per unique tag value — useful for distinguishing samples (`SM`) at a glance.

```
1. Load your BAM file in IGV
2. Right-click on the read track
3. Select: Color alignments by → Tag
4. Enter the tag name (e.g. SM)
5. IGV will assign a unique color per unique tag value
```

### Group by tag

Stacks reads into separate rows per tag value — useful for separating samples (`SM`) within the same view.

```
1. Right-click on the read track
2. Select: Group alignments by → Tag
3. Enter the tag name (e.g. SM)
4. Reads will be separated into labeled groups
```

### Sort by tag

Orders reads within the view by tag value — useful for comparing numeric tags like `NR` (number of reads stitched) or `FC` (5' read count).

```
1. Right-click on the read track
2. Select: Sort alignments by → Tag
3. Enter the tag name (e.g. NR, FC)
4. Reads will be reordered by the tag value at the center of the current view
```
