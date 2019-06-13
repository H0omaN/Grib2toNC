import glob
import subprocess
import os

############ Converting MRMS grib2 to Netcdf
#inputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceMRMS-6days/PrecipRate/"
#outputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceMRMS-6days/PrecipRate-NC/"
#files=os.listdir(inputfolder)
#files.sort()
#inputfiles=glob.glob(inputfolder+"*.grib2")
#inputfiles.sort() 
#i=0
#for file in inputfiles:
#    Script='wgrib2 '+file+' -netcdf '+ outputfolder+files[i][:-6]+'.nc'
#    subprocess.getstatusoutput(Script)
#    i=i+1
#    print(str(i))
    
########### converting ST IV grib to netcdf
inputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceSTIV/1h/ST4/"
outputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceSTIV/1h/ST4-NC/"
files=os.listdir(inputfolder)
files.sort()
#inputfiles=glob.glob(inputfolder+"*.grib2")
#inputfiles.sort() 
i=0
for file in files:  

    os.rename(inputfolder+file, inputfolder+file+".grb")
    Script0="module load ncl/6.4.0"+" \n"
    Script1="ncl_convert2nc "+file+".grb"+" -i "+inputfolder+" -o "+outputfolder
    Script=Script0+Script1
    subprocess.getstatusoutput(Script)
    i=i+1
    print(str(i))