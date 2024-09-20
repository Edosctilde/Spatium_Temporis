from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
setup(direct, [1,4,7,10,6])

Seqh = seq([giallo, rosso, bianco, azzurro, giallo, nero], [7, 4, 5, 6, 7, 3])#32
Seql = seq([giallo, bianco, nero, giallo, azzurro, rosso, giallo, rosso], [10, 5, 6, 7, 3, 8, 6, 4])#49
Seqm = seq([giallo, bianco, giallo, rosso, nero, azzurro], [4, 1, 5, 10, 3, 5])#28

shift = 10
#inizio partitura
T = 144+shift
dil = 1
Seql.play(T, [cRnd, 20, 400], 100, 0.2, df = [cRnd, -100, 100], dt = dil)
Seql.play(T, [cRnd, 2120, 2400], 200, [0.01, 0.02, 0.02, 0.015, 0.05, 0.1, 0, 0], df = [cRnd, -300, 300], dt = dil)
T = 150+shift
Seqm.play(T, [cRnd, 1120, 1400], 300, [0.1, 0.05, 0.1, 0.08, 0.04, 0.06], df = [cRnd, -500, 500], dt = dil)
T = 147+shift
Seqh.play(T, [cRnd, 9200, 10400], 100, 0.05, df = [cRnd, -100, 100], dt = dil)
Seqh.play(T, [cRnd, 420, 900], 50, [0.1, 0.05, 0.03, 0.05, 0.02, 0.05], df = [cRnd, -300, 300], dt = dil)

T = 140

setup(reverse, [10, 14, 7, 3, 4])
Seql.play(T, [cRnd, 100, 400], 150, [cLin, 0.006, 0.1], dt = 0.3)
Seqm.play(T, [cRnd, 1120, 1400], 300, [cLin, 0.006, 0.06], df = [cRnd, -500, 500], dt = 0.5)
Seqh.play(T, [cRnd, 9000, 10300], 150, [cLin, 0.005, 0.08], dt = 0.44)

T = 204
setup(reverse, 1)
Seql.play(T, [cRnd, 100, 400], 150, [cRnd, 0.05, 0.1], dt = 39/49)
setup(reverse, [cRnd, 3, 9])
Seqm.play(T, [cRnd, 1120, 1400], 300, [cRnd, 0.06, 0.1], df = [cRnd, -500, 500], dt = 39/28)
Seqh.play(T, [cRnd, 9000, 10300], 150, [cRnd, 0.05, 0.08], dt = 39/32)


T = 277
setup(reverse, [cRnd, 3, 9])
Seql.play(T, [cRnd, 100, 400], 150, [cLin, 0.05, 0.001], dt = 11/49)
Seqm.play(T, [cRnd, 1120, 1400], 300, [cLin, 0.06, 0.001], df = [cRnd, -500, 500], dt = 15/28)
Seqh.play(T, [cRnd, 9000, 10300], 150, [cLin, 0.08, 0.001], dt = 6/32)

T = 340
setup(reverse, [cRnd, 0.5, 3])
Seql.play(T, [cRnd, 100, 400], 150, [cLin, 0.01, 0.001], dt = 14/49)
Seqm.play(T, [cRnd, 1120, 1400], 300, [cLin, 0.015, 0.001],  dt = 12/28)
Seqh.play(T, [cRnd, 9000, 10300], 150, [cLin, 0.01, 0.001], dt = 16/32)
