from classi import *
from cost import *
from funz import*
#set della direzione dell'inviluppo DIRETTA
setup(direct, [cRnd, 0.05, 0.3])
#dati
Seq1 = seq([nero, azzurro, giallo, bianco], [20, 6, 12, 6])#44
Seq2 = seq([nero, azzurro, rosso, giallo, bianco], [1, 1, 1, 1, 1])#5
Seq3 = seq([azzurro, rosso, azzurro, rosso], [2, 1, 1.5, 2])#6.5
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

T = 204
#39
setup(reverse, 9)
Seq1.play(T, [cRnd, 10500, 15000], 500, 0.1, df = [cLin, 600, 40], dt = 39/44)
Seq2.play(T, [cRnd, 2030, 2160], 50, [cLin, 0.05, 0.1], dt = 39/5)
Seq3.play(T, [cRnd, 3450, 3550], 60, [cLin, 0.2, 0.15], dt = 39/6.5)

T = 277
Seq1.play(T, [cRnd, 10500, 15000], 500, [cLin, 0.08, 0.001], df = [cLin, 600, 40], dt = 14/44)
Seq2.play(T, [cRnd, 2030, 2160], 50, [cLin, 0.1, 0.002], dt = 9/5)
Seq3.play(T, [cRnd, 3450, 3550], 60, [cLin, 0.2, 0.002])
