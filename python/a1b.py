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



Seq = seq([bianco, rosso, bianco, azzurro, rosso],
          [6, 4, 0.4, 5, 9])
Seq2 = seq([azzurro, bianco, giallo, rosso, nero, azzurro], [2, 1, 1, 1, 1, 1.5])
#inzio partitura
T = 50
osc(nero, T, 5, 120, 10, [cLin, 0.01, 0.02], 2)
Seq.play(T, [10300, 10500, 10000, 10500, 10200, 10300], 650, 0.01, df = [cRnd, -500, 500], dt = 1)
Seq2.play(T, [13300, 13500, 13000, 13500, 13200, 13300], 150, 0.005, df = [cRnd, -500, 500], dt = 1)
osc(rosso, T, 15, 80, 10, [cLin, 0.01, 0.02], 3)


"""
T = Seq.play(T, [9300, 9500, 9000, 1500, 1200], 350, [cLin, 0.02, 0.2], df = [100, -100, -8500, 0, 0])
azzurro.long_play(T, 8, 300, 100, 0.2)

T += 10
Seq2.play(T, [9300, 9500, 9000, 9500, 9200, 9300], 650, 0.01, df = [cRnd, -500, 500], dt = 2)
Seq2.play(T, [4300, 4500, 4000, 4500, 4200, 4300], 150, 0.005, df = [cRnd, -500, 500], dt = 2)

T = 0
Seq2.play(T, [10300, 10500, 10000, 10500, 10200, 10300], 650, 0.01, df = [cRnd, -500, 500], dt = 3)
Seq2.play(T, [3300, 3500, 3000, 3500, 3200, 3300], 150, 0.005, df = [cRnd, -500, 500], dt = 3)
"""
