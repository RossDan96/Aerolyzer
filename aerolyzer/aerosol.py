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
       print scatter
       aerosolList.append(("fog", scoreSize(scatter,.1,200)))
       aerosolList.append(("cloud", scoreSize(scatter,2,80)))
       aerosolList.append(("cement", scoreSize(scatter,3,100)))
       aerosolList.append(("seasalt", scoreSize(scatter,.02,.5)))
       aerosolList.append(("coal", scoreSize(scatter,1,100)))
       aerosolList.append(("oilsmoke", scoreSize(scatter,.025,1)))
       aerosolList.append(("machining", scoreSize(scatter,.1,80)))
       aerosolList.append(("biomass", scoreSize(scatter,.08,1.4)))
       aerosolList.append(("diesel", scoreSize(scatter,.02,.1)))
       aerosolList.append(("nuclei", scoreSize(scatter,.007,.03)))
       aerosolList.append(("accumulation", scoreSize(scatter,.03,1)))
       aerosolOut = sorted(aerosolList, key=lambda aerosol: aerosol[1], reverse = True)
       return aerosolOut
