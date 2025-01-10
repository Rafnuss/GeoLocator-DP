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

- Properties indicated with `*` are required: you'll need to provide a values
- Properties described as **Computed** can (and should) be computed automatically from the content of the datapacakge. Even if required, these values don't need to be provided manually. These are located at the end of the page.
- The properties are listed by order of priority/importance.
