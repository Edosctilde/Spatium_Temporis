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

setup(direct, 5)

Seq = seq([azzurro, bianco, giallo], [3,2,1])
Seqb = seq([rosso, nero, bianco], [1,2,3])
#inizio partitura
T = 168.5
durtot = 36
dil = 1.5
n = int(durtot/(6*dil))

for i in range(n):
    Seqb.play(T, [cRnd, 20, 250], 80, 0.05, where = 180, dt = dil)
    T = Seq.play(T, [cRnd, 11000, 12500], 100, 0.05, where = 180, dt = dil)
