#!/bin/bash
mrxdir=$1
cd $mrxdir

#source ~/.bashrc
#conda activate vips

shopt -s globstar
for i in **/*.mrxs*; 
do
	echo $i
	drop=${i%.*}'.tiff'
	echo $drop
	#vips openslideload $i $drop[tile,compression=lzw] --autocrop=true 
done

