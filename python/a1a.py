from classi import *
from cost import *
from funz import *
#set della direzione dellìinviluppo INVERSA
directionOfEnv = reverse
bianco.envDirection = directionOfEnv
giallo.envDirection = directionOfEnv
rosso.envDirection = directionOfEnv
azzurro.envDirection = directionOfEnv
nero.envDirection = directionOfEnv

#inzio partitura
T = 0

Seq = seq([nero, azzurro, bianco, azzurro, rosso, giallo, bianco, rosso, bianco],
          [5,    10,      2,      3,       5,     2,      1,      7,     4])

#hf
Seq.play(T, [cRnd, 20, 600], 150, [cLin, 0.05, 0.2], dt = 2)
#lf
Seq.play(T, [cRnd, 10, 100], 50, [cLin, 0.02, 0.1], dt = 2)
#vedi se mettere un booost a inizio sulle basse, magari in partenza
