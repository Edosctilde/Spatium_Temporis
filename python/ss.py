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
Seq1 = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])#44
Seq2 = seq([nero, azzurro, rosso, giallo, bianco], [1, 1, 1, 1, 1])#5


Seq2.play(39.8+9, [cRnd, 100, 150], 500, 70, df = [100, 250, 500, 750, 1000], dt = 0.06)

Seq1.play(55.7+9, [cRnd, 100, 150], 500, 72, df = [cLin, 600, 40], dt = 0.006)
Seq2.play(107.6+9, [cLin, 200, 100], 200, 70, df = [cLin, 100, 0], dt = 0.1)

Seq2.play(203.9, [cLin, 140, 1450], 500, 69, df = (1450-140)/5, dt = 0.06)
Seq2.play(203.9, [cLin, 140, 50], 50, 72, df = -18, dt = 0.06)



#leading and leaving climax
setup(reverse, 0.5)
dur = 18
for i in range(dur-1):
    nero.play(204-dur+(i+1), 2, 140, 10*(i+1), 50+i)
setup(direct, 13)

nero.play(204, 39/2, 140, 100, 72, where = 45)

Seq1.play(339.5, [cRnd, 100, 150], 500, [cLin, 50, 65], df = [cLin, 600, 40], dt = 1/44)
Seq2.play(340, [cLin, 200, 100], 200, [cLin, 48, 62], df = [cLin, 100, 0], dt = 1/5)

