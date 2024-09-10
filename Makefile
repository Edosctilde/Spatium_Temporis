PY = python
CS = csound

all: a1a a2a a1b ss

a2a: $(PY)/a2a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a2a.py > $(CS)/scoa2a.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa2a.sco -o results/a2a


a1a: $(PY)/a1a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a1a.py > $(CS)/scoa1a.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa1a.sco -o results/a1a


a1b: $(PY)/a1b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/a1b.py > $(CS)/scoa1b.sco
	$(CS) $(CS)/orc.orc $(CS)/scoa1b.sco -o results/a1b


main_a: $(PY)/main_a.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/main_a.py > $(CS)/scomain_a.sco
	$(CS) $(CS)/orc.orc $(CS)/scomain_a.sco -o results/main_a

main_b: $(PY)/main_b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/main_b.py > $(CS)/scomain_b.sco
	$(CS) $(CS)/orc.orc $(CS)/scomain_b.sco -o results/main_b


ss: $(PY)/ss.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/ss.py > $(CS)/scoss.sco
	$(CS) $(CS)/orc.orc $(CS)/scoss.sco -o results/ss


climax: $(PY)/climax.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/climax.py > $(CS)/scoclimax.sco
	$(CS) $(CS)/orc.orc $(CS)/scoclimax.sco -o results/climax
