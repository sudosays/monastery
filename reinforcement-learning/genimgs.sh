#!/bin/sh

cd images

for f in $(ls)
do
    fname=$(echo $f | cut -f1 -d'.')
    inkscape -D -z --file=$fname.svg --export-pdf=$fname.pdf --export-latex
done
