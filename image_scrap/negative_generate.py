__author__ = 'foury'
import csv
import cv2
import string

def negtive_sample(image, stepSize, windowSize,x_r,y_r,h,w):
    #sample neg images from four direction close to cropped image
            imp_l=image[x_r-windowSize[0]:x_r,y_r-windowSize[1]:y_r]
            imp_r=image[x_r+w:x_r+w+windowSize[0],y_r+]
            imn="/Users/foury/Documents/github/2016_18m/image_scrap/dent_neg/"+str(x)+"_"+str(y)+"_"+str(x_r)+"_"+str(y_r)+".jpg"
            cv2.imwrite(imn,imp)
            #cv2.imshow("this",imp)
            #cv2.waitKey(10000)


f_read=open("/Users/foury/Documents/github/2016_18m/image_scrap/dentcrop/log_copy.csv",'r')
imdir="/Users/foury/Documents/github/2016_18m/image_scrap/car_dent_Google/"
lines=csv.reader(f_read,delimiter=',')
i=0
for line in lines:
    imname=line[6][-15:-4]
    impath=imdir+imname
    im = cv2.imread(impath)
    #cv2.imshow("this",im)
    #cv2.waitKey(100000)
   negtive_sample(im, 10, [28, 28],int(line[2]),int(line[3]),int(line[4]),int(line[5]))