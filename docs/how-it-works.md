# How it works

RNA BaseCode reconstructs full-length transcripts from ordinary short-read sequencing. The
step that makes this possible is pattern matching: reverse transcription leaves each RNA
molecule with its own signature of mismatches, so reads coming from the same original
molecule can be recognised and stitched back together.

Work through it below.

<iframe src="../demo/reconstruction.html"
        title="Interactive explainer: reconstructing molecules from short reads"
        loading="lazy"
        class="demo-frame"></iframe>

This is what the [BaseCode Processing Pipeline](overview.md) does at the **Reconstruct
Molecules** and **Stitch Molecules** steps, on millions of molecules at once.
