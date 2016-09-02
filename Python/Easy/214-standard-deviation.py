# -*- coding: utf-8 -*-
"""
Updated last on Fri Aug 12
/u/CirclingNeptune
"""

import math

sample = raw_input('Enter in numbers: ')
sample = map(int, sample.split())

#find mean
mean = math.fsum(sample) / len(sample)

#find variance
sum = 0
for x in sample:
    sum += (x - mean) ** 2
variance = sum / len(sample)

#find standard deviation
print '{0:.4f}'.format(math.sqrt(variance))