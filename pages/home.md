---
title: GeoLocator DP
background: /assets/home.png
permalink: /
description: Data exchange format for geolocator data
---

{:.alert .alert-primary style="padding-left: 32px;"}
**GeoLocator Data Package** (GeoLocator DP) defines a data exchange format for geolocator data. By using a common structure across projects, GeoLocator DP makes data easier to share, compare, and reuse, ultimately supporting bird migration research, conservation, and public outreach.

<table>
    <tr style="border-top-width: 1px;">
        <td>
            <a href="https://raphaelnussbaumer.com/GeoLocatorExplorer/" target="_blank"><img src="assets/geolocatorexplorer_screenshot.png" width="100%;"/></a>
             Use <b><a href="https://raphaelnussbaumer.com/GeoLocatorExplorer/">GeoLocatorExplorer</a></b> to browse trajectories from all published packages in one place.
        </td>
    </tr>

</table>

## Structure

A GeoLocator Data Package follows the more general [Data Package](https://datapackage.org/) and is organized into three components: (1) the core resources containing raw geolocator data, (2) optional but highly recommended trajectory resources generated with [GeoPressureR](https://raphaelnussbaumer.com/GeoPressureManual/), and (3) a minimal local manifest.

### 1. Core Resources

The core GeoLocator DP resources consist of raw geolocator data and deployment information. These `resources` can be generated without running trajectory analyses.

| File                                                                                 | Description                                                                                           |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [`tags.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/tags/)                 | Table of devices used in the study. We assume that a `tag` is only used once on a single animal.      |
| [`measurements.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/measurements/) | Table with the raw measurements of all sensors (e.g., light, pressure, ...) for all tags.             |
| [`observations.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/core/observations/) | Table with the field observations associated with tags such as equipment, retrieval, or other events. |

### 2. GeoPressureR Resources

The GeoPressureR extension consists of optional trajectory data generated through the [GeoPressureR workflow analysis](https://raphaelnussbaumer.com/GeoPressureManual/geopressuretemplate-workflow.html).

| File                                                                                          | Description                                                                          |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [`staps.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/staps)                 | Table of the stationary periods of all tags.                                         |
| [`paths.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/paths)                 | Table of the trajectory of all tags, typically most likely path or simulation paths. |
| [`edges.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/edges)                 | Table containing the flight information of the edges associated with the paths.      |
| [`twilights.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/twilights)         | Table of the twilights estimated from light data for all tags.                       |
| [`pressurepaths.csv`](https://raphaelnussbaumer.com/GeoLocator-DP/geopressurer/pressurepaths) | Table of pressure-based paths.                                                       |
| `params.json`                                                                                 | JSON parameters used to run the GeoPressureR workflow (optional).                    |

### 3. Local Manifest

Following the [Data Package standard](https://datapackage.org/standard/data-package/), each GeoLocator DP contains a `datapackage.json` file with: (1) a machine-readable index of all data [`resources`](https://datapackage.org/standard/data-resource/), (2) a package-level [`$schema`](https://datapackage.org/standard/data-package/#dollar-schema) pointing to the GeoLocator DP profile version, and (3) an optional `id` set to the Zenodo DOI URL when available. The local manifest stays intentionally minimal, while descriptive metadata are managed in Zenodo and resolved from the Zenodo record on read.

## Zenodo Record and Metadata

GeoLocator data packages are published on [Zenodo](https://zenodo.org/) because it provides:

1. long-term hosting, DOI assignment, and versioned records,
2. a simple and reliable way to manage metadata through web forms,
3. community curation through the [GeoLocator DP Zenodo community](https://zenodo.org/communities/geolocator-dp/).

{:.alert .alert-info style="padding-left: 32px;"}
For practical publishing steps to create and use a GeoLocator data package, see the [GeoLocatoR chapters in the GeoPressureManual](https://raphaelnussbaumer.com/GeoPressureManual/geolocator-intro.html).

## Resources

<table>
    <tr>
        <td>
            <a href="https://raphaelnussbaumer.com/GeoLocatoR/"><img src="assets/logo_geolocator.png" width="100px" alt="GeoLocatoR logo"/></a>
        </td>
        <td>
            The <a href="https://raphaelnussbaumer.com/GeoLocatoR/">GeoLocatoR</a> R package is designed to handle GeoLocator DP: creating a DP, adding resources, writing a DP, and reading a DP. It is essentially an extension of the <a href="https://docs.ropensci.org/frictionless/">frictionless</a> package for geolocator data.
        </td>
    </tr>
    <tr style="border-top-width: 1px;">
        <td>
            <a href="https://raphaelnussbaumer.com/GeoPressureManual/geolocator-intro.html"><img src="assets/cover_geopressuremanual.png" width="100px" alt="GeoPressureManual logo"/></a>
        </td>
        <td>
            The <a href="https://raphaelnussbaumer.com/GeoPressureManual/geolocator-intro.html">Geolocator Manual</a> R book has a dedicated part on the use of the GeoLocator Data Package. This is a great place to start learning more about how to use it with your GeoPressureTemplate project.
        </td>
    </tr>
    <tr>
        <td><a href="https://raphaelnussbaumer.com/GeoPressureR/"><img src="assets/logo_geopressurer.png" width="100px" alt="GeoPressureR logo"/></a></td>
        <td>
            <a href="https://raphaelnussbaumer.com/GeoPressureR/">GeoPressureR</a> is the main package to analyze geolocator data. Once a GeoLocator Data Package is created, GeoPressureR is our recommended software to read the data into R and analyze the data.
        </td>
    </tr>
      <tr style="border-top-width: 1px;">
        <td>
            <a href="https://zenodo.org/communities/geolocator-dp/"><img src="assets/logo.png" width="100px" alt="GeoLocator DP logo"/> </a>
        </td>
        <td>
            You'll be able to find all GeoLocator Data Packages in the <a href="https://zenodo.org/communities/geolocator-dp/">GeoLocator Data Package Zenodo Community</a>. Once you've published your data package, make sure to <a href="https://help.zenodo.org/docs/share/submit-to-community/">submit it to the community</a>.
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://raphaelnussbaumer.com/GeoLocatorExplorer/"><img src="assets/logo_geolocatorexplorer.svg" width="100px" alt="GeoLocatorExplorer logo"/> </a>
        </td>
        <td>
            Explore the most likely trajectories of all existing data packages on a 3D map with <a href="https://raphaelnussbaumer.com/GeoLocatorExplorer/">GeoLocatorExplorer</a>.
        </td>
    </tr>
</table>

## How to Cite

> Nussbaumer, R. (2024). GeoLocator-DP: Data exchange format for multi-sensor geolocator. Zenodo. [10.5281/zenodo.14258411](https://doi.org/10.5281/zenodo.14258411)
