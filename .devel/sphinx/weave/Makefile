# Copyright (c) 2015-2022, Marek Gagolewski <https://www.gagolewski.com>

FILES_RMD = \
	clustbench-usage.Rmd \
	internal-validity-measures.Rmd \
	external-validity-measures.Rmd \
	data-v1.Rmd \
	file-format.Rmd \
	how-to-access.Rmd \
	many-partitions.Rmd \
	noise-points.Rmd \
	true-vs-predicted.Rmd

RMD_MD_OUTPUTS=$(patsubst %.Rmd,%.md,$(FILES_RMD))
#RMD_RST_OUTPUTS=$(patsubst %.Rmd,%.rst,$(FILES_RMD))

%.md: %.Rmd
	./Rmd2md.sh "$<"

all : rmd

rmd : $(RMD_MD_OUTPUTS)
