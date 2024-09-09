;OPCODES

opcode MS, aa, akk
    amono, kag, kmod xin
    aSmod poscil 1, kmod
    kar = kag*3.141592653589793/180
    aM = amono*sin(kar)
    aS = amono*cos(kar)*aSmod
    xout aM, aS
endop

opcode SDMX, aa,aa
    ain1,ain2 xin
    asum = (ain1+ain2)/sqrt(2)
    adif = (ain1-ain2)/sqrt(2)
    xout asum,adif
endop


opcode PHIL, a, aki
  asig, kfl, ibw xin
  as1 butbp asig, kfl, ibw
  as2 butbp as1, kfl, ibw
  aS butbp as2, kfl, ibw
  xout aS
endop


opcode FILT26, a, akk ;FILTRO DEL 26esimo ORDINE
  asig, kfl, kfh xin
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterlp asig, kfh
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  asig butterhp asig, kfl
  aS butterhp asig, kfl
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
        ivol   =  $p8
#;fine setup


;inizio filtraggio
#define FILT(aS'kf'ib) #
        aS_filt PHIL $aS, $kf, $ib  ;filtro il segnale
        abal poscil 0.5, 440  ;segnale (una sinusoide di amp 1) con cui bilanciare il segnale filtrato
        aS_bal balance aS_filt, abal
#;fine filtraggio


;inizio ms
#define MIDSIDE(aS_bal'kEnv'ialpha'imod) #
        aMid, aSide MS $aS_bal*$kEnv, $ialpha, $imod
        aL, aR SDMX aMid, aSide
    outs aL, aR
#;fine ms