#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:40:20 2019

@author: sameerhussain
"""

def arrival(queue, mu, delta_t=1):
    """
    Simulate random arrival of an airplane to a queue
    
    Parameters
    ----------

    queue : list
        List of planes in a queue
    mu : float
        Rate of arrival of  planes (# / hour)
    delta_t : int, float
        Time step in minutes
    
    Returns
    --------
    num : int
        Number of planes  added to a list

        
    Notes
    -----
    Changes to te input queue(list) rely on list mutability; hence, the
    queue isn't ret.
    
    """
    
    from scipy.stats import poisson
    import numpy as np
    r = poisson.rvs(mu / 60, size=delta_t)
    num = np.sum(r)
    
    if num > 0:
        for i in range(num):
            queue.append(0)
    
    return num

def waiting(queue, delta_t):
    for i in range(len(queue)):
        queue[i]+=delta_t
