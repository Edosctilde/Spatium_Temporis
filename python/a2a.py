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
Seq1.play(T, [cRnd, 180, 220], 100, [cLin, 63, 69])

T = 24+trasl
#prima frase
Seq2.play(T, [cRnd, 500, 550], 200, [cLin, 65, 68], dt = 4)

#mutazione
T = 40+trasl
Seq1.play(T, [cRnd, 60, 160], 100, [cLin, 72, 68], dt = 0.3)
Seq2.play(T, [cRnd, 450, 550], 150, [cLin, 63, 70], dt = 2.6)
T = Seq3.play(T, [cRnd, 550, 600], 60, [cLin, 65, 70], dt = 2)
#
Seq1.play(T, [cRnd, 100, 150], 500, 68, df = [cLin, 600, 40], dt = 0.006)
Seq1.play(T, [cRnd, 30, 160], 70, [cLin, 58, 53], dt = 0.15)
Seq3.play(T, [cRnd, 450, 550], 65, [cLin, 67, 60])

Seq1.play(T, [cRnd, 400, 450], 100, [67, 70, 64, 68], dt = 0.3)
T = Seq3.play(T , [cRnd, 660, 700], 50, [cLin, 65, 68], dt = 3)
#climax
T = 204
#39
setup(reverse, 9)
Seq1.play(T, [cRnd, 10500, 15000], 500, 58, df = [cLin, 600, 40], dt = 39/44)
Seq2.play(T, [cRnd, 2030, 2160], 50, [cLin, 62, 65], dt = 39/5)
Seq3.play(T, [cRnd, 3450, 3550], 60, [cLin, 65, 67], dt = 39/6.5)
#climax cutter
dur = 2
setup(reverse, [4,3,7,13,9])
T = 244.5-dur
bianco.play(T, dur, 12560, 121, 0.1, where = 160)
rosso.play(T, dur, 2080, 121, 0.1, where = 160)
giallo.play(T, dur, 3460, 121, 0.1, where = 160)

T = 277
Seq1.play(T, [cRnd, 10500, 15000], 500, [cLin, 0.08, 0.001], df = [cLin, 600, 40], dt = 14/44)
Seq2.play(T, [cRnd, 2030, 2160], 50, [cLin, 0.1, 0.002], dt = 9/5)
Seq3.play(T, [cRnd, 3450, 3550], 60, [cLin, 0.2, 0.002])
