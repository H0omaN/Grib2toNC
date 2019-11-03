import glob
import subprocess
import os




############ Converting MRMS grib2 to Netcdf
inputfolder="/home/ho0man/Data/Mathew_Hurricane/grib2/"
outputfolder="\"/media/ho0man/ADATA HD710 1TB/Data/Mathew_Hurricane/NC/\""
files=os.listdir(inputfolder)
files.sort()
inputfiles=glob.glob(inputfolder+"*.grib2")
inputfiles.sort() 
i=0
for file in inputfiles:
    Script0='wgrib2 '+file+' -netcdf '+ outputfolder+files[i][:-6]+'.nc'
    newncfile=outputfolder+files[i][:-6]+'.nc'
    Script1='nccopy -d5 '+newncfile+' '+newncfile[:-3]+'_double.nc'
    Script2='rm '+newncfile
    subprocess.getstatusoutput(Script0+'\n'+Script1+'\n'+Script2)
    i=i+1
    print(str(i)+" "+file)
    
############ converting ST IV grib to netcdf
#inputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceSTIV/1h/ST4/"
#outputfolder="/srv/ccrc/data60/z5194283/Data/Originaldata/HurricaneFlorenceSTIV/1h/ST4-NC/"
#files=os.listdir(inputfolder)
#files.sort()
##inputfiles=glob.glob(inputfolder+"*.grib2")
##inputfiles.sort() 
#i=0
#for file in files:  
#
#    os.rename(inputfolder+file, inputfolder+file+".grb")
#    Script0="module load ncl/6.4.0"+" \n"
#    Script1="ncl_convert2nc "+file+".grb"+" -i "+inputfolder+" -o "+outputfolder
#    Script=Script0+Script1
#    subprocess.getstatusoutput(Script)
#    i=i+1
#    print(str(i))