#!/usr/bin/env bash

mkdir -p code

for i in `ls *.md | xargs -n 1 | grep "[01][0-9]"`
do
    echo 
    echo "File $i"
    echo 
    sed -n '/```/,/```/ p' < $i > "code/"$(echo $i | sed 's/.md//')".txt"
    echo "=========="
done


## get rid of ```
## sed -n '/^```/,/^```/p' < input.file | sed '/^```/d'