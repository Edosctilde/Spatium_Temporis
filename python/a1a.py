from classi import *
from cost import *
from funz import *
setup(reverse, [cRnd, 0.08, 0.15])
#inzio partitura
T = 0

Seq = seq([nero, azzurro, bianco, azzurro, rosso, giallo, bianco, rosso, bianco],
          [5,    10,      2,      3,       5,     2,      1,      7,     4])#34

azzurro.play(T, 10, 60, 70, 0.05)
T = 9
#hf
Seq.play(T, [cRnd, 20, 600], 150, [cLin, 0.02, 0.2], dt = 2)
#lf
Seq.play(T, [cRnd, 10, 100], 50, [cLin, 0.01, 0.1], dt = 2)

T = 204
setup(direct, 5)
Seq.play(T, [cRnd, 400, 600], 250, [cRnd, 0.05, 0.1], where = 180)
#lf
Seq.play(T, [cRnd, 10, 100], 90, [cRnd, 0.05, 0.1], where = [cRnd, 90, 180])

T = 277
Seq.play(T, [cRnd, 400, 600], 250, [cLin, 0.1, 0.05], where = 180, dt = 12/34)
#lf
Seq.play(T, [cRnd, 10, 100], 90, [cLin, 0.1, 0.05], where = [cRnd, 90, 180], dt = 12/34)

#finale
setup(direct, [cRnd, 0.08, 0.15])
T = 350
Seq.play(T, [cRnd, 1400, 1800], [cLin, 400, 100], [cLin, 0.01, 0.005], df = [0, 0, 0, 0, 0, 0, 0, 0, -250], where = 180)
nero.play(T, 6, 1200, 100, 0.005)
#
setup(direct, 7)
T = 350
Seq.play(T, [cRnd, 1000, 1400], [cLin, 400, 100], [cLin, 0.01, 0.005], where = 180)
nero.play(T, 6, 1200, 100, 0.005)
