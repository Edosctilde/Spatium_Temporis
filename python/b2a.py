from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
setup(reverse, [4, 9, 10, 3, 12])

Seq = seq([nero, azzurro, rosso, giallo, bianco], [3,4,5,5,4])#21
Seq2 = seq([azzurro, rosso, nero, bianco, giallo], [2,5,7,6,1])#21
Seq3 = seq([giallo, nero, azzurro, rosso, bianco], [2,3,4,5,7])#21
T = 168.8
Seq.play(T, [cRnd, 300, 600], 50, [cLin, 56, 68], where = 180)
Seq.airsim(T, [cRnd, 400, 700], 100, [cLin, 55, 66], df = [cRnd, -200, 200], where = 180, dt = 0.5)
Seq2.play(T, [cRnd, 2550, 2650], 150, [cLin, 56, 62], df = [cRnd, -100, 100], where = 135)
Seq3.play(T, [cRnd, 100, 300], 30, [cLin, 60, 64], df = [cRnd, -50, 50], where = 90)
setup(reverse, 15)
T = Seq3.airsim(T, [cRnd, 9000, 9500], 150, [cLin, 58, 52], df = [cRnd, -150, 150], where = 180, dt = 0.5)

setup(reverse, 0.2)
Seq.airsim(T, [cRnd, 400, 4700], 100, [cLin, 60, 68], df = [cRnd, -200, 200], where = 180, dt = 1.6)
T += 7
setup(direct, 10)
Seq3.play(T, [cRnd, 100, 900], 200, [cRnd, 63, 70], df = [cRnd, -250, 250], where = 190, dt = 0.6)
Seq2.play(T, [cRnd, 100, 1900], 200, [cRnd, 63, 70], df = [cRnd, -250, 250], where = 190, dt = 1.3)

T+= 7
Seq2.play(T, [cRnd, 6600, 7000], 200, [cRnd, 64, 68], df = [cRnd, -300, 300], dt = 1)
Seq3.play(T, [cRnd, 1600, 3000], 200, [cRnd, 66, 70], df = [cRnd, -300, 300], dt = 1)

T += 7
setup(direct, [1,3,5,7,9])
Seq.play(T, [cRnd, 1400, 1700], 100, [cLin, 66, 70], df = [cRnd, -200, 200], where = 180, dt = 0.16)

#climax
T = 204
setup(direct, [3, 4, 7, 12, 9])
Seq.airsim(T, [cRnd, 400, 700], 100, [cLin, 55, 63], df = [cRnd, -200, 200], where = [cRnd, 0, 90], dt = 39/21)
Seq2.airsim(T, [cRnd, 2550, 2650], 150, [cLin, 54, 60], df = [cRnd, -100, 100], where = [cRnd, 90, 180], dt = 39/21)
Seq3.airsim(T, 60, 30, [cRnd, 63, 66], where = [cRnd, 0, 180], dt = 38/21)


#climax cutter
dur = 2
setup(reverse, [4,3,7,13,9])
T = 244.5-dur
bianco.play(T, dur, 560, 121, 0.1, where = 160)
rosso.play(T, dur, 2580, 121, 0.1, where = 160)
giallo.play(T, dur, 60, 121, 0.1, where = 160)
