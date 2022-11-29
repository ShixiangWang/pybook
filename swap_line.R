#!/usr/bin/env Rscript
args = commandArgs(trailingOnly = TRUE)
l1 = as.integer(args[1])
l2 = as.integer(args[2])
file = args[3]
dt = data.table::fread(file, header = FALSE)

swap <- function(x,i,j) {x[c(i,j)] <- x[c(j,i)]; x} 
data.table::fwrite(dt[swap(1:nrow(dt), l1, l2)], file = file, quote = FALSE, row.names = FALSE, col.names = FALSE)
