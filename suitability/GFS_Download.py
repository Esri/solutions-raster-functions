# Name: Download NOAA data

# Description: Downloads the most up to date data from the NOAA site by getting the present date.

# Date Edited: 13/01/2015


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

    print "Toolbox imported"

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print "datetime returned"

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\gfs_hd_%s_00z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/gfs_0p50/gfs%s/gfs_0p50_00z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "gfs_hd_%s_00z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;pratesfc"
    out_file = stringFinal
    extent = "234 32 246 43"
    dimension = "time '2015-01-01 00:00:00' '2025-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print "OPeNDAP Tool run"

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, "NetCDF", Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print "Rasters added to Mosaic Dataset - "+filename

#__________________________________________________________________________________________________________________________________________________

def download06():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print "Toolbox imported"

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print "datetime returned"

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\gfs_hd_%s_06z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/gfs_0p50/gfs%s/gfs_0p50_06z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "gfs_hd_%s_06z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;pratesfc"
    out_file = stringFinal
    extent = "234 32 246 43"
    dimension = "time '2015-01-01 00:00:00' '2025-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print "OPeNDAP Tool run"

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, "NetCDF", Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print "Rasters added to Mosaic Dataset - "+filename


#________________________________________________________________________________________________________________________________________________

def download12():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print "Toolbox imported"

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print "datetime returned"

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\gfs_hd_%s_12z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/gfs_0p50/gfs%s/gfs_0p50_12z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "gfs_hd_%s_12z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;pratesfc"
    out_file = stringFinal
    extent = "234 32 246 43"
    dimension = "time '2015-01-01 00:00:00' '2025-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print "OPeNDAP Tool run"

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, "NetCDF", Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print "Rasters added to Mosaic Dataset - "+filename


#_________________________________________________________________________________________________________________________________________________

def download18():
    #Import custom toolbox required
    arcpy.ImportToolbox("C:\MAOW_2\Tools\MultidimensionSupplementalTools\Multidimension Supplemental Tools.pyt")

    print "Toolbox imported"

    #Get present date and time
    patternDate = '%Y%m%d'
    patternTime = '%H:%M:%S'
    stringDateNow = datetime.utcnow().strftime(patternDate)
    stringTimeNow = datetime.utcnow().strftime(patternTime)

    print "datetime returned"

    #Insert present date into string for out_file
    stringToChange = r"C:\MAOW_2\NETCDF_data\gfs_hd_%s_18z.nc"
    stringToChange2 = r"http://nomads.ncep.noaa.gov/dods/gfs_0p50/gfs%s/gfs_0p50_18z"
    stringToInsert = stringDateNow
    stringFinal = stringToChange % stringToInsert
    stringFinal2 = stringToChange2 % stringToInsert
    filename = "gfs_hd_%s_18z.nc" % stringToInsert


    #Declare variables to be added into OPeNDAP to NetCDF tool
    in_url = stringFinal2
    variable = "rh2m;pratesfc"
    out_file = stringFinal
    extent = "234 32 246 43"
    dimension = "time '2015-01-01 00:00:00' '2025-12-31 00:00:00'"

    #Run OPeNDAP to NetCDF tool
    arcpy.OPeNDAPtoNetCDF_mds( in_url, variable, out_file, extent, dimension, "BY_VALUE")

    print "OPeNDAP Tool run"

    #____________________________________________________________________________________________________________________________________________


    Input_Data = out_file 

    output = "C:\MAOW_2\Geodatabase\MAOW2_data.gdb\\MAOW2_Data" # to be set by user at beginning

    # Process: Add Rasters To Mosaic Dataset
    arcpy.AddRastersToMosaicDataset_management(output, "NetCDF", Input_Data, "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", "", "0", "1500", "", "*.nc", "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", "", "NO_FORCE_SPATIAL_REFERENCE")

    print "Rasters added to Mosaic Dataset - "+filename

#________________________________________________________________________________________________________________________________________________
    

now_time = time(int(datetime.utcnow().strftime("%H")), int(datetime.utcnow().strftime("%M")), int(datetime.utcnow().strftime("%S")))
#now_time = time(23,34,45)


if now_time >= time(04,50,00) and now_time < time(10,50,00):
    download00()
    #print "0000 to 0600"
elif now_time >= time(10,50,00) and now_time < time(16,50,00):
    download06()
    #print "0600 to 1200"
elif now_time >= time(16,50,00) and now_time < time(23,00,00):
    download12()
    #print "1200 to 1800"
elif ((now_time >= time(23,00,00) and now_time <= time(23,59,59)) or (now_time >= time(00,00,00) and now_time <= time(04,49,59))):
    download18()
    #print "1800 to 0000"