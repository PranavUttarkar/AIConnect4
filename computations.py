from math import *
from decimal import *

coldFinal1 =float(input('cf: '))
coldInit1= float(input('ci: '))
masscoldFinal1 =float(input('mcf: '))
masscoldInit1= float(input('mci: '))
HotFinal1 = float(input('hf: '))
HotInit1 = 100.0
massHotFinal1 =float(input('mhf: '))
massHotInit1= float(input('mhi: '))
C = 4.184

qCold1 = ((masscoldFinal1-masscoldInit1)*(C)*(coldFinal1-coldInit1))
qHot1 = (-1)*((massHotFinal1-massHotInit1)*(C)*(HotFinal1-HotInit1))
qCal1 = qHot1-qCold1
CalC1 = qCal1/(coldFinal1-coldInit1)
print('#1', "qCold: ", qCold1  ,"qHOT: ", qHot1, "qCal: ", qCal1)

####

coldFinal2 =float(input('cf: '))
coldInit2= float(input('ci: '))
masscoldFinal2 =float(input('mcf: '))
masscoldInit2= float(input('mci: '))
HotFinal2 = float(input('hf: '))
HotInit2 = 100.0
massHotFinal2 =float(input('mhf: '))
massHotInit2= float(input('mhi: '))
C = 4.184

qCold2 = ((masscoldFinal2-masscoldInit2)*(C)*(coldFinal2-coldInit2))
qHot2 = (-1)*((massHotFinal2-massHotInit2)*(C)*(HotFinal2-HotInit2))
qCal2 = qHot2-qCold2
CalC2 = qCal2/(coldFinal2-coldInit2)
print('#2', "qCold: ", qCold2  ,"qHOT: ", qHot2, "qCal: ", qCal2)


####

coldFinal3 =float(input('cf: '))
coldInit3= float(input('ci: '))
masscoldFinal3 =float(input('mcf: '))
masscoldInit3= float(input('mci: '))
HotFinal3 = float(input('hf: '))
HotInit3 = 100.0
massHotFinal3 =float(input('mhf: '))
massHotInit3= float(input('mhi: '))
C = 4.184

qCold3 = ((masscoldFinal3-masscoldInit3)*(C)*(coldFinal3-coldInit3))
qHot3 = (-1)*((massHotFinal3-massHotInit3)*(C)*(HotFinal3-HotInit3))
qCal3 = qHot3-qCold3
CalC3 = qCal3/(coldFinal3-coldInit3)
print('#3', "qCold: ", qCold3  ,"qHOT: ", qHot3, "qCal: ", qCal3)


AvgCal = ((CalC1+CalC2+CalC3)/3)
print(CalC1, CalC2, CalC3, AvgCal)