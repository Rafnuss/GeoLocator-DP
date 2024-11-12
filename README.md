# GeoLocator DP

**GeoLocator Data Package** (GeoLocator DP) is a data exchange format for geolocator data. It follows the [Data Package standard](https://datapackage.org/standard/data-package/) for the structuring of the data.

A geolocator data package consists of three sets of data: (1) the metadata of the project, (2) the core resources contianing the main dataset and (3) optional trajectory data generated with the [GeoPressure suite](https://raphaelnussbaumer.com/GeoPressureManual/#the-geopressure-suite).

## 1. Metadata

The description of project and the data is contained in [`datapackage.json`](https://raphaelnussbaumer.com/GeoLocator-DP/datapackage/).

| File                                                                           | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`datapackage.json`](https://raphaelnussbaumer.com/GeoLocator-DP/datapackage/) | List of the project's metadata such as the package's title, licences, contributors etc. as well as a list of the data [`resources`](https://datapackage.org/standard/data-resource/) that make up the package |

## 2. Core Resources

The core GeoLocator DP resources contain of the raw geolocator data. These `resources` can be generated without any analysis of the geolocator data.

| File                                                                                 | Description                                                                                            |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| [`tags.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/tags/)                 | Table of devices used in the study. We assume that a `tag` is only used once on a single animal.       |
| [`measurements.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/measurements/) | Table with the raw measurements of all sensors (e.g., light, pressure, ...) for all tags.              |
| [`observations.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/observations/) | Table with the field observations associated with tags such as equipment, retrieval, or others events. |

## 3. GeoPressureR Resources

The GeoPressureR extensions consists of optional trajectrory data generated through the GeoPressureR workflow anaylsis[](https://raphaelnussbaumer.com/GeoPressureManual/geopressuretemplate-workflow.html).

| File                                                                                          | Description                                                                          |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [`staps.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/staps)                 | Table of the stationary periods of all tags.                                         |
| [`paths.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/paths)                 | Table of the trajectory of all tags, typically most likely path or simulation paths. |
| [`edges.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/edges)                 | Table containing the flight informations of the edges associated with the paths.     |
| [`twilights.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/twilights)         | Table of the twilights estimated from light data for all tags.                       |
| [`pressurepaths.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/pressurepaths) | Table of the pressurepaths                                                           |

## Example

> Nussbaumer, R., Rime, Y., & Osinubi, S. T. (2024). GeoLocator Data Package: South African Woodland Kingfisher [Data set]. _Zenodo_. <https://doi.org/10.5281/zenodo.13829929>

## User guides

- [How to create a GeoLocator Data Package from a GeoPressureTemplate folder?](https://raphaelnussbaumer.com/GeoLocatoR/articles/create-from-geopressuretemplate.html)
- [How to read and use a Data package?](https://raphaelnussbaumer.com/GeoLocatoR/articles/read-and-use-datapackage.html)

## Software

<table>
    <tr>
        <td><img src="https://raphaelnussbaumer.com/GeoLocatoR/logo.png" width="100px"/> </td>
        <td>
        The <a href="https://raphaelnussbaumer.com/GeoLocatoR/">GeoLocatoR</a> R package is designed to handle GeoLocator DP: creating DP, adding resources to DP, writing DP and reading DP. It is essentially an extension of the <a href="https://docs.ropensci.org/frictionless/">frictionlessr</a> package for geolocator data.
        </td>
        </tr>
        <tr>
        <td><img src="https://raphaelnussbaumer.com/GeoPressureR/logo.png" width="100px"/></td>
        <td>
        <a href="https://raphaelnussbaumer.com/GeoPressureR/">GeoPressureR</a> is the main package to analyse geolocator data. Once a Geolocator data package is created, GeoPressureR is our recommended software to read the data into R and analyse the data.
        </td>
    </tr>
</table>
