# BaseCode Processing Pipeline

The <b><span style="color:#583092">BaseCode Processing Pipeline</span></b> will process your RNA BaseCode sequencing data from unmapped reads (FASTQ file format) from a compatible sequencer (i.e. MGI DNBSEQ-G99, MGI DNBSEQ-G400, Illumina NovaSeq X Series) to <b><span style="color:#583092">BaseCode Synthetic Long Reads</span></b> mapped to the reference genome (BAM file format) together with quality control metrics related to overall assay quality.

The final output of the BaseCode Processing Pipeline can be used for further downstream analysis (e.g. [IsoQuant](https://github.com/BasicGenomics/IsoQuant_pipeline); see {doc}`Downstream analysis <downstream>`).