# Suitability Functions

These functions extract weather variables from NAM and GFS data and display the impact of these on various activities based on thresholds which can be set by the user within the function.

![Image of repository-template](SuitRaster.png)

## Sections

* [Military Aspects Of Weather functions](#military-aspects-of-weather)


## Military Aspects Of Weather functions

<description>
<link to template>

* DeriveHeatIndex.rft.xml
	* Displays Heat Index given variables for temperature and relative humidity.
* DeriveWindChill_non_uv.rft.xml
	* Displays Windchill given a temperature variable and wind speed as a single variable not as u and v components.
* DeriveWindChill_uv.rft.xml
	* Displays Windchill given a temperature variable and wind speed in u and v component format.
* ExtractCloudCeiling.rft.xml
	* Displays Cloud Ceiling extracted from a specific variable.
* ExtractCloudCover.rft.xml
	* Displays Cloud Cover as a percentage extracted from a specific variable.
* ExtractGust.rft.xml
	* Displays wind gust extracted from a specific variable.
* ExtractPrecipitationRate.rft.xml
	* Displays Precipitation Rate extracted from specific variable.
* ExtractRelativeHumidity.rft.xml
	* Displays Relative Humidity extracted from a suitable variable.
* ExtractTemperature.rft.xml
	* Displays Temperature extracted from a suitable variable.
* ExtractVisibility.rft.xml
	* Displays Visibility extracted from a suitable variable.
* ExtractWindDirection.rft.xml
	* Displays wind direction given wind data in u and v format.
* ExtractWindSpeed.rft.xml
	* Displays wind speed given wind data in u and v format.
* OpImpact_Air_Defence_Cloud_Ceiling.rft.xml
	* Displays the operational impact of the cloud ceiling on Air Defence
* OpImpact_Air_Defence_Temperature.rft.xml
	* Displays the operational impact of the temperature on Air Defence
* OpImpact_Air_Defence_Visibility.rft.xml
	* Displays the operational impact of visibility on Air Defence
* OpImpact_Air_Defence_Wind_Speed.rft.xml
	* Displays the operational impact of wind speed on Air Defence
* OpImpact_Artillery_Cloud_Ceiling.rft.xml
	* Impact of cloud ceiling on Artillery operations.
* OpImpact_Artillery_Visibility.rft.xml
	* Displays operational impact of visibility on Artillery operations.
* OpImpact_Artillery_Wind_Speed.rft.xml
	* Displays operational impact of windspeed derived from u and v componenets of wind on Artillery operations.
* OpImpact_Bridge_Crossing_Wind_Speed.rft.xml
	* Diplsays operational impact of windspeed derived from u and v componenets of wind on bridge crossings.
* OpImpact_Cross_Country_Manoeuveres_CloudCeiling.rft.xml
	* Displays impact of cloud ceiling on cross country manoeuvres.
* OpImpact_Cross_Country_Manoeuvres_Snow_Depth.rft.xml
	* Displays impact of Snow Depth on cross country manoeuvres.
* OpImpact_Cross_Country_Manoeuvres_Temperature.rft.xml
	* Displays the impact of temperature on cross country manoeuvres.
* OpImpact_Cross_Country_Manoeuvres_Visibility.rft.xml
	* Displays operational impact of visibility on cross country manoeuvres.
* OpImpact_Cross_Country_Manoeuvres_Wind_Speed.rft.xml
	* Displays the impact on cross country manoeuvres of wind speed based on u and v components of wind.
* OpImpact_Parachute_CloudCeiling.rft.xml
	* Displays impact of cloud ceiling on parachute operations.
* OpImpact_Parachute_WindSpeed.rft.xml
	* Displays impact of wind speed derived from u and v components on parachute operations
* OpImpact_Personnel_Heat_Index.rft.xml
	* Display impact of heat index on personnel.
* OpImpact_Personnel_Temp.rft.xml
	* Operation impact of temperature on personnel.
* OpImpact_UAV_Cloud_Ceiling.rft.xml
	* Displays impact of cloud cover on Unmanned Aerial Vehicles (UAVs)
* OpImpact_UAV_Visibility.rft.xml
	* Displays impact of Visibility on Unmanned Aerial Vehicles (UAVs)
* OpImpact_UAV_Wind_Speed.rft.xml
	* Displays the impact of windspeed derived from u and v components of wind on Unmanned Aerial Vehicles (UAVs).
* Tactical_Airlift_Cloud_Ceiling.rft.xml
	* Displays impact of cloud ceiling on Tactical Airlift operations.
* Tactical_Airlift_Visibility.rft.xml
	* Displays the impact of visibility on Tactical Airlift operations.


## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

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

[](Esri Tags: ArcGIS Defense and Intelligence Military Environment Planning Analysis Emergency Management ArcGISSolutions)
[](Esri Language: XML, Python)