from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
setup(direct, 0.4)

Seqh = seq([giallo, rosso, bianco, azzurro, giallo, nero], [7, 4, 5, 6, 7, 3])#32
Seql = seq([giallo, bianco, nero, giallo, azzurro, rosso, giallo, rosso], [10, 5, 6, 7, 3, 8, 6, 4])#49
Seqm = seq([giallo, bianco, giallo, rosso, nero, azzurro], [4, 1, 5, 10, 3, 5])#28

shift = 10
#inizio partitura
T = 144+shift
dil = 1
Seql.play(T, [cRnd, 20, 400], 100, 63, df = [cRnd, -100, 100], dt = dil)
Seql.play(T, [cRnd, 2120, 2400], 200, [53, 56, 56, 55, 54, 53, 0, 0], df = [cRnd, -300, 300], dt = dil)
T = 150+shift
Seqm.airsim(T, [cRnd, 1120, 1400], 300, [63, 60, 63, 62, 61, 62], df = [cRnd, -500, 500], dt = dil)
T = 147+shift
Seqh.airsim(T, [cRnd, 9200, 10400], 100, 57, df = [cRnd, -100, 100], dt = dil)
Seqh.airsim(T, [cRnd, 420, 900], 50, [53, 60, 57, 61, 59, 60], df = [cRnd, -300, 300], dt = dil)

T = 140

setup(reverse, 0.8)
Seql.airsim(T, [cRnd, 100, 400], 150, [cLin, 60, 72], dt = 0.3)
Seqm.airsim(T, [cRnd, 1120, 1400], 300, [cLin, 58, 68], df = [cRnd, -500, 500], dt = 0.5)
Seqh.airsim(T, [cRnd, 9000, 10300], 150, [cLin, 55, 62], dt = 0.44)

#climax
T = 204
setup(reverse, 1)
Seql.airsim(T, [cRnd, 100, 400], 150, [cRnd, 69, 72], dt = 39/49)
Seqm.airsim(T, [cRnd, 1120, 1400], 300, [cRnd, 63, 68], df = [cRnd, -500, 500], dt = 39/28)
Seqh.airsim(T, [cRnd, 9000, 10300], 150, [cRnd, 60, 66], dt = 39/32)

#climax cutter
dur = 2
setup(reverse, [4,3,7,13,9])
T = 244.5-dur
bianco.play(T, dur, 9560, 121, 0.1, where = 160)
rosso.play(T, dur, 1280, 121, 0.1, where = 160)
giallo.play(T, dur, 260, 121, 0.1, where = 160)

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

