from classi import *
from cost import *
from funz import*
#set della direzione dell'inviluppo DIRETTA
directionOfEnv = direct
bianco.dir = directionOfEnv
giallo.dir = directionOfEnv
rosso.dir = directionOfEnv
azzurro.dir = directionOfEnv
nero.dir = directionOfEnv
mod = 0.1
bianco.mod = mod
giallo.mod = mod
rosso.mod = mod
azzurro.mod = mod
nero.mod = mod
#dati
Seq1 = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])
Seq2 = seq([nero, azzurro, rosso, giallo, bianco], [1, 1, 1, 1, 1])
Seq3 = seq([azzurro, rosso, azzurro, rosso], [2, 1, 1.5, 2])
trasl = 41.93+9
#-----------------------------------#
#inizio
T = 0 + trasl
Seq1.play(T, [cRnd, 180, 220], 100, [cLin, 0.05, 0.2])

#lingua /sclaetta
T = 24+trasl

#prima frase
Seq2.play(T, [cRnd, 500, 550], 200, [cLin, 0.12, 0.02], dt = 4)

#mutazione
T = 40+trasl
Seq1.play(T, [cRnd, 60, 160], 100, [cLin, 0.1, 0.001], dt = 0.3)
Seq2.play(T, [cRnd, 450, 550], 150, [cLin, 0.1, 0.2], dt = 2.6)
T = Seq3.play(T, [cRnd, 550, 600], 60, [cLin, 0.15, 0.17], dt = 2)
#
Seq1.play(T, [cRnd, 100, 150], 500, 0.1, df = [cLin, 600, 40], dt = 0.006)
Seq1.play(T, [cRnd, 30, 160], 50, [cLin, 0.05, 0.001], dt = 0.15)
Seq3.play(T, [cRnd, 450, 550], 60, [cLin, 0.2, 0.15])

Seq1.play(T, [cRnd, 400, 450], 100, [0.05, 0.2, 0.1, 0.15], dt = 0.3)
T = Seq3.play(T , [cRnd, 660, 700], 50, [cLin, 0.05, 0.12], dt = 3)

#soffio
#Seq2.play(T, [cRnd, 500, 660], 50, [cLin, 0.1, 0.3], dt = 4)

