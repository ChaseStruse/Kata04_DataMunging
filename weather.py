import csv
import os

currentWorkingDirectory = os.path.dirname(os.path.abspath(__file__))
weatherFile = os.path.join(currentWorkingDirectory, 'weather.dat')

weatherData = []

for line in open(weatherFile):
    weatherData += [line.split()]

days = [weatherData[0] for x in weatherData]

print(weatherData[2][1])

def setMaxTemps(_weatherData):
    _maxTemps = []
    for day in weatherData:
        _maxTemps.append(day[1])
    return(_maxTemps)

maxTemperatures = setMaxTemps(weatherData)

def setLowTemps(_weatherData):
    _lowTemps = []
    for day in weatherData:
        _lowTemps.append(day[2])
    return(_lowTemps)

lowTemperatures = setLowTemps(weatherData)

def findHighestDifferenceBetweenTemperatures(_lowTemps, _highTemps):
    highestDifference = 0
    isString = True
    for temp in range(len(_highTemps)):
        isString = isinstance(_highTemps[temp], str)
        if(highestDifference == 0 and isString == False):
            highestDifference = _highTemps[temp] - _lowTemps[temp]
        elif(highestDifference > 0 and isString == False):
            if(highestDifference < _highTemps[temp] - _lowTemps[temp]):
                highestDifference = _highTemps[temp] - _lowTemps[temp]
        
    return highestDifference

print(findHighestDifferenceBetweenTemperatures(lowTemperatures, maxTemperatures))