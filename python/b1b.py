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

Seq = seq([azzurro, bianco, giallo], [3,2,1])
Seqb = seq([rosso, nero, bianco], [1,2,3])
#inizio partitura
T = 153 
durtot = 51
dil = 0.3
n = int(durtot/(6*dil))

for i in range(n):
    T = Seq.play(T, [cRnd, 20, 250], 60, 64, dt = dil)


