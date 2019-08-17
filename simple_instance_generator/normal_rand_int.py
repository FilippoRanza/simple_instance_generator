#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import numpy as np
from scipy.stats import norm

DELTA = 1


def __build_prob__(mean, vals):
    prob = norm.cdf(vals + DELTA, loc=mean) - norm.cdf(vals - DELTA, loc=mean)
    prob /= prob.sum()
    return prob


def make_normal_random_int(mean, begin, end):
    vals = np.arange(begin, end + 1)
    p = __build_prob__(mean, vals)

    def __out__(count=1):
        return np.random.choice(vals, size=count, p=p)
    
    return __out__
