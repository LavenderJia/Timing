# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:57:54 2018

@author: lavwan
"""

import time, sys
timer = time.perf_counter if sys.platform[:3] == 'win' else time.time()

def total(reps, func, *pargs, **kargs):
    """ 
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Return (best time, last result)
    """
    best = 2 ** 32 #136 years
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best : best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
        (best of reps1 runs of (total reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


