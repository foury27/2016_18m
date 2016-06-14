import os
import shutil
src_path="/Users/foury/Documents/github/2016_18m/image_scrap/train/posGt/"
src_path1="/Users/foury/Documents/github/2016_18m/image_scrap/car_dent_Google/"
src_path2="/Users/foury/Documents/github/2016_18m/image_scrap/dentcrop/"
des_path="/Users/foury/Documents/github/2016_18m/image_scrap/train/pos/"
type="dent_"

try:
    for file in os.listdir(src_path2):
        #print file
        new=des_path+type+file[:-4]
        #new=des_path+file[:-4]+".jpg"
        old=src_path1+'pic_'+file[-11:-4]
        print new
        print old
        shutil.copyfile(old,new)
except IOError:
    pass

