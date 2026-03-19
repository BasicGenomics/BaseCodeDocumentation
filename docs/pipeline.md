# Starting the BaseCode Processing Pipeline

To start the BaseCode Processing Pipeline, a configuration file must be specified, containing the paths to the FASTQ files, sample sheet, and reference genome. In addition, four directories on the host machine must be mounted into the Docker container. The required mount points are:
- Path to the results folder, which will contain all BaseCode Processing Pipeline output.
- Path to configuration folder, containing the configuration file (and sample sheet).
- Path to the BaseCode resources directory, containing the genome reference and annotations (the folder `genome_references/` must be present).
- Path to the FASTQ files obtained from a sequencer compatible with RNA BaseCode.

The BaseCode Processing Pipeline is then started using docker run. After the BaseCode Processing Pipeline has finished, the ownership of the results folder should be changed to the current user using chown. A guided start-up script is available here: [BaseCodeHelper repository](https://github.com/BasicGenomics/BaseCodeHelper).

Example commands to start the BaseCode Processing Pipeline:
```
mkdir results
docker run –mount type=bind,src=$(pwd)/results/,dst=/usr/local/BaseCode/results/ --mount type=bind,src=$(pwd)/config/,dst=/usr/local/BaseCode/config/ --mount type=bind,src=/path/to/BaseCode_resources/,dst=/usr/local/app/resources/ --mount type=bind,src=$(pwd)/fastq/,dst=/usr/local/BaseCode/fastq/ basicgenomics/basecode:latest
sudo chown -R user:group results/
```

> **NOTE** results/ folder may be located in any directory, but we recommend keeping it within the BaseCode directory.

The directory structure in the Docker image:
```
├─ /usr/
│  ├─ local/
│     ├─ BaseCode/
│        ├─ workflow/
│           ├─ envs/
│           ├─ resources/
│           ├─ rules/
│           ├─ scripts/
│     ├─ app/
└─       ├─ resources/   ⟵ BaseCode_resources is bound to this folder.
```
