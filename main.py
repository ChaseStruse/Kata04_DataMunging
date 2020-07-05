import csv
import os
import weather as weather

def getFile(_currentWorkingDirectory, _fileName):
     return(os.path.join(_currentWorkingDirectory, _fileName))

def getDataFromFileIntoAnArray(_file):
    array = []
    for line in open(_file):
        array += [line.split()]
    return array

currentWorkingDirectory = os.path.dirname(os.path.abspath(__file__))

weatherFileName = 'weather.dat'
weatherFile = getFile(currentWorkingDirectory, weatherFileName)
weatherData = getDataFromFileIntoAnArray(weatherFile)
maxTemperatures = weather.setMaxTemps(weatherData)
lowTemperatures = weather.setLowTemps(weatherData)
print(weather.findTheDayWithTheHighestTemperatureDifference(lowTemperatures, maxTemperatures))