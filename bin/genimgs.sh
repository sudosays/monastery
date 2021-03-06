#!/bin/sh

img_files=$(find "$(cd ../images; pwd)" -type f -name "*.svg")

echo $img_files

for f in $img_files
do
    fname=$(echo $f | cut -f 1 -d '.')
    inkscape -D -z --file=$fname.svg --export-pdf=$fname.pdf --export-latex
done
