# BAM file tags

When `annotate_bam` is `True`, the pipeline writes
`results/isoquant/{name}.annotated.sorted.bam`, the molecules carrying their IsoQuant
assignment in custom tags. This makes it possible to inspect assignments directly in a genome
browser, using the same colour/group/sort-by-tag workflow described in
[Working with BAM tags](vignette-bam-tags.md).

All tags written by the BaseCode Processing Pipeline are preserved, so `SM`, `XT`, `NR`,
`ER`, `IR`, `FC`, `IC` and `TC` remain available. See
[BAM file tags](functions.md) for those. The tags below are added by this pipeline.

## Molecule preparation

Added while adapting the stitched BAM for IsoQuant.

| Tag | Type | Description |
|-----|---------|------------------------------------|
| `CP` | Integer | Complete (full-length) molecule: `1` when both ends were observed (`TC` > 0 and `FC` > 0), otherwise `0`. This is the flag `full_length_only` filters on. |
| `AD` | String | What was adapted for IsoQuant: `gap` (molecule contains an unsequenced inner gap), `polya` (a synthetic poly-A tail was added because the 3′ end was observed), `gap+polya` (both), or `none`. |

## IsoQuant assignment

| Tag | Type | Description |
|-----|---------|------------------------------------|
| `ZA` | String | Assignment type, e.g. `unique`, `unique_minor_difference`, `ambiguous`, `inconsistent`, `inconsistent_non_intronic`, `inconsistent_ambiguous`, `noninformative`, `intergenic`. Set to `no_isoquant_assignment` for molecules IsoQuant did not assign. |
| `ZI` | String | Assigned isoform (transcript) ID. |
| `ZG` | String | Assigned gene ID. |
| `ZE` | String | The events supporting the assignment, comma-separated, for example `extra_intron_novel:14451-181624,alt_donor_site_known:182191-182528`. |
| `ZM` | String | Discovered transcript model the molecule supports, or `no_model` if it supports none. |

:::{note} Multi-isoform assignments
With the default `duplicate_mode: all`, a molecule compatible with several isoforms carries
every one of them, `;`-joined in `ZI` and `ZE`. The two lists are positionally aligned, so
`ZI[i]` corresponds to `ZE[i]` and the events explaining each candidate isoform can be read
off pairwise. `ZA` and `ZG` are `;`-joined only when their values actually differ between
candidates.

Set `duplicate_mode` to `best` or `first` if a single isoform per molecule is preferred.
:::

## Imputed structure

Added when `include_imputed` is `True`. The molecule's CIGAR is rewritten to the exon/intron
structure IsoQuant resolved, so a genome browser displays the reconstructed structure rather
than the raw alignment with its unsequenced gaps. Because that structure no longer corresponds
to the original read sequence base for base, the sequence is replaced entirely by `N` and the
base qualities are flattened to a constant 30. This applies to every rewritten molecule, not
only those whose CIGAR changed.

| Tag | Type | Description |
|-----|---------|------------------------------------|
| `OC` | String | The original CIGAR string, before the rewrite. |
| `IM` | Integer | `1` if the CIGAR was changed by the rewrite, `0` if it was already identical to the imputed structure. |

:::{important} The displayed sequence is not the observed sequence
Every rewritten molecule carries a sequence of `N` and a CIGAR describing imputed structure,
whatever the value of `IM`. Use this BAM for inspecting structure and assignment, not for
anything that depends on base-level sequence. The sequence and alignment as observed remain in
`results/{name}.stitched.molecules.sorted.bam`.
:::
