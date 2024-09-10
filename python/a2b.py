from classi import *
from cost import *
from funz import*
import random as r

#set della direzione dell'inviluppo DIRETTA
directionOfEnv = direct
bianco.dir = directionOfEnv
giallo.dir = directionOfEnv
rosso.dir = directionOfEnv
azzurro.dir = directionOfEnv
nero.dir = directionOfEnv
#    #    #    #    #
mod = 0.2
bianco.mod = mod
giallo.mod = mod
rosso.mod = mod
azzurro.mod = mod
nero.mod = mod

#dati
Seqa = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])
Seqb = seq([azzurro, rosso, azzurro, rosso, giallo, bianco], [3.17, 2, 4.2, 3.4, 5.6, 6])

T = 108+9

#Seqa.play(T, [cRnd, 400, 450], 100, [0.05, 0.2, 0.1, 0.15], dt = 0.3)
T = Seqb.play(T , [680, 690, 620, 640, 580, 560], 50, [cLin, 0.12, 0.5], legato = True)
