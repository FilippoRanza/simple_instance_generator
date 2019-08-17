#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import numpy as np
from scipy.stats import norm

DELTA = 1


def __build_prob__(m, var, vals):
    prob = norm.cdf(vals + DELTA, loc=m, scale=var) - norm.cdf(vals - DELTA, loc=m, scale=var)
    prob /= prob.sum()
    return prob


def make_normal_random_int(mean, variance, begin, end):
    vals = np.arange(begin, end + 1)
    p = __build_prob__(mean, variance, vals)

    def __out__(count=1):
        return np.random.choice(vals, size=count, p=p)

    return __out__
