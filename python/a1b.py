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



Seq = seq([bianco, rosso, bianco, azzurro, rosso], [3, 4, 0.4, 4, 1.5])
Seq2 = seq([azzurro, bianco, giallo, rosso, nero, azzurro], [2, 1, 1, 1, 1, 1.5])
#inzio partitura
T = 50
#osc(nero, T, 5, 120, 10, [cLin, 0.01, 0.02], 2)
Seq.play(T, [10300, 10500, 10000, 10500, 10200, 10300], 650, 0.01, df = [cRnd, -500, 500], dt = 1)
Seq2.play(T, [13300, 13500, 13000, 13500, 13200, 13300], 150, 0.005, df = [cRnd, -500, 500], dt = 1)
#osc(rosso, T, 15, 80, 10, [cLin, 0.01, 0.02], 3)

modulation = 7
bianco.mod = modulation
giallo.mod = modulation
rosso.mod = modulation
azzurro.mod = modulation
nero.mod = modulation

T = 104
Seq.play(T, [cRnd, 12000, 12500], 800, [cLin, 0.005, 0.13], df = [cRnd, -1000, 1000])
Seq2.play(T, [cRnd, 10000, 10500], 100, 0.005, df = [cRnd, -300, 300])
