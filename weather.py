import csv
import os

currentWorkingDirectory = os.path.dirname(os.path.abspath(__file__))
weatherFile = os.path.join(currentWorkingDirectory, 'weather.dat')

weatherData = []

for line in open(weatherFile):
    weatherData += [line.split()]

print(weatherData)
