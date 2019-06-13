import glob
import subprocess
import os


inputfolder=""
outputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HuricaneFlorenceMRMS/MRMS-30min-1km/"
files=os.listdir(inputfolder)
files.sort()
inputfiles=glob.glob(inputfolder+"*.grib2")
inputfiles.sort() 
i=0
for file in inputfiles:
    Script='wgrib2 '+file+' -netcdf '+ outputfolder+files[i][:-5]+'.nc'
    subprocess.getstatusoutput(Script)
    i=i+1
    print(str(i))