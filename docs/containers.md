# Container images

Both pipelines are distributed as Docker images from the Basic Genomics organisation on
Docker Hub: [hub.docker.com/u/basicgenomics](https://hub.docker.com/u/basicgenomics).

## Versions

:::{div}
:class: table-centered

| Pipeline | Image | Version | Size |
| --- | --- | --- | --- |
| BaseCode Processing Pipeline | [`basicgenomics/basecode`](https://hub.docker.com/r/basicgenomics/basecode) | [![](https://img.shields.io/docker/v/basicgenomics/basecode?sort=semver&label=%20&color=EB0079)](https://hub.docker.com/r/basicgenomics/basecode/tags) | 1.23 GiB |
| BaseCode IsoQuant Pipeline | [`basicgenomics/basecode_isoquant`](https://hub.docker.com/r/basicgenomics/basecode_isoquant) | [![](https://img.shields.io/docker/v/basicgenomics/basecode_isoquant?sort=semver&label=%20&color=EB0079)](https://hub.docker.com/r/basicgenomics/basecode_isoquant/tags) | 0.66 GiB |
:::

`basicgenomics/basecode:latest` points at the newest release of the BaseCode Processing
Pipeline. To keep a study on one version, pull its version tag instead, for example
`basicgenomics/basecode:1.4.0`.

Running the BaseCode Processing Pipeline container is covered in
[Starting the Pipeline](pipeline.md).

Running the BaseCode IsoQuant Pipeline container is covered in
[Starting the Pipeline](isoquant-pipeline.md).
