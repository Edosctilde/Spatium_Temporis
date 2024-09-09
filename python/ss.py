from classi import *
from cost import *
from funz import*
#set della direzione dell'inviluppo DIRETTA
directionOfEnv = direct
bianco.envDirection = directionOfEnv
giallo.envDirection = directionOfEnv
rosso.envDirection = directionOfEnv
azzurro.envDirection = directionOfEnv
nero.envDirection = directionOfEnv
Seq1 = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])
Seq2 = seq([nero, azzurro, rosso, giallo, bianco], [1, 1, 1, 1, 1])


Seq2.play(39.8, [cRnd, 100, 150], 500, 0.1, df = [100, 250, 500, 750, 1000], dt = 0.06)

Seq1.play(55.7, [cRnd, 100, 150], 500, 0.1, df = [cLin, 600, 40], dt = 0.006)
Seq2.play(107.6, [cLin, 200, 100], 200, 0.1, df = [cLin, 100, 0], dt = 0.1)
Seq2.play(168.6, [cRnd, 100, 150], 500, 0.4, df = [100, 250, 500, 750, 1000], dt = 0.06)
