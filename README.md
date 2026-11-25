<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Aggregates tract profiles from many subjects and plots the group mean and standard deviation of FA along each tract (utility for the deprecated tractprofile datatype).**

Reads the CSV tract profiles in each input, collects AD, FA, MD and RD per tract and writes product.json with plots of the mean FA profile and its standard deviation across inputs. Use it for a quick group-level look at tract profiles. It works on the deprecated tractprofile datatype and produces no dataset output, only plots.

Run it on brainlife.io: [https://doi.org/10.25663/bl.app.90](https://doi.org/10.25663/bl.app.90)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `profiles` | `neuro/tractprofile-deprecated` | yes | Tract profile outputs (one per subject), each a directory of per-tract CSV files. |

Runtime: container `brainlife/mcr:neurodebian1604-r2017a`; 1 CPUs.

<!-- brainlife-app:end -->

