#  Input requirements
## Input overview
The BaseCode Processing Pipeline is designed to process RNA BaseCode data. This section details the necessary input files required to run the pipeline.
- FASTQ files (*Required*): BaseCode data is recommended to be sequenced paired-end and the BaseCode Processing Pipeline requires at least two fastq files.
- Sample sheet file (*Required*): The sample sheet contains the information needed to properly process each sequenced sample. 
- Configuration file (*Required*): The configuration file points the pipeline to the required input files and defines other parameters needed to run the pipeline. 
- Genome reference and annotations (*Required*): This set of files are needed to map the sequencing reads to the reference genome and specify genomic intervals for the reconstruction step.

The FASTQ file locations and the sample sheet location are specified in the configuration file, which is placed in the `config/` subfolder and named `config.yaml`. The directory containing the genome reference and annotations is additionally specified by mounting the directory when running the Docker image (see {doc}`Starting the BaseCode Processing Pipeline <pipeline>`).

The proposed directory structure:
```
├─ BaseCode/
│  ├─ config/
│     ├─ config.yaml
│     ├─ SampleSheet.xlsx
│  ├─ fastq/
│  ├─ results/ 	   	    ⟵ Results of BaseCode Processing Pipeline will appear here.
├─ BaseCode_resources/
│  ├─ genome_references/
│     ├─ Homo_sapiens/
│        ├─ reference.fa
│        ├─ genomeref*
│        ├─ geneannotations*
│     ├─ ...
```

### FASTQ files
The BaseCode Processing Pipeline expects FASTQ files obtained directly from a compatible sequencer (i.e. MGI DNBSEQ-G99, MGI DNBSEQ-G400, Illumina NovaSeq X Series) without any preprocessing.

#### MGI sequencers
The MGI family of sequencers output two FASTQ files for each lane, `*_read_1.fq.gz` and `*_read_2.fq.gz`, where the indexing sequences are appended to the end of read 2.

If a sample has been sequenced across multiple lanes of the sequencing run, the FASTQ files should be concatenated before the BaseCode Processing Pipeline is started. The easiest way to achieve this is using cat in the Linux command line:
```
cat L01/*_read_1.fq.gz L02/*_read_1.fq.gz > L01_L02_read_1.fq.gz
cat L01/*_read_2.fq.gz L02/*_read_2.fq.gz > L01_L02_read_2.fq.gz
```
#### Illumina sequencers
Illumina sequencing platforms generate four FASTQ files, paired-end read files, `_R1.fastq.gz` and `_R2.fastq.gz`, and separate index read files, `_I1.fastq.gz` and `_I2.fastq.gz`, containing the indexing sequences. Illumina sequencing data are typically demultiplexed post-run. For downstream processing with the BaseCode Processing Pipeline, FASTQ files should be concatenated before the BaseCode Processing Pipeline is started. The easiest way to achieve this is using cat in the Linux command line:
```
cat *_R1.fq.gz > R1.fq.gz
cat *_R2.fq.gz > R2.fq.gz
cat *_I1.fq.gz > I1.fq.gz
cat *_I2.fq.gz > I2.fq.gz
```

The FASTQ files are recommended to be placed in the `fastq/` subfolder:
```
mkdir BaseCode 
cd BaseCode
mkdir fastq
cp /path/to/fastqs_files fastq/
```
> **NOTE** FASTQ files may be located in any directory, as long as the correct path is provided appropriately in the configuration file when running the Docker container (see {doc}`Starting the BaseCode Processing Pipeline <pipeline>`).

### Sample sheet
The sample sheet is supplied in the form of an Excel Workbook (XLSX) file with information for each sample. The sample sheet contains 5 required columns and 1 optional column. A sample sheet template can be found here: [SampleSheet.xlsx](resources/SampleSheet.xlsx).

The template features a drop-down menu of allowed index primer names for each reaction.

Example sample sheet:
<table>
<thead>
<tr>
<th rowspan="2">SAMPLE_ID</th>
<th colspan="2">PCR A</th>
<th colspan="2">PCR B</th>
<th rowspan="2">DESC</th>
</tr>
<tr>
<th>FW1</th>
<th>RV1</th>
<th>FW1</th>
<th>RV2</th>
</tr>
</thead>
<tbody>
<tr><td>SAMPLE1</td><td>Idx_Fw1_1</td><td>Idx_Rv1_1</td><td>Idx_Fw1_1</td><td>Idx_Rv2_1</td><td>TEST1</td></tr>
<tr><td>SAMPLE2</td><td>Idx_Fw1_2</td><td>Idx_Rv1_1</td><td>Idx_Fw1_2</td><td>Idx_Rv2_1</td><td>TEST2</td></tr>
<tr><td>SAMPLE3</td><td>Idx_Fw1_3</td><td>Idx_Rv1_1</td><td>Idx_Fw1_3</td><td>Idx_Rv2_1</td><td>TEST3</td></tr>
<tr><td>SAMPLE4</td><td>Idx_Fw1_4</td><td>Idx_Rv1_1</td><td>Idx_Fw1_4</td><td>Idx_Rv2_1</td><td>TEST4</td></tr>
<tr><td>SAMPLE5</td><td>Idx_Fw1_5</td><td>Idx_Rv1_1</td><td>Idx_Fw1_5</td><td>Idx_Rv2_1</td><td>TEST5</td></tr>
<tr><td>SAMPLE6</td><td>Idx_Fw1_6</td><td>Idx_Rv1_1</td><td>Idx_Fw1_6</td><td>Idx_Rv2_1</td><td>TEST6</td></tr>
</tbody>
</table>

#### Sample sheet columns
<table>
<thead>
<tr>
<th colspan="2">Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><b>SAMPLE_ID</b></td>
<td>
Sample identification name. May not contain spaces or dashes (-).
Any spaces or dashes will automatically be replaced with underscore (_).
</td>
</tr>
<td rowspan="2"><b>PCR A</b></td>
<td><b>FW1</b></td>
<td>
The first (forward) index primer used for PCR A.<br>
<b>Valid FW1 names:</b><br>
Idx_Fw1_1<br>
Idx_Fw1_2<br>
Idx_Fw1_3<br>
Idx_Fw1_4<br>
Idx_Fw1_5<br>
Idx_Fw1_6
</td>
</tr>
<tr>
<td><b>RV1</b></td>
<td>
The second (reverse) index primer used for PCR A.<br>
<b>Valid RV1 names:</b><br>
Idx_Rv1_1<br>
Idx_Rv1_2<br>
Idx_Rv1_3<br>
Idx_Rv1_4
</td>
</tr>
<tr>
<td rowspan="2"><b>PCR B</b></td>
<td><b>FW1</b></td>
<td>
The first (forward) index primer used for PCR B.<br>
<b>Valid FW1 names:</b><br>
Idx_Fw1_1<br>
Idx_Fw1_2<br>
Idx_Fw1_3<br>
Idx_Fw1_4<br>
Idx_Fw1_5<br>
Idx_Fw1_6
</td>
</tr>
<tr>
<td><b>RV2</b></td>
<td>
The second (reverse) index primer used for PCR B.<br>
<b>Valid RV2 names:</b><br>
Idx_Rv2_1<br>
Idx_Rv2_2<br>
Idx_Rv2_3<br>
Idx_Rv2_4
</td>
</tr>
<tr>
<td colspan="2"><b>DESC</b></td>
<td>Optional sample description.</td>
</tr>
</tbody>
</table>

The sample sheet is recommended to be placed in the `config/` subfolder:
```
mkdir config
cp /path/to/SampleSheet.xlsx config/
```

### Configuration file
The configuration file (`config/config.yaml`) contains all the information needed to run the <b>BaseCode Processing Pipeline</b> and uses the YAML language. The configuration file mainly specifies the name of the processing run, sample sheet used, reference genome, and the FASTQ files used as input. See below for an exhaustive list of possible options.

>**IMPORTANT** The paths specified in the configuration file are relative paths in the Docker container, not the paths on your host machine. The paths on your host machine are specified when running the BaseCode Processing Pipeline (see {doc}`Starting the BaseCode Processing Pipeline <pipeline>`).

Example configuration file (`config.yaml`):
```
name: 'TEST_RUN'
samplesheet: 'config/SampleSheet.xlsx'
reference: 'Homo_sapiens'
r1: 'fastq/read_1.fq.gz'
r2: 'fastq/read_2.fq.gz'
```

#### Configuration file options
In the following description, *Required* means the configuration option must be specified in the config.yaml file. *Optional* means that the configuration option is either not strictly necessary or has a carefully chosen default value which can be overridden by specifying another value in config.yaml.

| Configuration option | Description |
|----------------------|-------------|
| **name** | **Required.** String. Name of the processing run. |
| **samplesheet** | **Required.** String. Path to the sample sheet file. Can either be a CSV or XLSX file. The path is relative to the BaseCode pipeline folder in the Docker image (e.g. `config/SampleSheet.xlsx`). |
| **reference** | **Required.** String. Name of the folder in the specified `.../BaseCode_resources/genome_references/` path containing the required reference and annotation files. |
| **r1** | **Required.** String. Path to the Read 1 FASTQ file. Assumed to be compressed using gzip (`.fq.gz`). The path is relative to the BaseCode pipeline folder in the Docker image (e.g. `fastq/read_1.fq.gz`). |
| **r2** | **Required.** String. Path to the Read 2 FASTQ file. Assumed to be compressed using gzip (`.fq.gz`). The path is relative to the BaseCode pipeline folder in the Docker image (e.g. `fastq/read_2.fq.gz`). |
| **i1** | **Optional.** String. Path to the Index 1 FASTQ file. Commonly generated by Illumina sequencing platforms. If specified, the pipeline assumes all relevant indexing sequences come from `i1` and `i2`. Assumed to be compressed using gzip (`.fq.gz`). The path is relative to the BaseCode pipeline folder (e.g. `fastq/index_1.fq.gz`). |
| **i2** | **Optional.** String. Path to the Index 2 FASTQ file. Commonly generated by Illumina sequencing platforms. If specified, the pipeline assumes all relevant indexing sequences come from `i1` and `i2`. Assumed to be compressed using gzip (`.fq.gz`). The path is relative to the BaseCode pipeline folder (e.g. `fastq/index_2.fq.gz`). |
| **gene_identifier** | **Optional.** String. The gene identifier found in the 9th column of the GFF3 gene annotation files. [**Default:** `gene_name`]. |
| **resource_dir** | **Optional.** String. Path to the resources directory in the Docker image. [**Default:** `/usr/local/app/resources/`]. |
| **index_layout** | **Optional.** String. Specifies which parts of the indexing sequences should be used for sample demultiplexing. Should not be changed unless sequencing was performed with non-standard index sequencing cycles. [**Default:** `16:0-16`]. |
| **umilen** | **Optional.** Integer. Specifies the length of the UMI found in the oligo-dT primer. **Note:** BaseCode Bulk does not contain a UMI. **Default:** `0`. |
| **dtlen** | **Optional.** Integer. Length of the T-stretch found in the oligo-dT primer. [**Default:** `24`]. |
| **dt_cutoff** | **Optional.** Integer. Minimum number of T nucleotide detected in the T-stretch to be considered a 3'-read. [**Default:** `16`]. |
| **ts_sequence** | **Optional.** String. The sequenced part of the template-switching oligo (TSO). Used to identify 5'-reads. [**Default:** `TCTTCTCTCCTCCTCC`]. |
| **ts_pad** | **Optional.** Integer. Number of bases to trim after the detected TSO sequence. [**Default:** `3`]. |
| **ts_cutoff** | **Optional.** Integer. Maximum number of mismatches to the TSO sequence to be considered a 5'-read. [**Default:** `5`]. |
| **params** | **Optional.** Parameters passed to other software used in the pipeline. |
| **params: cutadapt** | **Optional.** String. Parameters used in the trim_fastq step, passed to cutadapt. [**Default:** `-n 2 -m 25 -q 10 -a CTGTCTCTTATACACATCT -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -g TTTTTTTTTTTTTTTTTTTT -g GGAGGAGGAGAGAAGA -g AAAAAAAAAAAAAAAAAAAA -A CTGTCTCTTATACACATCT -A AAAAAAAAAAAAAAAAAAAA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT`]. |
| **params: hisat3n** | **Optional.** String. Parameters used in the map_reads step, passed to hisat-3n. [**Default:** `-k 5 --max-seeds 8 --score-min L,0,-0.5 --base-change G,A --no-temp-splicesite`]. |

The configuration file must be placed in the `config/` subfolder:
```
cp /path/to/config.yaml config/
```


### Genome reference and annotations
The BaseCode Processing Pipeline requires a set of files related to read mapping and gene assignment.
Files needed for read mapping and gene assignment:

| File | Description |
|----------------------|-------------|
| **reference.fa** | Reference genome sequence in FASTA format. |
| **genomeref*** |Pre-built indexes for HISAT-3N. |
| **geneannotations*** | Gene annotations with exon and intron information (GFF3). |


#### Basic Genomics reference storage
For an overview of all reference genomes and annotation files provided by Basic Genomics, please visit: [Basic Genomics Reference Storage](ftp://u473420-sub23@u473420-sub23.your-storagebox.de)

Access credentials:
- **Username:** `u473420-sub23`
- **Server:** `u473420-sub23.your-storagebox.de`
- **Password:** `TBA`

Available reference genomes and annotations:  
- Homo sapiens
- Mus musculus  
- Rattus norvegicus        
- Danio rerio  
- Caenorhabditis elegans
- Drosophila melanogaster  

<img src="images/References.png" width="800">

To use these resources, the downloaded folder must be saved to a folder named `genome_references/`. We recommend calling the parent folder `BaseCode_resources/`. Example installation using the Linux command line:
```
mkdir BaseCode_resources
cd BaseCode_resources
mkdir genome_references
cd genome_references
sftp u473420-sub23@u473420-sub23.your-storagebox.de
cd genome_references
get -r Homo_sapiens
```

You can alternatively access the reference files using any SFTP client (e.g. `Cyberduck`, `FileZilla`).

> **NOTE** The path to the parent folder `.../BaseCode_resources/genome_references/` is specified using Docker when the BaseCode Processing Pipeline is started (see {doc}`Starting the BaseCode Processing Pipeline <pipeline>`), and the name of the folder (e.g. Homo_sapiens) is specified in the configuration file (see [Configuration file](#configuration-file)).

#### Generating custom genome reference and annotations
If your reference genome and annotation files are not provided by Basic Genomics, you can generate them using the [BaseCodeGenerate pipeline](https://github.com/BasicGenomics/BaseCodeGenerate/tree/conda). 

The pipeline prepares all required reference assets for running BaseCode Processing Pipeline with a custom genome reference and annotations. 
To run the BaseCodeGenerate pipeline, the following are required:
- A reference genome sequence in FASTA format. 
- An annotation file in GTF/GFF3 format.

We recommend fetching reference genome and annotation files from either [Ensembl](https://www.ensembl.org/info/data/ftp/index.html) or [GENCODE](https://www.gencodegenes.org/).