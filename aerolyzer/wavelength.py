import cv2
import numpy as np
import math
        
def comparisonArray(mode):
        img = cv2.imread('/home/aero/Documents/Aerolyzer/Aerolyzer/aerolyzer/images/Spectrum1pixel.png')
        BGRArray = []
        HSVArray = []
        i=0
        if mode==0:
            while i<(img.shape[1]):
                BGRArray.append(img[0,i])
                i+=1
            return BGRArray
        else:
            hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            while i<(hsvimg.shape[1]):
                HSVArray.append(hsvimg[0,i])
                i+=1
            return HSVArray
            
def get_wavelength(abc,mode):
    a_diff=0
    b_diff=0
    c_diff=0
    dist=0
    bestDist=2555
    best=0
    i=0
    min_wavelength = 380
    ValArray = comparisonArray(mode)
    while i < (len(ValArray) - 1):
        a_diff = math.fabs(ValArray[i][0] - abc[0])
        b_diff = math.fabs(ValArray[i][1] - abc[1])
        c_diff = math.fabs(ValArray[i][2] - abc[2])
	if mode==1:
                a_diff = a_diff*6
        dist = math.sqrt((a_diff*a_diff)+(b_diff*b_diff)+(c_diff*c_diff))
        
        if(dist < bestDist):
            best = i
            bestDist = dist
        i+=1
    return best + min_wavelength
