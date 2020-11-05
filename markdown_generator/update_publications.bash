#! /bin/bash

force=1
source="_publications"
dest="/Users/barrault/Sites/loicbarrault.git/_publications"


for file in `ls $source/`
do
	echo "Processing $file"
	if [ ! -e $dest/$file ] || [ $force = 1 ]; then
		echo "copying $file"
		cp $source/$file $dest/
	else
		echo "already there, skipping..."
	fi

done





