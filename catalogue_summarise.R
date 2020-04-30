#!/usr/bin/env Rscript

# Summarise the list of the Clustering Datasets as provided
# in the catalogue/*.csv files
# Copyright (C) 2018-2020 Marek.Gagolewski.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

library("stringi")
file_names <- list.files("catalogue", glob2rx("*.csv"), full.names=TRUE)
file_names <- file_names[!stri_detect_regex(file_names, "[hg]2mg")]
#file_names <- "catalogue/g2mg.csv"
x <- lapply(file_names, function(file_name)
    unique(read.csv(file_name)[,c("dataset", "n", "d")]))
x <- do.call(rbind, x)
row.names(x) <- NULL
knitr::kable(x, format="markdown", row.names=TRUE)
