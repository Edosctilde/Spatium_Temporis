sr = 96000
kr = 44100
nchnls = 2
0dbfs = 1

#include "csound/oplib.csd"

;##############################################################################;

instr 1
  $SETUP(p4'p5'p6'p7'p8'p9)
  $FILT(aS_mono'kfilt'ibandwidth)
  iatk = p3*0.01
  isus = p3*4/5
  irel = p3-iatk-isus
  imod = p11
  if (p10  == 1) then
    ;kEnv expseg 0.0001, 0.006*p3, ivol, 0.004*p3, ivol/2, p3*(4/5-0.01), ivol/2, p3/5, 0.0001
    kEnv linseg 0, iatk, ivol, isus, ivol, irel, 0
  elseif (p10 == 0) then
    ;kEnv expseg 0.0001, p3/5, ivol, p3*(4/5-0.01), ivol/2, 0.004*p3, ivol/2, 0.006*p3, 0.0001
    kEnv linseg 0, iatk, ivol, isus, ivol, irel, 0
  endif
  $MIDSIDE(aS_bal'kEnv'ialpha'imod)
endin

;------------------------------------------------------------------------------;


