# Copyright (c) 2015-2023, Marek Gagolewski <https://www.gagolewski.com>

FILES_RMD = \
	clustbench-usage.Rmd \
	internal-validity-measures.Rmd \
	external-validity-measures.Rmd \
	suite-v1.Rmd \
	data-v1.Rmd \
	results-v1.Rmd \
	file-format.Rmd \
	how-to-access.Rmd \
	many-partitions.Rmd \
	noise-points.Rmd \
	contributing.Rmd \
	colouriser.Rmd \
	true-vs-predicted.Rmd

RMD_MD_OUTPUTS=$(patsubst %.Rmd,%.md,$(FILES_RMD))
#RMD_RST_OUTPUTS=$(patsubst %.Rmd,%.rst,$(FILES_RMD))

%.md: %.Rmd
	./Rmd2md.sh "$<"

all : rmd

rmd : $(RMD_MD_OUTPUTS)

clean:
	rm -f $(RMD_MD_OUTPUTS)
