from cost import *
from funz import *
#CLASSI
#definisco la classe base
class inst():
    def __init__(self, nomeFile, envDirection, modulation):
        self.nomeFile = nomeFile
        self.dir = envDirection
        self.mod = modulation
        
    def play(self, when, dur, f, bw, vol, where = None, df = 0):
        
        alpha = gestione_spazio(when, where)
        print("i1 %f %f \"../audioFiles/%s.wav\" %f %f %f %f %f %f %f" %(when, dur, self.nomeFile, f, bw, alpha, vol, df, self.dir, self.mod))
        
        return when+dur

    def long_play(self, when, dur, f, bw, vol, where = None, df = 0, segmentazione = None):
        #la funzione serve a generare fasce sonore + lunghe di AudioMaxLen
        durate = segmentazione_durata(dur, segmentazione)
        for n in range(len(durate)):
            newf = f+(df*n/len(durate))
            newdf = df/len(durate)
            if n == len(durate)-1:
                dur = durate[n]
            else:
                dur = durate[n]*6/5
            self.play(when, dur, newf, bw, vol, where, newdf)
            when += durate[n]
        return when
#
#      
#Ora la classe che riproduce in sequenza gli elementi
class seq():
    def __init__(self, sequenza, pesi):
        self.sequenza = sequenza
        self.pesi = pesi
        
    def play(self, when, f, bw, vol, where = None, df = 0, dt = 1, legato = True):
        #dt è l'unità temporale
        lung = len(self.sequenza)
        f = check_ea(f, lung)
        bw = check_ea(bw, lung)
        vol = check_ea(vol, lung)
        where = check_ea(where, lung)
        df = check_ea(df, lung)
        if legato:
            durate = [i*6/5 for i in self.pesi]
        else:
            durate = self.pesi
        for n in range(lung):
            if self.pesi[n]*dt > AudioMaxLen:
                self.sequenza[n].long_play(when, durate[n]*dt, f[n], bw[n], vol[n], where[n], df[n])
                when += self.pesi[n]*dt
            elif self.pesi[n]*dt < AudioMaxLen:
                self.sequenza[n].play(when, durate[n]*dt, f[n], bw[n], vol[n], where[n], df[n])
                when += self.pesi[n]*dt
        return when

    
    def airsim(self, when, f, bw, vol, ndiram = 5, ddf = 100, where = None, df = 0, dt = 1):
        self.play(when, f, bw, vol, where, df, dt)
        durFix = ndiram/sum(self.pesi)
        for i in range(ndiram):
            self.play(when+(i/durFix), f, bw, vol, where, df = [cRnd, -ddf, +ddf])
        return when + (sum(self.pesi)*dt)

        
    def osc(self, when, f, bw, vol, noscil, where = None, df = 0, dt = 1, legato = True):
        lung = len(self.sequenza)
        f = check_ea(f, lung)
        bw = check_ea(bw, lung)
        vol = check_ea(vol, lung)
        where = check_ea(where, lung)
        df = check_ea(df, lung)
        noscil = check_ea(noscil, lung)
        if legato:
            durate = [i*6/5 for i in self.pesi]
        else:
            durate = self.pesi
        for n in range(lung):         
            osc(self.sequenza[n], when, self.pesi[n]*dt, f[n], bw[n], vol[n], noscil[n], where[n], df[n])
            when += self.pesi[n]*dt
        return when
"""   
    def tronca(self, when, dur, f, bw, vol, where = None, df = 0, dt = 1):
        lung = len(self.sequenza)
        f = check_ea(f, lung)
        bw = check_ea(bw, lung)
        vol = check_ea(vol, lung)
        where = check_ea(where, lung)
        df = check_ea(df, lung)
        tbkp = when
        n = 0
        while when-tbkp <= dur:
            if self.pesi[n]*dt > AudioMaxLen:
                when = self.sequenza[n].long_play(when, self.pesi[n]*dt, f[n], bw[n], vol[n], where[n], df[n])
            elif self.pesi[n]*dt < AudioMaxLen:
                when = self.sequenza[n].play(when, self.pesi[n]*dt, f[n], bw[n], vol[n], where[n], df[n])
            n += 1
        return when
        
    def eForma(self, when, f, bw, vol, nosc, where = None, df = 0, dt = 1, legato = True):
        #dt è l'unità temporale
        lung = len(self.sequenza)
        f = check_ea(f, lung)
        bw = check_ea(bw, lung)
        vol = check_ea(vol, lung)
        where = check_ea(where, lung)
        df = check_ea(df, lung)
        #nosc = check_ea(
        for n in range(lung):           
            self.sequenza[n].play(when, durate[n]*dt, f[n], bw[n], vol[n], where[n], df[n])
            when += self.pesi[n]*dt
        return when
"""
        
#definisco gli strumenti per ogni file che ho
bianco = inst("b", direct, 0.5)
giallo = inst("g", direct, 0.5)
rosso = inst("r", direct, 0.5)
azzurro = inst("a", direct, 0.5)
nero = inst("n", direct, 0.5)

colors = [nero, azzurro, rosso, giallo, bianco]

def setup(envdir, modul):
    envdir = check_ea(envdir, 5)
    modul = check_ea(modul, 5)
    for i in range(5):
        colors[i].dir = envdir[i]
        colors[i].mod = modul[i]
        
