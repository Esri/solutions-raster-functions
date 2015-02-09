# solutions-raster-functions

Raster functions can be applied to raster datasets and mosaic datasets for fast, accurate analytic capabilities.

![Raster functions graphic](GenericFunctionsGraphic.png)

## Features

* The [**suitability**](./suitability/README.MD) folder contains:
  * Military Aspects of Weather functions

## Sections

* [Requirements](#requirements)
* [Instructions](#instructions)
* [Resources](#resources)
* [Issues](#issues)
* [Contributing](#contributing)
* [Licensing](#licensing)

## Requirements

* ArcGIS Desktop 10.3
* ArcGIS Pro 1.0 or higher

## Instructions

### General Help

* [New to Github? Get started here.](http://htmlpreview.github.com/?https://github.com/Esri/esri.github.com/blob/master/help/esri-getting-to-know-github.html)
* [Getting started with image and raster processing](http://pro.arcgis.com/en/pro-app/help/data/imagery/get-started-with-image-and-raster-processing.htm)
* [Apply functions to a dataset](http://pro.arcgis.com/en/pro-app/help/data/imagery/apply-functions-to-a-dataset.htm)

### Getting Started

* Download the solutions-raster-functions repo to your local computer.
* These raster functions are designed to be work with mosaic datasets only and only with NAM and GFS data in the OpenDAP format.  If the user wants to use other data formats then the raster functions and associated Python scripts will have to be edited.
* They have been built with NAM CONUS (12KM) and GFS 0.50 Degree both downloaded in the OpenDAP format obtained from here (http://nomads.ncep.noaa.gov/)
* With ArcGIS Desktop 10.3
	* Add the raster functions to the mosaic dataset as processing templates.
	* Add mosaic dataset to project and then apply relevant processing template.
* With ArcGIS Pro:
	* Presently these raster functions do not work within ArcGIS Pro.

## Resources

* [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/community/)

## Issues

Find a bug or want to request a new function?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Copyright 2015 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[license.txt](license.txt) file.

[](Esri Tags: ArcGIS Defense Intelligence Situational Awareness Military)
[](Esri Language: Python)

