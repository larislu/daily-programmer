# -*- coding: utf-8 -*-
"""
Updated last on Sun Aug 07
/u/CirclingNeptune
"""

origDNA = raw_input('Input DNA: ')
midDNA = origDNA[6:len(origDNA) - 5]
codons = ['Met']

aminoAcids = {}
aminoAcids.update(aminoAcids.fromkeys(('G C T ', 'G C C ', 'G C A ', 'G C G '), 
                                       'Ala'))
aminoAcids.update(aminoAcids.fromkeys(('C G T ', 'C G C ', 'C G A ', 'C G G ',
                                       'A G A ', 'A G G '), 'Arg'))
aminoAcids.update(aminoAcids.fromkeys(('A A T ', 'A A C '), 'Asn'))
aminoAcids.update(aminoAcids.fromkeys(('G A T ', 'G A C '), 'Asp'))
aminoAcids.update(aminoAcids.fromkeys(('T G T ', 'T G C '), 'Cys'))
aminoAcids.update(aminoAcids.fromkeys(('C A A ', 'C A G '), 'Gln'))
aminoAcids.update(aminoAcids.fromkeys(('G A A ', 'G A G '), 'Glu'))
aminoAcids.update(aminoAcids.fromkeys(('G G T ', 'G G C ', 'G G A ', 'G G G '), 
                                       'Gly'))
aminoAcids.update(aminoAcids.fromkeys(('C A T ', 'C A C '), 'His'))
aminoAcids.update(aminoAcids.fromkeys(('A T T ', 'A T C ', 'A T A '), 'Ile'))
aminoAcids.update(aminoAcids.fromkeys(('T T A ', 'T T G ', 'C T T ', 'C T C ',
                                       'C T A ', 'C T G '), 'Leu'))
aminoAcids.update(aminoAcids.fromkeys(('A A A ', 'A A G '), 'Lys'))
#skip 'ATG' - Met
aminoAcids.update(aminoAcids.fromkeys(('T T T ', 'T T C '), 'Phe'))
aminoAcids.update(aminoAcids.fromkeys(('C C T ', 'C C C ', 'C C A ', 'C C G '),
                                       'Pro'))
aminoAcids.update(aminoAcids.fromkeys(('T C T ', 'T C C ', 'T C A ', 'T C G ', 
                                       'A G T ', 'A G C '), 'Ser'))
aminoAcids.update(aminoAcids.fromkeys(('A C T ', 'A C C ', 'A C A ', 'A C G '), 
                                       'Thr'))
aminoAcids.update(aminoAcids.fromkeys(('T G G '), 'Trp'))
aminoAcids.update(aminoAcids.fromkeys(('T A T ', 'T A C '), 'Tyr'))
aminoAcids.update(aminoAcids.fromkeys(('G T T ', 'G T C ', 'G T A ', 'G T G '), 
                                       'Val'))
#skip 'TTA, TGA, TAG' - STOP

i = 0
while (i < len(midDNA)):
    dnaSlice = midDNA[i:i + 6]
    codons.append(aminoAcids[dnaSlice])
    i += 6
    
codons.append('STOP')
print origDNA
print ' '.join(codons)