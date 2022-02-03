import math
import numpy as np


def main():

    print("--------------------------------")
    print("| codedrome.com                |")
    print("| Geometric and Harmonic Means |")
    print("--------------------------------\n")

    housePriceIncreases = getHousePriceIncreases()
    print("House Price Increases\n---------------------")
    print(housePriceIncreases)
    print()

    am = arithmeticMean(housePriceIncreases)
    print("Arithmetic mean (wrong)\n-----------------------")
    print(am)
    print()

    gm = geometricMean(housePriceIncreases)
    print("Geometric mean (correct)\n------------------------")
    print(gm)
    print()

    print("=============================================================\n")

    averageSpeeds = getAverageSpeeds()
    print("Average speeds\n--------------")
    print(averageSpeeds)
    print()

    am = arithmeticMean(averageSpeeds)
    print("Arithmetic mean (wrong)\n-----------------------")
    print(am)
    print()

    hm = harmonicMean(averageSpeeds)
    print("Harmonic mean (correct)\n-----------------------")
    print(hm)
    print()


def getHousePriceIncreases():

    return np.array([1.065, 1.022, 1.015, 1.028, 1.035, 1.048, 1.055, 1.042, 1.044, 1.039], dtype=np.float64)


def getAverageSpeeds():

    return np.array([42, 63, 78, 48, 71, 63, 73, 44, 68, 63, 73, 60], dtype=np.float64)


def arithmeticMean(data):

    mean = np.mean(data)

    return mean


def geometricMean(data):

    if np.any(data <= 0):
        raise ValueError("All values must be positive")

    # Calculate base 10 logarithms of data
    # Can use any base
    logarithms = np.log10(data)

    # Calculate arithmetic mean of logarithms
    logarithms_mean = np.mean(logarithms)

    # Calculate geometric mean
    # Base must be same as that used for
    # calculating logarithms, here 10 is used
    geometric_mean = math.pow(10, logarithms_mean)

    # The calculation has been split into 3 lines
    # for clarity but these can be combined into
    # a single line thus:
    # geometric_mean = math.pow(10, np.mean(np.log10(data)))

    return geometric_mean


def harmonicMean(data):

    if np.any(data <= 0):
        raise ValueError("All values must be positive")

    # Calculate reciprocals of values
    reciprocals = np.power(data, -1)

    # Calculate arithmetic mean of reciprocals
    reciprocals_mean = np.mean(reciprocals)

    # Calculate harmonic mean
    harmonic_mean = math.pow(reciprocals_mean, -1)

    # The calculation has been split into 3 lines
    # for clarity but these can be combined into
    # a single line thus:
    # harmonic_mean = math.pow(np.mean(np.power(data, -1)), -1)

    return harmonic_mean


main()
