import wavelength
import math
import scipy.stats as stats

def getVal(aerosol):
       return aerosol[1]

def scoreSize(target,minS,maxS):
       rangeS = (maxS - minS)
       median = minS + (rangeS/2)
       stddev = rangeS/3
       zscore = math.fabs((target - median)/stddev)
       pscore = stats.norm.sf(zscore)
       zscore2 = math.fabs(((target/10) - median)/stddev)
       pscore2 = stats.norm.sf(zscore2)
       prob = math.fabs(pscore - pscore2)
       return prob

def analyzeWavelength(wavelength):
       aerosolList = []
       aerosolOut = []
       scatter = wavelength/1000
       aerosolList.append(("fog", scoreSize(scatter,.1,200), False))
       aerosolList.append(("cloud", scoreSize(scatter,2,80), False))
       aerosolList.append(("cement", scoreSize(scatter,3,100), True))
       aerosolList.append(("seasalt", scoreSize(scatter,.02,.5), False))
       aerosolList.append(("coal", scoreSize(scatter,1,100), True))
       aerosolList.append(("oilsmoke", scoreSize(scatter,.025,1), True))
       aerosolList.append(("machining", scoreSize(scatter,.1,80), True))
       aerosolList.append(("tobacco", scoreSize(scatter,.08,1.4), True))
       aerosolList.append(("diesel", scoreSize(scatter,.02,.1), True))
       aerosolList.append(("nuclei", scoreSize(scatter,.007,.03), False))
       aerosolList.append(("dust", scoreSize(scatter,.05,1000), False))
       aerosolList.append(("biomass", scoreSize(scatter,.001,1), True))
       #aerosolOut = sorted(aerosolList, key=lambda aerosol: aerosol[1], reverse = True)
       return aerosolList

def compileValues(pixela, pixelb, numtypes):
        pixelc = []
        for i in range(numtypes):
                pixelc.append((pixela[i][0],pixela[i][1] + pixelb[i][1], pixela[i][2]))
        return pixelc

def readHazeLayer(pixArray):
        numtypes = 12
        #cumulative = list(map(lambda x : analyzeWavelength(wavelength.get_wavelength(x,1)), pixArray))
        cumulative = []
        for i in pixArray:
                cumulative.append(analyzeWavelength(wavelength.get_wavelength(i,1)))
        aerosolSum = reduce((lambda x, y: [(x[0][0],x[0][1] + y[0][1], x[0][2]),(x[1][0],x[1][1] + y[1][1], x[1][2]),(x[2][0],x[2][1] + y[2][1], x[2][2]),(x[3][0],x[3][1] + y[3][1], x[3][2]),(x[4][0],x[4][1] + y[4][1], x[4][2]),(x[5][0],x[5][1] + y[5][1], x[5][2]),(x[6][0],x[6][1] + y[6][1], x[6][2]),(x[7][0],x[7][1] + y[7][1], x[7][2]),(x[8][0],x[8][1] + y[8][1], x[8][2]),(x[9][0],x[9][1] + y[9][1], x[9][2]),(x[10][0],x[10][1] + y[10][1], x[10][2]),(x[11][0],x[11][1] + y[11][1], x[11][2])]), cumulative)
        aerosolSum = sorted(aerosolSum, key=lambda aerosol: aerosol[1], reverse = True)
        return aerosolSum
