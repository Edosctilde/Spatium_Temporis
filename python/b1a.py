from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
directionOfEnv = direct
bianco.dir = directionOfEnv
giallo.dir = directionOfEnv
rosso.dir = directionOfEnv
azzurro.dir = directionOfEnv
nero.dir = directionOfEnv

Seqh = seq([giallo, rosso, bianco, azzurro, giallo, nero], [7, 4, 5, 6, 7, 3])
Seql = seq([giallo, bianco, nero, giallo, azzurro, rosso, giallo, rosso], [10, 5, 6, 7, 3, 8, 6, 4])
Seqm = seq([giallo, bianco, giallo, rosso, nero, azzurro], [4, 1, 5, 10, 3, 5])


#inizio partitura
T = 144
dil = 0.7
Seql.play(T, [cRnd, 20, 400], 100, 0.2, df = [cRnd, -100, 100], dt = dil)
Seql.play(T, [cRnd, 2120, 2400], 200, [0.01, 0.02, 0.02, 0.015, 0.05, 0.1, 0, 0], df = [cRnd, -300, 300], dt = dil)
T = 150
Seqm.play(T, [cRnd, 1120, 1400], 300, [0.1, 0.05, 0.1, 0.08, 0.04, 0.06], df = [cRnd, -500, 500], dt = dil)
T = 147
Seqh.play(T, [cRnd, 9200, 10400], 100, 0.05, df = [cRnd, -100, 100], dt = dil)
Seqh.play(T, [cRnd, 420, 900], 50, [0.1, 0.05, 0.03, 0.05, 0.02, 0.05], df = [cRnd, -300, 300], dt = dil)
