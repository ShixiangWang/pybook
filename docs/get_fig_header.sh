for i in `ls *.md | xargs -n 1 | grep "[01][0-9]"`
do
    echo 
    echo "File $i"
    echo 
    sed -n '/!\[图.*\]/p' $i
    echo "=========="
done