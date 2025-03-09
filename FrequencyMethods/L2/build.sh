#!/usr/bin/env bash

# Get location of this file
projRoot=$(dirname $(realpath $0))

# Run jupyter notebook to generate figures
jupyter nbconvert --to notebook --execute --inplace $projRoot/python/notebook.ipynb

# Compile typst report to pdf
typst compile --root $projRoot $projRoot/report/report.typ $projRoot/report/report.pdf