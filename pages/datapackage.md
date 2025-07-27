---
layout: profile
title: datapackage.json
permalink: /datapackage/
background: /assets/datapackage.png
toc: true
---

The metadata is critical for describing your dataset and making your record findable. The metadata associated with a GeoLocator DP are expressed in the `datapackage.json` file. It follows exactly the [Data Package](https://datapackage.org/standard/data-package/).

This definition of the metadata map directly Zenodo metadata structure, which follows [DataCite Metadata Schema](https://datacite-metadata-schema.readthedocs.io/). Note that we map datapackage [`contributors`](https://datapackage.org/standard/data-package/#contributors) to [`creator`](https://datacite-metadata-schema.readthedocs.io/en/4.6/properties/creator/) (and not [`contributor`](https://datacite-metadata-schema.readthedocs.io/en/4.6/properties/contributor/)).

In addition, to allow export of a geolocator data package to [Movebank](https://www.movebank.org/), we add some of the specifications from [Movebank Study Attributes]([https://www.movebank.org/cms/movebank-content/studies-page#study_details]).

{:.alert .alert-info style="padding-left: 32px;"}

- Properties indicated with `*` are required.
- Properties indicated with `+` can (and should) be derived/computed directly from the content of the datapackage rather than provided manually.
- The properties are listed by order of priority/importance with computed properties listed at the bottom as usually less relevant for users.
