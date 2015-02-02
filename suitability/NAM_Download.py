# Name: Download NOAA data 00 hr

# Description: Downloads the most up to date data from the NOAA site by getting the present date.

# Date Edited: 12/01/2015


#Import modules
import arceditor
import arcpy
import datetime
from datetime import datetime
from datetime import time

#_____________________________________________________________________________________________________________________________________________

def download00():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\nam_%s_1hr_00z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_00z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "nam_%s_1hr_00z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    Raster_Type = "NetCDF" 

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning
    output2 = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Wind" # to be set by user at beginning

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=0", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

#__________________________________________________________________________________________________________________________________________________

def download06():
    import arcpy

    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\nam_%s_1hr_06z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_06z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "nam_%s_1hr_06z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    Raster_Type = "NetCDF"

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning
    output2 = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Wind" # to be set by user at beginning

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=1", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

#________________________________________________________________________________________________________________________________________________

def download12():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\nam_%s_1hr_12z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_12z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "nam_%s_1hr_12z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    Raster_Type = "NetCDF"

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning
    output2 = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Wind" # to be set by user at beginning

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=1", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

#_________________________________________________________________________________________________________________________________________________________________

def download18():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print ("Toolbox imported")

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print ("datetime returned")

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\nam_%s_1hr_18z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/nam/nam%s/nam1hr_18z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "nam_%s_1hr_18z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;tcdcclm;tmpsfc;hgtclb;vissfc;ugrd10m;vgrd10m;ugrdmwl;vgrdmwl;snodsfc;gustsfc"
    out_file = stringFinal
    extent = "-126 32 -114 43"
    dimension = "time '2015-01-01 00:00:00' '2015-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print ("OPeNDAP Tool run")

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    Raster_Type = "NetCDF"

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning
    output2 = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Wind" # to be set by user at beginning

    # Process: Remove Rasters From Mosaic Dataset
    arcpy.RemoveRastersFromMosaicDataset_management(output, "OBJECTID >=1", "NO_BOUNDARY", "NO_MARK_OVERVIEW_ITEMS", "NO_DELETE_OVERVIEW_IMAGES", "NO_DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "NO_CELL_SIZES")

    arcpy.RemoveRastersFromMosaicDataset_management(output2, "OBJECTID >= 0", "UPDATE_BOUNDARY", "MARK_OVERVIEW_ITEMS", "DELETE_OVERVIEW_IMAGES", "DELETE_ITEM_CACHE", "REMOVE_MOSAICDATASET_ITEMS", "UPDATE_CELL_SIZES")

    print ("Removed Raster from Mosaic Dataset")

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")
    arcpy.AddRastersToMosaicDataset_management(output2, Raster_Type, Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print ("Rasters added to Mosaic Datasets - "+filename)

#_________________________________________________________________________________________________________________________________________________



now_time = time(int(datetime.utcnow().strftime("%H")), int(datetime.utcnow().strftime("%M")), int(datetime.utcnow().strftime("%S")))
#now_time = time(14,10,45)


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
