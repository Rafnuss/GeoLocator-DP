---
layout: schema
title: observations.csv
permalink: /core/observations/
background: /assets/observations.png
schema: observations-table-schema
---

`observations.csv` is a [tabular data](https://datapackage.org/standard/glossary/#tabular-data) ressources from a GeoLocator Data Package containing any relevant [events](http://rs.tdwg.org/dwc/terms/Event) (datetime and location) that happened typically on the field and which providing important information for the analysis. These observations must typically include at least the equipment and, if appriate, the retrieval, but also any ringing control or direct sightings for instance.

{:.alert .alert-info}
You can think of `observations` as your log entries in your ringing book.

An observation is described by at least, the `datetime` of the observation, the location (`latitude` and `longitude`), the tag involved `tag_id` and the type of observations `observation_type` (e.g., equipement, retrieval or control). In addition, we require also `age` and `life_stage` (which can be set as unknown `U`).
