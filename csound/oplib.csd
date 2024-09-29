;OPCODES

opcode MS, aa, akkk
  amono, kag, kmod, kpp xin
  aSmod poscil kpp, kmod        ; in caso cambiare kpp con 0.5
  kar = kag*3.141592653589793/180
  ipos = 0.785398163397
  kM = sin(kar)
  kS = cos(kar)
  aM = amono*kM
  aS = amono*kS*aSmod
  aL = amono*(1-kpp) + (kpp * (aM*sin(ipos) + aS*cos(ipos)))/2
  aR = amono*(1-kpp) + (kpp * (aM*sin(-ipos) + aS*cos(-ipos)))/2
  
  xout aL, aR
endop


opcode PHIL, a, aki
  asig, kfl, ibw xin
  as1 butbp asig, kfl, ibw
  as2 butbp as1, kfl, ibw
  aS butbp as2, kfl, ibw
  xout aS
endop


;inizio setup
#define SETUP(p4'p5'p6'p7'p8'p9) #
;CARICO IL SUONO

        aS_mono diskin2 $p4
        
    ;DEFINISCO LA FREQUENZA DI FILTRAGGIO E LA BANDA
        if0   =   $p5       ;frequenza di partenza
        ibandwidth = $p6    ;ampiezza banda del filtro
        iff   =   if0 + $p9 ;frequenza finale
        kfilt linseg if0, p3, iff
    ;DEFINISCO L'ANGOLO PER MS
        ialpha =  $p7
    ;DEFINISCO IL VOLUME [0;1]
        ivol   =  ampdb($p8)/32767
#;fine setup


;inizio filtraggio
#define FILT(aS'kf'ib) #
        aS_filt PHIL $aS, $kf, $ib  ;filtro il segnale
        abal poscil 1, 440  ;segnale (una sinusoide di amp 0.9) con cui bilanciare il segnale filtrato
        aS_bal balance aS_filt, abal
#;fine filtraggio

