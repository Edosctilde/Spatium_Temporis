from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
setup(reverse, [4, 9, 10, 3, 12])

Seq = seq([nero, azzurro, rosso, giallo, bianco], [3,4,5,5,4])#21
Seq2 = seq([azzurro, rosso, nero, bianco, giallo], [2,5,7,6,1])#21
Seq3 = seq([giallo, nero, azzurro, rosso, bianco], [2,3,4,5,7])#21
T = 168.8
Seq.play(T, [cRnd, 300, 600], 50, [cLin, 0.005, 0.1], where = 180)
Seq.play(T, [cRnd, 400, 700], 100, [cLin, 0.003, 0.08], df = [cRnd, -200, 200], where = 180, dt = 0.5)
Seq2.play(T, [cRnd, 2550, 2650], 150, [cLin, 0.005, 0.02], df = [cRnd, -100, 100], where = 135)
Seq3.play(T, [cRnd, 100, 300], 30, [cLin, 0.001, 0.01], df = [cRnd, -50, 50], where = 90)
setup(reverse, 15)
T = Seq3.play(T, [cRnd, 9000, 9500], 150, [cLin, 0.005, 0.01], df = [cRnd, -150, 150], where = 180, dt = 0.5)

setup(reverse, [4, 7, 9, 14, 17])
Seq.play(T, [cRnd, 400, 4700], 100, [cLin, 0.003, 0.1], df = [cRnd, -200, 200], where = 180, dt = 1.6)
T += 7
setup(direct, 10)
Seq3.play(T, [cRnd, 100, 900], 200, [cRnd, 0.05, 0.1], df = [cRnd, -250, 250], where = 190, dt = 0.6)
Seq2.play(T, [cRnd, 100, 1900], 200, [cRnd, 0.05, 0.1], df = [cRnd, -250, 250], where = 190, dt = 1.3)

T+= 7
Seq2.play(T, [cRnd, 6600, 7000], 200, [cRnd, 0.05, 0.1], df = [cRnd, -300, 300], dt = 1)
Seq3.play(T, [cRnd, 1600, 3000], 200, [cRnd, 0.05, 0.1], df = [cRnd, -300, 300], dt = 1)

T += 7
setup(direct, [1,3,5,7,9])
Seq.play(T, [cRnd, 1400, 1700], 100, [cLin, 0.1, 0.15], df = [cRnd, -200, 200], where = 180, dt = 0.16)

T += 3.5
setup(reverse, [1,3,5,7,9])
Seq.play(T, [cRnd, 2400, 2700], 100, [cLin, 0.1, 0.15], df = [cRnd, -200, 200], where = 180, dt = 0.16)

T = 204
setup(direct, [3, 4, 7, 12, 9])
Seq.play(T, [cRnd, 400, 700], 100, [cLin, 0.003, 0.08], df = [cRnd, -200, 200], where = [cRnd, 0, 90], dt = 39/21)
Seq2.play(T, [cRnd, 2550, 2650], 150, [cLin, 0.005, 0.02], df = [cRnd, -100, 100], where = [cRnd, 90, 180], dt = 39/21)
Seq3.play(T, 60, 30, [cRnd, 0.08, 0.2], where = [cRnd, 0, 180], dt = 39/21)

