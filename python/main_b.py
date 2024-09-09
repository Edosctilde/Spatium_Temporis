from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
directionOfEnv = reverse
bianco.envDirection = directionOfEnv
giallo.envDirection = directionOfEnv
rosso.envDirection = directionOfEnv
azzurro.envDirection = directionOfEnv
nero.envDirection = directionOfEnv

#inzio partitura
T = 0

Seqh = seq([giallo, rosso, bianco, azzurro, giallo, nero], [3, 4, 5, 4, 6, 3])
Seql = seq([giallo, bianco, nero, giallo, azzurro, rosso], [2, 5, 3, 7, 3, 5])

Seqm = seq([giallo, bianco, giallo, rosso, nero, azzurro], [4, 1, 5, 7, 3, 5])

Seqm.play(T, [cRnd, 20, 90], 150, [cLin, 0.2, 0.05], dt = 0.8)

T = 5
dil = 0.6
Seql.play(T, [cRnd, 2120, 2400], 200, [cLin, 0.01, 0.1], dt = dil)

Seqm.play(T, [cRnd, 1120, 1400], 300, [cLin, 0.03, 0.05],  dt = dil)

Seqh.play(T, [cRnd, 9200, 10400], 100, [cLin, 0.02, 0.06], dt = dil)

T = 10
dil = 0.4
Seqh.play(T, [cRnd, 420, 900], 50, [cLin, 0.05, 0.1], dt = dil)
Seql.play(T, [cRnd, 20, 400], 100, 0.2, dt = dil)
