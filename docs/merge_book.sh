ls *.md | xargs -n 1 | grep "[01]" > tmp_list
Rscript swap_line.R 1 2 tmp_list
cat `cat tmp_list` > interactive_python.md
rm tmp_list
