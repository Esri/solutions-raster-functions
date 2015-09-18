# Name: Download NOAA data 00 hr

# Description: Downloads the most up to date data from the NOAA site by getting the present date.

# Date Edited: 26/03/2015


#Import modules
import arceditor
import arcpy
import os
import datetime
from datetime import datetime
from datetime import time


#Gets the current directory where the script is sitting so that everything else can work off relative paths.
folder = os.path.dirname(__file__)
topFolder = os.path.dirname(folder)
        
#Names of folders to be added to topFolder generated above
gdb = "Geodatabase"
NetCDFData = "NetCDFdata"
tls = "Tools"

#_____________________________________________________________________________________________________________________________________________

def download00():
    #Import custom toolbox required
    arcpy.ImportToolbox(topFolder + os.sep + tls + "\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange =  topFolder + os.sep + NetCDFData + r"\nam%s1hr00z.nc"
    stringToChange2 = topFolder + os.sep + NetCDFData + r"\nam%s1hr00zWind.nc"
    stringToChange3 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_00z"
    
    stringToInsert = stringDateNow
    
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    stringFinal3 = stringToChange3 % stringToInsert
    filename = "nam%s1hr00z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool for general data
    in_url = stringFinal3
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc;apcpsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #Declare variables to be added into OPeNDAP to NetCDF tool for download of wind data
    in_url2 = stringFinal3
    variable2 = "ugrd10m;vgrd10m"
    out_file2 = stringFinal2
    extent2 = "-126 32 -114 43"
    dimension2 = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url2, variable2, out_file2, extent2, dimension2, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file
    Input_Data2 = out_file2

    Raster_Type = "NetCDF" 

    output = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWData" 
    output2 = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWWind"

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=0", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data2, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

    # mxd = arcpy.mapping.MapDocument(topFolder + os.sep + "\mxd\MAOWTemplate.mxd")
    # arcpy.RefreshTOC()

    # print("Refreshed Map Doc") 

#__________________________________________________________________________________________________________________________________________________

def download06():
    #Import custom toolbox required
    arcpy.ImportToolbox(topFolder + os.sep + tls + "\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = topFolder + os.sep + NetCDFData + r"\nam%s1hr06z.nc"
    stringToChange2 = topFolder + os.sep + NetCDFData + r"\nam%s1hr06zWind.nc"
    stringToChange3 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_06z"
    
    stringToInsert = stringDateNow
    
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    stringFinal3 = stringToChange3 % stringToInsert
    filename = "nam%s1hr06z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool for general data
    in_url = stringFinal3
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc;apcpsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"


    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #Declare variables to be added into OPeNDAP to NetCDF tool for download of wind data
    in_url2 = stringFinal3
    variable2 = "ugrd10m;vgrd10m"
    out_file2 = stringFinal2
    extent2 = "-126 32 -114 43"
    dimension2 = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url2, variable2, out_file2, extent2, dimension2, "BY_VALUE")

    print ("OPeNDAP Tool run")

    
    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file
    Input_Data2 = out_file2

    Raster_Type = "NetCDF" 

    output = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWData" 
    output2 = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWWind"
    
    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=0", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data2, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

	
#________________________________________________________________________________________________________________________________________________

def download12():
    #Import custom toolbox required
    arcpy.ImportToolbox(topFolder + os.sep + tls + "\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = topFolder + os.sep + NetCDFData + r"\nam%s1hr12z.nc"
    stringToChange2 = topFolder + os.sep + NetCDFData + r"\nam%s1hr12zWind.nc"
    stringToChange3 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_12z"
    
    stringToInsert = stringDateNow
    
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    stringFinal3 = stringToChange3 % stringToInsert
    filename = "nam%s1hr12z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool for general data
    in_url = stringFinal3
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc;apcpsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #Declare variables to be added into OPeNDAP to NetCDF tool for download of wind data
    in_url2 = stringFinal3
    variable2 = "ugrd10m;vgrd10m"
    out_file2 = stringFinal2
    extent2 = "-126 32 -114 43"
    dimension2 = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url2, variable2, out_file2, extent2, dimension2, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file
    Input_Data2 = out_file2

    Raster_Type = "NetCDF" 

    output = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWData" 
    output2 = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWWind"

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=0", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data2, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)
#_________________________________________________________________________________________________________________________________________________________________

def download18():
    #Import custom toolbox required
    arcpy.ImportToolbox(topFolder + os.sep + tls + "\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")
    
    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = topFolder + os.sep + NetCDFData + r"\nam%s1hr18z.nc"
    stringToChange2 = topFolder + os.sep + NetCDFData + r"\nam%s1hr18zWind.nc"
    stringToChange3 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_18z"
    
    stringToInsert = stringDateNow
    
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    stringFinal3 = stringToChange3 % stringToInsert
    filename = "nam%s1hr18z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool for general data
    in_url = stringFinal3
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc;apcpsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #Declare variables to be added into OPeNDAP to NetCDF tool for download of wind data
    in_url2 = stringFinal3
    variable2 = "ugrd10m;vgrd10m"
    out_file2 = stringFinal2
    extent2 = "-126 32 -114 43"
    dimension2 = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url2, variable2, out_file2, extent2, dimension2, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file
    Input_Data2 = out_file2

    Raster_Type = "NetCDF" 

    output = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWData" 
    output2 = topFolder + os.sep + gdb + "\MAOWdata.gdb\\MAOWWind"

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=0", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data2, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

#_________________________________________________________________________________________________________________________________________________



now_time = time(int(datetime.utcnow().strftime("%H")), int(datetime.utcnow().strftime("%M")), int(datetime.utcnow().strftime("%S")))
#now_time = time(8,10,45)


if now_time >= time(02,50,00) and now_time < time(8,50,00):
    download00()
    #print "0000 to 0600"
elif now_time >= time(8,50,00) and now_time < time(14,50,00):
    download06()
    #print "0600 to 1200"
elif now_time >= time(14,50,00) and now_time < time(21,00,00):
    download12()
    #print "1200 to 1800"
elif ((now_time >= time(21,00,00) and now_time <= time(23,59,59)) or (now_time >= time(00,00,00) and now_time <= time(02,49,59))):
    download18()
    #print "1800 to 0000"
