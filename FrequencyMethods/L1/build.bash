#!/usr/bin/env bash
projroot=$(dirname $0)

file1="report/sup/list-fourier.typ"
echo "\`\`\`py" | tee $projroot/$file1 > /dev/null
cat $projroot/python/fourier.py | tee -a $projroot/$file1 > /dev/null
echo "\`\`\`" | tee -a $projroot/$file1 > /dev/null

file2="report/sup/list-square.typ"
echo "\`\`\`py" | tee $projroot/$file2 > /dev/null
cat $projroot/python/square_test.py | tee -a $projroot/$file2 > /dev/null
echo "\`\`\`" | tee -a $projroot/$file2 > /dev/null

file3="report/sup/list3.typ"
echo "\`\`\`py" | tee $projroot/$file3 > /dev/null
cat $projroot/python/2.py | tee -a $projroot/$file3 > /dev/null
echo "\`\`\`" | tee -a $projroot/$file3 > /dev/null

typst c --root=. $projroot/report/report.typ $projroot/L1-report.pdf