---
title: GeoLocator DP
background: /assets/home.png
permalink: /
description: Data exchange format for geolocator data
---

**GeoLocator Data Package** (GeoLocator DP) is a data exchange format for geolocator data.

## Core module

The core GeoLocator DP module consists of:

| File                                                                      | Description                                                                                                       |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [`datapackage.json`](datapackage/){:.d-inline-block style="width:150px;"} | Metadata of the project/study.                                                                                    |
| [`tags.csv`](tags/)                                                       | Table of tags/devices/geolocators used in the study. We assume that a `tag` is only used once on a single animal. |
| [`measurements.csv`](measurements/)                                       | Table with the raw measurements of all measurements.                                                              |
| [`observations.csv`](observations/)                                       | Table with any observations associated with tag (e.g. equipment, retrieval, control).                             |

## GeoPressureR Extension

_to be added_

| File                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [`config.yml`](){:.d-inline-block style="width:150px;"} |             |
| [`tag_label.csv`]()                                     |             |
| [`twilight_label.csv`]()                                |             |
| [`stap.csv`]()                                          |             |
| [`stap.csv`]()                                          |             |
| [`path_most_likely.csv`]()                              |             |
| [`path_simulation.csv`]()                               |             |
| [`edge_most_likely.csv`]()                              |             |
| [`edge_simulation.csv`]()                               |             |
| [`map_pressure.geotiff`]()                              |             |
| [`map_light.geotiff`]()                                 |             |
| [`map_marginal.geotiff`]()                              |             |

## Example

_To be added_

## Software

- [GeoPressureR](https://github.com/Rafnuss/GeoPressureR)
- GeoPressureTemple or GeoTemplate?

## Validation

## Inspiration

### camtrap-dp

GeoLocator DP follows closely [camtrap-dp](https://camtrap-dp.tdwg.org/).

### Movebank

GeoLocator Data Package follows a simplified data model inspired from [Movebank data model](https://www.movebank.org/cms/movebank-content/mb-data-model) where:

- A GL `datapackage` corresponds to a Movebank `study`.
- A GL `tag` is equivalent to a Movebank `deployment` as the archival geolocators are generally used once on a single bird. This assumption allows to greatly simplify our data model.
- The GL `measurements` table is more related to the Movebank `observation` which stores the measurements of all measurements or all tags.
- A GL `observation` is not a measurement from the sensor, but some other
