---
title: GeoLocator DP
background: /assets/home.png
permalink: /
description: Data exchange format for geolocator data
---

**GeoLocator Data Package** (GeoLocator DP) is a data exchange format for geolocator data. It follows the [Data Package standard](https://datapackage.org/standard/data-package/) for the structuring of the data.

## Metadata

The main description of the data is contained in [`datapackage.json`](datapackage/). It provides general metadata such as the package's title, licences, contributors etc. as well as a list of the data [`resources`](https://datapackage.org/standard/data-resource/) that make up the package.

| File                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [`datapackage.json`](datapackage/){:.d-inline-block style="width:150px;"} |             |

## Core Resources

The core GeoLocator DP resources contain of the raw geolocator data. These `resources` can be generated without any analysis of the geolocator data.

| File                                                            | Description                                                                                                       |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [`tags.csv`](core/tags/){:.d-inline-block style="width:150px;"} | Table of tags/devices/geolocators used in the study. We assume that a `tag` is only used once on a single animal. |
| [`measurements.csv`](core/measurements/)                        | Table with the raw measurements of all sensors (e.g., light, pressure, ...) for all tags.                         |
| [`observations.csv`](core/observations/)                        | Table with the field observations associated with tags such as equipment, retrieval, or others events             |

## GeoPressureR Resources

| File                                                                       | Description |
| -------------------------------------------------------------------------- | ----------- |
| [`config.yml`](geopressurer/config){:.d-inline-block style="width:150px;"} |             |
| [`twilights.csv`](geopressurer/twilights)                                  |             |
| [`staps.csv`](geopressurer/staps)                                          |             |
| [`paths.csv`](geopressurer/paths)                                          |             |
| [`pressurepaths.csv`](geopressurer/pressurepaths)                          |             |
| [`edges.csv`](geopressurer/edges)                                          |             |
| [`maps.geotiff`](geopressurer/maps)                                        |             |

## Example

_To be added_

## Software

- [GeoPressureR](https://github.com/Rafnuss/GeoPressureR)
- GeoPressureTemple or GeoTemplate?

## Validation
