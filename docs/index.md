# Introduction
The <b><span style="color:#583092">BaseCode Processing Pipeline</span></b> will process your RNA BaseCode sample from unmapped reads (FASTQ file format) from a compatible sequencer (i.e. MGI DNBSEQ-G99, MGI DNBSEQ-G400, Illumina NovaSeq X Series) to <b><span style="color:#583092">BaseCode Synthetic Long Reads</span></b> mapped to the reference genome (BAM file format), quality control metrics related to overall assay quality, and BaseCode synthetic long read reconstruction performance.

The final output of the BaseCode Processing Pipeline can be used for further downstream analysis (e.g. IsoQuant or SQUANTI; see {doc}`Downstream analysis <downstream>`).

## <span style="color:#583092">BaseCode Processing Pipeline</span>
The main steps of the BaseCode Processing Pipeline:
1.	Process Sample Sheet
The specified sample sheet is analyzed together with the input FASTQ files to determine which samples are to be processed and their associated sample indexes.
2.	Parse FASTQ
The each read in the input FASTQ file is processed to determine read compartment (3', 5', or internal) and the sample of origin. Some trimming is performed.
3.	Trim FASTQ
The reads in the processed FASTQ file are further trimmed for adapter sequenced and other undesired sequences.
4.	Map Reads
The reads in the trimmed FASTQ file are mapped to the specified reference genome.
5.	Assign Genes
The mapped reads are assigned to a gene locus.
6.	Reconstruct Molecules
The mapped and gene assigned reads are analyzed and grouped based on their molecule-specific mismatch pattern.
7.	Stitch Molecules
Reads corresponding to the same molecules are combined to form a synthetic long read.

<img src="images/BaseCode_Pipeline_Overview.png" width="600">