from cost import *
from funz import *
from classi import *

SeqA = seq([nero, azzurro, nero, rosso, nero, rosso], [10, 4, 7, 1.5, 5, 7])#34.5
SeqB = seq([giallo, azzurro, rosso, bianco, giallo, bianco, azzurro], [3, 1, 2.3, 2, 3, 0.7, 4])#16


#inizio partitura
T = 221
setup(reverse, 0.2)
T = SeqA.play(T, [cRnd, 9000, 10000], 100, [cLin, 0.001, 0.008], dt = 23/34.5)
T = SeqB.play(T, [cRnd, 9000, 10000], 100, 0.08, dt = 7.5/16)
SeqA.play(T, [cRnd, 9000, 10000], 120, [cRnd, 0.04, 0.08])
T = SeqB.play(T-5, [cRnd, 7000, 10000], 500, [cRnd, 0.02, 0.04])
SeqA.play(T, [cRnd, 4000, 6000], 120, [cRnd, 0.04, 0.08])

#newsetup
T = 230
setup(reverse, [1, 3, 5, 7, 13])
T = SeqB.play(T, [cRnd, 9000, 10000], 500, [cLin, 0.06, 0.01], df = [cRnd, -200, 200], dt = 2.5)
setup(reverse, [cRnd, 4, 11])
T = SeqA.play(T, [cRnd, 9000, 10000], 120, [cRnd, 0.04, 0.08])
setup(reverse, [cRnd, 0.1, 1.0])
SeqB.play(T, [cRnd, 9000, 10000], 120, [cRnd, 0.01, 0.05], df = [cRnd, -200, 200], dt = 2)
setup(reverse, 11)
SeqA.play(T, [cRnd, 9000, 10000], 500, [cRnd, 0.01, 0.05])

T = 350
T = SeqB.play(T, [cRnd, 9000, 10000], 500, [cRnd, 0.005, 0.02], df = [0, 0, 0, 0, 0, 0, -600], dt = 1.25)
SeqA.play(T, [cRnd, 8200, 8600], [cLin, 500, 50], [cLin, 0.01, 0.001])
#
setup(direct, [cRnd, 0.05, 0.2])
T = 350
T = SeqB.play(T, [cRnd, 9000, 10000], 500, [cRnd, 0.005, 0.02], df = [0, 0, 0, 0, 0, 0, -600], dt = 1.25)
SeqA.play(T, [cRnd, 8200, 8600], [cLin, 500, 50], [cLin, 0.01, 0.001])

