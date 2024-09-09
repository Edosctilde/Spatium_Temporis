from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
directionOfEnv = direct
bianco.envDirection = directionOfEnv
giallo.envDirection = directionOfEnv
rosso.envDirection = directionOfEnv
azzurro.envDirection = directionOfEnv
nero.envDirection = directionOfEnv

Seq = seq([nero, azzurro, bianco, azzurro, rosso, giallo, bianco, rosso, bianco],[5, 10, 2, 3, 5, 2, 1, 7, 4])

Seqh = seq([giallo, rosso, bianco, azzurro, giallo, nero], [7, 4, 5, 6, 7, 13])
Seql = seq([bianco, nero, giallo, azzurro, rosso, giallo, rosso], [5, 6, 7, 3, 8, 6, 4])

Seqm = seq([giallo, bianco, giallo, rosso, nero, azzurro], [6, 5, 5, 10, 8, 5])


#inzio partitura
T = 0
T = Seq.play(T, [cRnd, 100, 1000], 40, [cLin, 0.02, 0.2], dt = 0.3)
Seq.play(T, [cRnd, 10, 100], 40, [cLin, 0.2, 0.3], dt = 0.3)
T = 15
for i in range(15):
    Seqm.play(T, [cRnd, 2120, 3400], 100, [cRnd, 0.05, 0.20 ], df = [cRnd, -100, 100], dt = 0.3-(i*0.02))
    T += sum(Seqm.pesi)*(0.02)
T = 15
for i in range(15):
    Seqh.play(T, [cRnd, 6020, 8400], 300, [cRnd, 0.05, 0.15], df = [cRnd, -100, 100], dt = 0.3-(i*0.02))
    T += sum(Seqh.pesi)*(0.02)

T = 15
for i in range(15):
    Seql.play(T, [cRnd, 1520, 3000], 100, [cRnd, 0.05, 0.20], df = [cRnd, -100, 100], dt = 0.3-(i*0.02))
    T += sum(Seql.pesi)*(0.02)
T = 0
"""
for i in range(13):
    Seql.play(T, [cRnd, 20, 100], 100, [cLin, 0.01+(i*0.02), 0.02+(i*0.02)], dt = 0.05)
    T =Seqh.play(T, [cRnd, 9020, 10000], 100, [cLin, 0.01+(i*0.02), 0.02+(i*0.02)], dt = 0.05)
"""
osc(giallo, T, 26, 200, 100, [cLin, 0.001, 0.3], 9)
osc(nero, T, 26, 20, 10, [cLin, 0.001, 0.2], 2)
osc(giallo, T, 26, 10200, 100, [cLin, 0.001, 0.2], 5)



T = 30
osc(giallo, T, 20, 200, 50, [cLin, 0.01, 0.2], 4)
for i in range(30):
    Seql.play(T, [cRnd, 1520, 3000], 100, [cRnd, 0.05, 0.20], df = [cRnd, -100, 100], dt = randint(2,10)/100)
    Seqh.play(T, [cRnd, 6020, 8400], 300, [cRnd, 0.05, 0.15], df = [cRnd, -100, 100], dt = randint(2, 10)/100)
    T = Seqm.play(T, [cRnd, 2120, 3400], 100, [cRnd, 0.05, 0.20 ], df = [cRnd, -100, 100], dt = randint(2, 10)/100)
    Seql.play(T, [cRnd, 20, 100], 100, 0.1, dt = 0.05)
    Seqh.play(T, [cRnd, 9020, 10000], 100, 0.1, dt = 0.05)


