from classi import *
from cost import *
from funz import*
import random as r

setup(direct, 0.2)

#dati
Seqa = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])
Seqb = seq([azzurro, rosso, azzurro, rosso, giallo, bianco], [3.17, 2, 4.2, 3.4, 5.6, 6])

T = 117
Seqb.play(T , [680, 690, 620, 640, 580, 560], 50, [cLin, 0.06, 0.25], dt = 1.3,legato = True, where = [cRnd, 90, 180])
T = Seqb.play(T , [680, 690, 620, 640, 580, 560], 50, [cLin, 0.06, 0.25], dt = 1.3,legato = True, where = [cRnd, 0, 90])
Seqa.play(T, [cRnd, 400, 450], 100, [cLin, 0.2, 0.05], dt = 0.8)

T = 294
T = Seqb.play(T , [680, 690, 620, 640, 580, 560], 50, [cRnd, 0.01, 0.04], dt = 1.3, legato = True)
Seqa.play(T, [cRnd, 400, 450], 100, [cLin, 0.010, 0.040], dt = 0.5)
