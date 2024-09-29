from classi import *
from cost import *
from funz import*
import random as r

setup(direct, 0.01)

#dati
Seqa = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])
Seqb = seq([azzurro, rosso, azzurro, rosso, giallo, bianco], [3.17, 2, 4.2, 3.4, 5.6, 6])

T = 117
Seqb.airsim(T , [680, 690, 620, 640, 580, 560], 50, [cLin, 60, 68], dt = 1.3, where = [cRnd, 90, 180])
T = Seqb.airsim(T , [680, 690, 620, 640, 580, 560], 50, [cLin, 60, 68], dt = 1.3, where = [cRnd, 0, 90])
Seqa.play(T, [cRnd, 400, 450], 100, [cLin, 65, 50], dt = 0.8)

T = 294
T = Seqb.play(T , [680, 690, 620, 640, 580, 560], 50, [cRnd, 48, 56], dt = 1.3, legato = True)
Seqa.play(T, [cRnd, 400, 450], 100, [cLin, 40, 46], dt = 0.5)
