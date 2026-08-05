# Overview

The <b><span class="brand">BaseCode Processing Pipeline</span></b> will process your RNA BaseCode sequencing data from unmapped reads (FASTQ file format) from a compatible sequencer (i.e. MGI DNBSEQ-G99, MGI DNBSEQ-G400, Illumina NovaSeq X Series) to <b><span class="brand">BaseCode Synthetic Long Reads</span></b> mapped to the reference genome (BAM file format) together with quality control metrics related to overall assay quality.

The final output of the BaseCode Processing Pipeline can be used for further downstream analysis with the [BaseCode IsoQuant Pipeline](isoquant.md).

## Pipeline steps

The diagram below shows the whole run: the seven steps, the file format going in and out of
each, the tool that does the work, and the approximate time and memory each step needs.

Hover over a numbered marker to read what that step does and where it is documented.

The times shown are indicative and scale with the number of samples in the run. For up to
four samples, expect the run to complete within a day.

<div class="hotspots">

![BaseCode Processing Pipeline overview](images/BaseCode_Pipeline_Overview.png)

1. **Process Sample Sheet.** The sample sheet is read together with the input FASTQ files to determine which samples are to be processed, and which sample indexes belong to each of them. See [Input](input.md).
2. **Parse FASTQ.** Every read is examined to determine its compartment (5′, internal or 3′) and its sample of origin. Some trimming is performed at this stage.
3. **Trim FASTQ.** The reads are trimmed further, removing adapter sequences and other undesired sequences. Uses Cutadapt.
4. **Map Reads.** The trimmed reads are aligned to the reference genome with HISAT-3N. The reference comes from the mounted resources folder, see [Input](input.md).
5. **Assign Genes.** Each mapped read is assigned to a gene locus, using featureCounts.
6. **Reconstruct Molecules.** Reads are grouped by their molecule-specific mismatch pattern, which is what identifies the reads that came from the same original molecule. This is the longest and most memory-hungry step of the run.
7. **Stitch Molecules.** The reads belonging to each molecule are combined into a single synthetic long read, producing the output BAM. See [Output](output.md).

</div>