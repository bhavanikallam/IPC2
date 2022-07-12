import numpy as np
import statistics
from scipy import stats


def MEAN(number):
    return statistics.mean(number)


def GEOMEAN(number):
    return statistics.geometric_mean(number)


def MEDIAN(number):
    return statistics.median(number)


def STDEVS(number):
    return statistics.stdev(number)


def STDEVP(number):
    return statistics.pstdev(number)


def VARIANCE(number):
    return statistics.variance(number)


def PVARIANCE(number):
    return statistics.pvariance(number)


def NORMALDIST(mean, std):
    return stats.norm(mean, std)


def CHISQUARE(lst):
    return stats.chisquare(lst)



