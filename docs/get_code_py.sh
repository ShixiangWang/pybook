#!/usr/bin/env bash

mkdir -p code_py

for i in `ls *.md | xargs -n 1 | grep "[01][0-9]"`
do
    echo 
    echo "File $i"
    echo 
    sed -n '/```python/,/```/ p' < $i | sed '/```/d' | sed 's/Out/# Out/' > "code_py/"$(echo $i | sed 's/.md//')".py"
    echo "=========="
done


## Clean one by one
## ((In)|(Out)) ?\[[0-9]+\]: ?
## In ?\[[0-9]+\]: ?