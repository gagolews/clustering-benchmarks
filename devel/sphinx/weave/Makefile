# Copyright (c) 2015-2022, Marek Gagolewski <https://www.gagolewski.com>

FILES_RMD = \
	example.Rmd

RMD_MD_OUTPUTS=$(patsubst %.Rmd,%.md,$(FILES_RMD))
#RMD_RST_OUTPUTS=$(patsubst %.Rmd,%.rst,$(FILES_RMD))

%.md: %.Rmd
	Rscript -e 'knitr::knit("$<", "$@")'

all : rmd

rmd : $(RMD_MD_OUTPUTS)
