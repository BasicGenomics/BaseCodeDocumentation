#!/bin/bash
# Keep only end-to-end molecules (TC > 0 and FC > 0) from a stitched BAM
# Usage: bash filter_end_to_end.sh INPUT_BAM [OUTPUT_BAM]

set -euo pipefail

INPUT_BAM=$1
OUTPUT_BAM=${2:-$(basename "$INPUT_BAM" .bam).end_to_end.bam}

mkdir -p "$(dirname "$OUTPUT_BAM")"
samtools view -b -e '[TC]>0 && [FC]>0' -o "$OUTPUT_BAM" "$INPUT_BAM"
samtools index "$OUTPUT_BAM"
echo "Written and indexed: $OUTPUT_BAM"
