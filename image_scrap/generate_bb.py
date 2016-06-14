__author__ = 'foury'
import numpy as np
import csv
f_read=open("/Users/foury/Documents/github/2016_18m/image_scrap/dentcrop/log_copy.csv",'r')

lines=csv.reader(f_read,delimiter=',')
i=0
f_write=open("/Users/foury/Documents/github/2016_18m/image_scrap/dent_crop_cord/"+str(i)+".txt",'wb')
for row in lines:

    sp=" "
    content="crack"+sp+row[2]+sp+row[3]+sp+row[4]+sp+row[5]+sp+"0"+sp+"0"+sp+"0"+sp+"0"+sp+"0"+sp+"0"+sp+"0"+"\n"

    if row[-1].split("_")[0][-1]=='0':
        print row
        f_write=open("/Users/foury/Documents/github/2016_18m/image_scrap/dent_crop_cord/"+row[-1]+".txt",'wb')
        f_write.write(content)

        i=i+1

    else:
        f_write.write(content)



