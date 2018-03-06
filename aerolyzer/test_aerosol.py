import cv2
import numpy as np
import aerosol
import time
import math

def test_all():
        testspassed  = 0
        numtests  = 0
        if(test_analyzeWavelength()==1):
                print "test_analyzeWavelength() passed\n"
                testspassed+=1
                numtests+=1
        else:
                numtests+=1
                print "test_analyzeWavelength() failed\n"


        print "Number of Tests passed "+ str(testspassed) +"/"+str(numtests)+"\n"


def test_analyzeWavelength():
        rand = np.random.random() *1000
        wavelength = (rand%400)+300
        print aerosol.analyzeWavelength(wavelength)
        return 1
