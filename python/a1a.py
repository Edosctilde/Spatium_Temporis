from classi import *
from cost import *
from funz import *
setup(reverse, 0.05)
#inzio partitura
T = 0

Seq = seq([nero, azzurro, bianco, azzurro, rosso, giallo, bianco, rosso, bianco],
          [5,    10,      2,      3,       5,     2,      1,      7,     4])#34

azzurro.play(T, 16, 70, 40, 69)
T = 9
#hf
Seq.play(T, [cRnd, 100, 600], 150, [cLin, 60, 66], dt = 2, where = 0)
#lf
Seq.play(T, [cRnd, 20, 100], 50, [cLin, 66, 72], dt = 2, where = 0)

#
#@
#climax
T = 204
setup(direct, [cRnd, 4, 11])
Seq.play(T, [cRnd, 400, 600], 250, [cRnd, 60, 68], where = 180)
#lf
Seq.play(T, [cRnd, 10, 100], 90, [cRnd, 70, 80], where = [cRnd, 90, 180])
#climax cutter
dur = 2
setup(reverse, [4,3,7,13,9])
T = 244.5-dur
bianco.play(T, dur, 545, 121, 66, where = 160)
rosso.play(T, dur, 78, 121, 66, where = 160)
#
#@
#ripresa
setup(direct, 5)
T = 277
Seq.play(T, [cRnd, 400, 600], 250, [cLin, 65, 55], where = 180, dt = 12/34)
#lf
Seq.play(T, [cRnd, 10, 100], 90, [cLin, 68, 55], where = [cRnd, 90, 180], dt = 12/34)
#
#@
#finale
setup(direct, [cRnd, 0.08, 0.15])
T = 350
Seq.play(T, [cRnd, 1400, 1800], [cLin, 400, 100], [cLin, 60, 50], df = [0, 0, 0, 0, 0, 0, 0, 0, -250], where = 180)
nero.play(T, 6, 1200, 100, 0.005)
#
setup(direct, 7)
T = 350
Seq.play(T, [cRnd, 1000, 1400], [cLin, 400, 100], [cLin, 58, 45], where = 180)
nero.play(T, 6, 1200, 100, 0.005)

