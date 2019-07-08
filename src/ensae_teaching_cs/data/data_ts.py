"""
@file
@brief Data about timeseries.
"""
from datetime import datetime, timedelta
import numpy


def generate_sells(duration=730, end=None,
                   week_coef=None, month_coef=None,
                   trend=1.1):
    """
    Generates dummy data and trends and seasonality.
    """
    if week_coef is None:
        week_coef = numpy.array([0.1, 0.12, 0.12, 0.15, 0.20, 0., 0.])
        week_coef[5] = 1. - week_coef.sum()
    if month_coef is None:
        month_coef = [0.8, 1, 1, 1, 1, 1,
                      0.8, 0.6, 1, 1, 1, 1.5]
        month_coef = numpy.array(month_coef)
        month_coef /= month_coef.sum()

    if end is None:
        end = datetime.now()
    begin = end - timedelta(duration)
    day = timedelta(1)

    rows = []
    rnd = (numpy.random.randn(duration + 1) * 0.1) + 1
    exp = (1 + numpy.exp(- numpy.arange(duration + 1) / duration * trend)) ** (-1)
    pos = 0
    while begin <= end:
        month = begin.month
        weekd = begin.weekday()
        value = rnd[pos] * week_coef[weekd] * month_coef[month - 1] * exp[pos]
        pos += 1
        obs = dict(date=begin, value=value)
        rows.append(obs)
        begin += day
    return rows
