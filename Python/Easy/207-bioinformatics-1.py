# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 11:40:51 2016

/u/CirclingNeptune
"""

origDNA = raw_input('Input DNA')
compDNA = ''

for base in origDNA:
    if base == 'A':
        compDNA += 'T'
    if base == 'T':
        compDNA += 'A'
    if base == 'G':
        compDNA += 'C'
    if base == 'C':
        compDNA += 'G'

print origDNA
print ' '.join(compDNA)