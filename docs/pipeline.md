# Starting the Pipeline

To start the BaseCode Processing Pipeline, a configuration file must be specified (see [Input](input.md)), containing the paths to the FASTQ files, sample sheet, and reference genome. In addition, four directories on the host machine must be mounted into the Docker container. The required mount points are:
- Path to the results folder, which will contain all BaseCode Processing Pipeline output.
- Path to configuration folder, containing the configuration file (and sample sheet).
- Path to the BaseCode resources directory, containing the genome reference and annotations (the folder `genome_references/` must be present).
- Path to the FASTQ files obtained from a sequencer compatible with RNA BaseCode.

The pipeline is then started using `docker run`. After it has finished, the ownership of the results folder should be changed to the current user using `chown`. A guided start-up script is available from the [**BaseCodeHelper**](https://github.com/BasicGenomics/BaseCodeHelper) tool.

The [configuration builder](config-builder.md) writes this command for you, with the mount
paths filled in.

Example commands to start the BaseCode Processing Pipeline, run from the `BaseCode/` folder:

```bash
mkdir results
docker run --rm --name TEST_RUN \
    --mount type=bind,src=$(pwd)/results/,dst=/usr/local/BaseCode/results/ \
    --mount type=bind,src=$(pwd)/config/,dst=/usr/local/BaseCode/config/ \
    --mount type=bind,src=/path/to/BaseCode_resources/,dst=/usr/local/app/resources/ \
    --mount type=bind,src=$(pwd)/fastq/,dst=/usr/local/BaseCode/fastq/ \
    basicgenomics/basecode:1.2.6
sudo chown -R user:group results/
```

>**IMPORTANT** The Docker daemon runs as root by default and files created by the Docker container are owned by root. Therefore, the user which runs the BaseCode Processing Pipeline needs root access (either using `sudo` or by knowing the password to the root user) to change file permissions of the final output.

> **NOTE** The `results/` folder can be located in any directory, since it is mounted into the container. This documentation keeps it inside the `BaseCode/` directory so everything for a run sits together.

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
└─       ├─ resources/   ⟵ BaseCode_resources is bound here
```
