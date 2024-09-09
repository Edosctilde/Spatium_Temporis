PY = python
CS = csound

all: uno_b uno main_a main_b ss Up

UP: $(PY)/Up.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/Up.py > $(CS)/scoUp.sco
	$(CS) $(CS)/orc.orc $(CS)/scoUp.sco -o results/Up


uno: $(PY)/uno.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/uno.py > $(CS)/scouno.sco
	$(CS) $(CS)/orc.orc $(CS)/scouno.sco -o results/uno


uno_b: $(PY)/uno_b.py $(CS)/orc.orc $(PY)/classi.py $(PY)/cost.py $(PY)/funz.py 
	$(PY)3 $(PY)/uno_b.py > $(CS)/scouno_b.sco
	$(CS) $(CS)/orc.orc $(CS)/scouno_b.sco -o results/uno_b


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
