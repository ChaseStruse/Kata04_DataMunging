def setLowTemps(_weatherData):
    _lowTemps = []
    for day in _weatherData:
        _lowTemps.append(day[2])
    return(_lowTemps)

def setMaxTemps(_weatherData):
    _maxTemps = []
    for day in _weatherData:
        _maxTemps.append(day[1])
    return(_maxTemps)

def findTheDayWithTheHighestTemperatureDifference(_lowTemps, _highTemps):
    highestDifference = 0
    highestDifferenceDay = 0
    _lowTemps.pop(0)
    _highTemps.pop(0)

    for temp in range(len(_highTemps)):
        if(highestDifference == 0):
            highestDifference = float(_highTemps[temp]) - float(_lowTemps[temp])
            highestDifferenceDay = 1
        elif(highestDifference > 0):
            if(highestDifference < float(_highTemps[temp]) - float(_lowTemps[temp])):
                highestDifference = float(_highTemps[temp]) - float(_lowTemps[temp])
                highestDifferenceDay = temp + 2 # added 2 due to the pop function removing 1 and then arrays are 0 based 

    return highestDifferenceDay