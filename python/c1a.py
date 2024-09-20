from funz import *
from classi import *
from cost import *

setup(reverse, [cRnd, 1, 6])

Seqh = seq([nero, bianco, azzurro, giallo, nero], [3, 4, 1, 3, 4])#15
Seqm = seq([bianco, rosso, giallo, azzurro], [5, 3, 6, 4])#18
Seql = seq([azzurro, nero, azzurro, rosso, giallo], [4, 3, 3, 8, 3])#21

T = 221

Seql.play(T, [cRnd, 200, 1200], 100, [cLin, 0.03, 0.08])
Seqm.play(T+3, [cRnd, 3000, 6000], 300, [cLin, 0.03, 0.08])
Seqh.play(T+6, [cRnd, 10000, 13000], 200, [cLin, 0.03, 0.08])


T = 277

Seql.play(T, [cRnd, 200, 1200], 100, [cLin, 0.08, 0.01])
Seqm.play(T, [cRnd, 3000, 6000], 300, [cLin, 0.08, 0.01])
Seqh.play(T, [cRnd, 10000, 13000], 200, [cLin, 0.08, 0.01])

T = 322
setup(reverse, [cRnd, 6, 13])

Seql.play(T, [cRnd, 200, 1200], 100, [cLin, 0.005, 0.02])
Seqm.play(T+2, [cRnd, 3000, 6000], 300, [cLin, 0.005, 0.02])
Seqh.play(T+4, [cRnd, 10000, 13000], 200, [cLin, 0.005, 0.02])
