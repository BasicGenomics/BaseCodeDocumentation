#!/bin/bash
# Split a multi-sample BAM into per-sample BAM files
# Usage: bash split_bam_by_sample.sh INPUT_BAM

INPUT_BAM=$1

samtools view -h "$INPUT_BAM" | awk '
    BEGIN {FS=OFS="\t"}

    substr($0,1,1)=="@" {
        headers[++h]=$0
        next
    }

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
    [[ "$f" == "$(basename "$INPUT_BAM")" ]] && continue
    samtools index "$f"
    echo "Written and indexed: $f"
done
