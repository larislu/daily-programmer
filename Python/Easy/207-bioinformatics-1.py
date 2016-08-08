# -*- coding: utf-8 -*-
"""
Updated last on Sat Aug 06
/u/CirclingNeptune
"""

origDNA = raw_input('Input DNA: ')

compDNA = origDNA.replace('A', '-')
compDNA = compDNA.replace('T', 'A')
compDNA = compDNA.replace('-', 'T')
compDNA = compDNA.replace('G', '-')
compDNA = compDNA.replace('C', 'G')
compDNA = compDNA.replace('-', 'C')

print origDNA
print compDNA