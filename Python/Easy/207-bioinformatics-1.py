# -*- coding: utf-8 -*-
"""
Updated last on Sat Aug 06
/u/CirclingNeptune

I originally wrote this using if statements, but then rewrote it using the
replace() function to make the program shorter
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