from cost import *
from random import *

def line(dt, x, y0, y1):
    a = (y1-y0)/dt
    b = y0
    return a * x + b


def osc(colore, when, dur, f, bw, vol, fmod, where = None, df = 0, whole = 1):
    nTotosc = int(fmod*dur)
    lung = nTotosc
    f = check_ea(f, lung)
    bw = check_ea(bw, lung)
    vol = check_ea(vol, lung)
    where = check_ea(where, lung)
    df = check_ea(df, lung)
    for n in range(nTotosc):
        colore.play(when, 1.1*whole/fmod, f[n], bw[n], vol[n], where[n], df[n])
        when += 1/fmod
    return when


def gestione_spazio(tempo, spazio):
    #se non viene indicato nessun valore per lo spazio in particolare lo pone come il tempo +90 (sfasamento di 90 gradi del valore)
    if spazio is None:
        pos = tempo + 90
    elif spazio is not None:
        pos = spazio
    return pos


def segmentazione_durata(dur, segmentazione):
    #segmenta la durata dell'evento sonoro
    if segmentazione is None:
        tempi = []
        for i in range(int(dur/AudioMaxLen)):
            tempi.append(AudioMaxLen)
        tempi.append(dur%AudioMaxLen)#+(len(tempi)*AudioMaxLen/5))
    elif segmentazione is not None:
        tempi = segmentazione
    return tempi


def element_to_array(item, lung):
    #riempire un array con lung elementi di item
    array = []
    for i in range(lung):
        array.append(item)
    return array


def randArray(item, lung):
    array = []
    if type(item[1]) is float:
        n = len(str(item[1]))-2
    else:
        n = 0
    fix = pow(10, n)
    for i in range(lung):
        array.append(randint(int(item[1]*fix), int(item[2]*fix))/fix)
    return array

def linArray(item, lung):
    array = []
    step = (item[2]-item[1])/lung
    for i in range(lung):
        array.append(item[1]+(i*step))
    return array

                                                              #FARE SI CHE SE SI PASSA UN PARAMETO RAND VENGONO SCELTI DEI VALORI A CAZZO
def check_ea(item, lung):
    #controlla se item è un e(lemento) o un a(rray)
    #per necessità compositive se il caso è il primo poi lo converte in un array di se stesso
    if (type(item) is int) or (type(item) is float) or (type(item) is NoneType):
        newarray = element_to_array(item, lung)
    elif type(item) is list:
    #quando si passa gia un array lo si legge come tale, a meno che il primo carattere non sia un codice, in tal caso viene eseguita una determinata funzione di sorting secondo l'andamento descritto dal codice
        if type(item[0]) is str:
            if item[0] == cRnd:
                newarray = randArray(item, lung)
            elif item[0] == cLin:
                newarray = linArray(item, lung)
            elif item[0] == cEsp:
                pass
            
        elif (type(item[0]) is int) or (type(item[0]) is float):
            newarray = item
    return newarray


def andamento_aria(sequenza, when, f, bw, vol, df, ddf = [-1000, 1000], dt = 0.2, ddt = 0.1, where = None):
    #df = check_ea(df, len(sequenza.pesi))
    lung = len(sequenza.pesi)
    f = check_ea(f, lung)
    bw = check_ea(bw, lung)
    vol = check_ea(vol, lung)
    where = check_ea(where, lung)
    df = check_ea(df, lung)
    for j in range(len(sequenza.pesi)):
        if df[j] == 0:
            #se non ce un glissando il comportamento è regolare
            dT = dt
           
        else:
            #se ce il glissando il comportamento puo venire distorto nel dominio del tempo
            dT = dt*ddt
            
        rep = sequenza.pesi[j]/(sum(sequenza.pesi)*dT)
        tbkp = when
        resto = rep-int(rep)
        for i in range(int(rep)):
       
            dr = int(line(sequenza.pesi[j], when-tbkp, 0, df[j]))
            dF = [cRnd, ddf[0]+dr, ddf[1]+dr]
            when = sequenza.play(when, f, bw, vol[j], df = dF, dt = dT)
        sequenza.tronca(when, resto*sum(sequenza.pesi)*dT, f, bw, vol, df = dF, dt = dT)
        
        when = tbkp + sequenza.pesi[j]
    return when
##############################################################
"""
def nuvola( inst,when, dur, n, f, bw, vol, df = 50, overlap=2, dyn = None, dir = None):
    dt = dur/n/overlap
    tbkp = when
    
    
    for i in range(n):
        if dyn is None:
            v = vol
        elif dyn is not None:
            v = line(dur, when-tbkp, vol, dyn)
        dv = v/overlap
        if dir is None:
            r = randint(0,1)
            dir = r-(1-r)
        elif dir is not None:
            dir = dir
        freq = randint(f-df, f+df)
        inst.play(when, dt*overlap, freq, bw, dv, alpha = when+90, df = df*dir)
        when += dt
    return when



"""
