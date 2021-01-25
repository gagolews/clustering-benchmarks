#!/bin/bash

# Copyleft (C) 2018-2021 Marek Gagolewski <https://www.gagolewski.com>

batteries="fcps graves other sipu uci wut mnist h2mg g2mg"
for b in $batteries; do
    ./catalogue_generate.py $b
    pandoc catalogue/$b.md --to html -o catalogue/$b.html
done
