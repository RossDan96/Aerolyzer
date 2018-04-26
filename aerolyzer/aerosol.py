import wavelength
import math
import scipy.stats as stats
import retrieve_image_data

class AeroData(object):

    def __init__(self):
        pass

    def aerolyzeImage(self, pathname):
        imager = retrieve_image_data.RtrvData(pathname)
        return self.readHazeLayer(imager.get_hsv(pathname))

    def scoreSize(self,target,minS,maxS):
           rangeS = (maxS - minS)
           median = minS + (rangeS/2)
           stddev = rangeS/3
           zscore = math.fabs((target - median)/stddev)
           pscore = stats.norm.sf(zscore)
           zscore2 = math.fabs(((target/10) - median)/stddev)
           pscore2 = stats.norm.sf(zscore2)
           prob = math.fabs(pscore - pscore2)
           return prob

    def analyzeWavelength(self, wavelength):
           aerosolList = []
           aerosolOut = []
           scatter = wavelength/1000
           aerosolList.append(("fog", self.scoreSize(scatter,.1,200), False))
           aerosolList.append(("cloud", self.scoreSize(scatter,2,80), False))
           aerosolList.append(("cement", self.scoreSize(scatter,3,100), True))
           aerosolList.append(("seasalt", self.scoreSize(scatter,.02,.5), False))
           aerosolList.append(("coal", self.scoreSize(scatter,1,100), True))
           aerosolList.append(("oilsmoke", self.scoreSize(scatter,.025,1), True))
           aerosolList.append(("machining", self.scoreSize(scatter,.1,80), True))
           aerosolList.append(("tobacco", self.scoreSize(scatter,.08,1.4), True))
           aerosolList.append(("diesel", self.scoreSize(scatter,.02,.1), True))
           aerosolList.append(("nuclei", self.scoreSize(scatter,.007,.03), False))
           aerosolList.append(("dust", self.scoreSize(scatter,.05,1000), False))
           aerosolList.append(("biomass", self.scoreSize(scatter,.001,1), True))
           #aerosolOut = sorted(aerosolList, key=lambda aerosol: aerosol[1], reverse = True)
           return aerosolList

    def readHazeLayer(self, pixArray):
            numtypes = 12
            #cumulative = list(map(lambda x : analyzeWavelength(wavelength.get_wavelength(x,1)), pixArray))
            cumulative = []
            wave = wavelength.Wavelength()
            for i in pixArray:
                    cumulative.append(self.analyzeWavelength(wave.get_wavelength(i,1)))
            aerosolSum = reduce((lambda x, y: [(x[0][0],x[0][1] + y[0][1], x[0][2]),(x[1][0],x[1][1] + y[1][1], x[1][2]),(x[2][0],x[2][1] + y[2][1], x[2][2]),(x[3][0],x[3][1] + y[3][1], x[3][2]),(x[4][0],x[4][1] + y[4][1], x[4][2]),(x[5][0],x[5][1] + y[5][1], x[5][2]),(x[6][0],x[6][1] + y[6][1], x[6][2]),(x[7][0],x[7][1] + y[7][1], x[7][2]),(x[8][0],x[8][1] + y[8][1], x[8][2]),(x[9][0],x[9][1] + y[9][1], x[9][2]),(x[10][0],x[10][1] + y[10][1], x[10][2]),(x[11][0],x[11][1] + y[11][1], x[11][2])]), cumulative)
            aerosolSum = sorted(aerosolSum, key=lambda aerosol: aerosol[1], reverse = True)
            return aerosolSum
