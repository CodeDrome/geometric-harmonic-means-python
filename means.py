import math
import numpy as np


def main():

    print("--------------------------------")
    print("| codedrome.com                |")
    print("| Geometric and Harmonic Means |")
    print("--------------------------------\n")

    data = getData()
    print("data\n----")
    print(data)
    print()

    am = arithmeticMean(data)
    print("arithmetic mean\n---------------")
    print(am)
    print()

    gm = geometricMean(data)
    print("geometric mean\n---------------")
    print(gm)
    print()

    hm = harmonicMean(data)
    print("harmonic mean\n---------------")
    print(hm)
    print()


def getData():

    return np.array([828, 163, 465, 199, 647, 363, 711, 348, 142, 665, 972, 718, 93, 176, 474, 924], dtype=np.float64)


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
