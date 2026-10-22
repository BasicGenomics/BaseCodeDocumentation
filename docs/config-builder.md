# Configuration builder

Choose your options and the builder writes the `config.yaml` and the matching `docker run`
command for the BaseCode Processing Pipeline. Values that differ from the default are
highlighted.

<iframe src="../demo/config-builder.html#basecode"
        title="Interactive configuration builder for the BaseCode Processing Pipeline"
        class="demo-frame builder"></iframe>

Every option is documented in full under [Input](input.md). Keep the `name` you choose here:
the [BaseCode IsoQuant Pipeline](isoquant-config-builder.md) needs the same one to find the BAM
this pipeline produces.
