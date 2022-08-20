# Copyleft (C) 2020-2022, Marek Gagolewski <https://www.gagolewski.com>

.PHONY: python check test sphinx docs clean

.NOTPARALLEL: python test clean purge sphinx docs

PKGNAME="clustering-benchmarks"

all: python

################################################################################

python:
	#python3 setup.py install --user
	python3 -m pip install .

test: python
	pytest
	cd .devel/sphinx && make doctest && cd ../../

check: python
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics \
		--exclude=.devel,build,data,docs,.git,R,dist,clustering_benchmarks.egg-info,man,tutorials
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 \
		--statistics  \
		--exclude=.devel,build,data,docs,.git,R,dist,clustering_benchmarks.egg-info,man,tutorials \
		--ignore=E121,E123,E126,E226,E24,E704,W503,W504,E221,E303,E265

################################################################################

weave:
	cd .devel/sphinx/weave && make && cd ../../../

news:
	cd .devel/sphinx && cp ../../NEWS news.md

html: python news weave
	rm -rf .devel/sphinx/_build/
	cd .devel/sphinx && make html
	.devel/sphinx/fix-html.sh .devel/sphinx/_build/html/weave/
	@echo "*** Browse at"\
	    "file://`pwd`/.devel/sphinx/_build/html/index.html"

docs: html
	rm -rf docs/
	mkdir docs/
	cp -rf .devel/sphinx/_build/html/* docs/
	cp .devel/CNAME.tpl docs/CNAME
	touch docs/.nojekyll
	touch .nojekyll

################################################################################

clean:
	python3 setup.py clean
	rm -rf clustbench/__pycache__/
	rm -rf clustering_benchmarks.egg-info/
	rm -rf dist/
	rm -rf .devel/sphinx/_build/
	rm -rf revdep/

purge: clean
	#rm -f man/*.Rd
