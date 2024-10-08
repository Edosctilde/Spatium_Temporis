PY = python
CS = csound

all: a1a a2a a1b a2b b1a b1b b2a b2b c1a c1b ss

a2a: $(PY)/a2a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a2a.py > $(CS)/scoa2a.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa2a.sco -o Media/a2a

a1a: $(PY)/a1a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a1a.py > $(CS)/scoa1a.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa1a.sco -o Media/a1a


a1b: $(PY)/a1b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a1b.py > $(CS)/scoa1b.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa1b.sco -o Media/a1b

a2b: $(PY)/a2b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a2b.py > $(CS)/scoa2b.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa2b.sco -o Media/a2b

b1a: $(PY)/b1a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/b1a.py > $(CS)/scob1a.sco
	$(CS) $(CS)/orc.orc $(CS)/scob1a.sco -o Media/b1a

b1b: $(PY)/b1b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/b1b.py > $(CS)/scob1b.sco
	$(CS) $(CS)/orc.orc $(CS)/scob1b.sco -o Media/b1b

b2a: $(PY)/b2a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/b2a.py > $(CS)/scob2a.sco
	$(CS) $(CS)/orc.orc $(CS)/scob2a.sco -o Media/b2a

b2b: $(PY)/b2b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/b2b.py > $(CS)/scob2b.sco
	$(CS) $(CS)/orc.orc $(CS)/scob2b.sco -o Media/b2b

ss: $(PY)/ss.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/ss.py > $(CS)/scoss.sco
	$(CS) $(CS)/orc.orc $(CS)/scoss.sco -o Media/ss

c1a: $(PY)/c1a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/c1a.py > $(CS)/scoc1a.sco
	$(CS) $(CS)/orc.orc $(CS)/scoc1a.sco -o Media/c1a

c1b: $(PY)/c1b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/c1b.py > $(CS)/scoc1b.sco
	$(CS) $(CS)/orc.orc $(CS)/scoc1b.sco -o Media/c1b
