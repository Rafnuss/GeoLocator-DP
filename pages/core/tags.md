---
layout: schema
title: tags.csv
permalink: /core/tags/
schema: tags-table-schema
---

`tags.csv` is a [tabular data](https://datapackage.org/standard/glossary/#tabular-data) ressources from a GeoLocator Data Package. As we assumes that a tag is only deployed once on a single species, this table contains informations related to the device, the deployment and the animal equiped. Data collected on the bird which might be changing over time (e.g., `age`) should be provided in the [`observations`](/core/observations) table.

Additional data can be provided by following the [Movebank tag attribute dictionary](https://www.movebank.org/cms/movebank-content/movebank-attribute-dictionary#tag_attributes) and [Movebank deployement attribute dictionary](https://www.movebank.org/cms/movebank-content/movebank-attribute-dictionary#deployment_attributes)
