__author__ = 'foury'
import cv2
import os
import numpy as np
from random import randint
src_folder="test/"
dest_folder="./test/"
anglist=[0,60,120,180,240,300,360]
######functions decalred here
def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[:2])/2)
  print image_center
  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[:2],flags=cv2.INTER_LINEAR)
  return result


def random_assign_color(img,chanl):
    ranum=randint(0,255)
    img[:,:,chanl]=ranum
    return  (img,ranum)


#######


filelist=os.listdir(src_folder)
for file in filelist:
    filepath=src_folder+file
    im=cv2.imread(filepath)
    for ang in anglist:
        imrot=rotateImage(im,ang)
        imname=dest_folder+"_md"+str(ang)+file
        cv2.imwrite(imname,imrot)


filelist=os.listdir(src_folder)
for file in filelist:
    filepath=src_folder+file
    im=cv2.imread(filepath)
    imcolor,rnum=random_assign_color(im,0)

    imname=dest_folder+"_md"+str(rnum)+file
    cv2.imwrite(imname,imcolor)
