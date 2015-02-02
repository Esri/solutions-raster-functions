import numpy as np


class WindchillUV_2():

    def __init__(self):
        self.name = "Wind Chill Function"
        self.description = "This function computes wind chill on the Fahrenheit scale given u/v components of wind and air temperature."


    def getParameterInfo(self):
        return [
            {
                'name': 'tmpsfc',
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "Temperature Raster",
                'description': "A single-band raster where pixel values represent ambient air temperature in Fahrenheit."
            },
            {
                'name': 'u',
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "U component of wind Raster",
                'description': "A single-band raster where pixel values represent the u component of wind in miles per hour."
            },
            {
                'name': 'v',
                'dataType': 'raster',
                'value': None,
                'required': True,
                'displayName': "V component of wind Raster",
                'description': "A single-band raster where pixel values represent the v component of wind in miles per hour."
            },
        ]


    def getConfiguration(self, **scalars):
        return {
          'inheritProperties': 4 | 8,               # inherit all but the pixel type and NoData from the input raster
          'invalidateProperties': 2 | 4 | 8,        # invalidate statistics & histogram on the parent dataset because we modify pixel values.
          'inputMask': False                        # Don't need input raster mask in .updatePixels(). Simply use the inherited NoData.
        }


    def updateRasterInfo(self, **kwargs):
        kwargs['output_info']['bandCount'] = 1      # output is a single band raster
        kwargs['output_info']['pixelType'] = 'f4'
        return kwargs


    def updatePixels(self, tlc, size, props, **pixelBlocks):
        u = np.array(pixelBlocks['u_pixels'], dtype='f4')
        v = np.array(pixelBlocks['v_pixels'], dtype='f4') 
        t = ((((np.array(pixelBlocks['tmpsfc_pixels'], dtype='f4') )-273.15)*1.8000) +32.00)

        ws = (np.sqrt(np.square(u) + np.square(v))*2.23694)
        ws16 = np.power(ws, 0.16)
        outBlock = 35.74 + (0.6215 * t) - (35.75 * ws16) + (0.4275 * t * ws16)
        pixelBlocks['output_pixels'] = outBlock.astype(props['pixelType'])
        return pixelBlocks


    def updateKeyMetadata(self, names, bandIndex, **keyMetadata):
        if bandIndex == -1:
            keyMetadata['datatype'] = 'Scientific'
            keyMetadata['datatype'] = 'Windchill'
        elif bandIndex == 0:
            keyMetadata['wavelengthmin'] = None     # reset inapplicable band-specific key metadata
            keyMetadata['wavelengthmax'] = None
            keyMetadata['bandname'] = 'Windchill'
        return keyMetadata
