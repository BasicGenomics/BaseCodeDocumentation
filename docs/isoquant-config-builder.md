# Configuration builder

Choose your options and the builder writes the `config.yaml` and the matching `docker run`
command for the BaseCode IsoQuant Pipeline. Values that differ from the default are
highlighted.

<iframe src="../demo/config-builder.html#isoquant"
        title="Interactive configuration builder for the BaseCode IsoQuant Pipeline"
        class="demo-frame builder isoquant"></iframe>

Every option is documented in full under [Input](isoquant-input.md). Set `name` to the name
used by the [BaseCode Processing Pipeline](config-builder.md), otherwise this pipeline cannot
find the BAM it produced.
