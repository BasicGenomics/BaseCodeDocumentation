# Configuration builder

Choose your options and the builder writes the `config.yaml` and the matching `docker run`
command for you. Values that differ from the pipeline default are highlighted, and `name` is
kept in step across both pipelines, since they must match for the IsoQuant pipeline to find
the BAM the processing pipeline produced.

<iframe src="../demo/config-builder.html"
        title="Interactive configuration builder for the BaseCode pipelines"
        class="demo-frame builder"></iframe>

Every option is documented in full under
[Input](input.md) for the processing pipeline and
[Input](isoquant-input.md) for the IsoQuant pipeline.
