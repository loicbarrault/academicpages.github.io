#! /bin/bash

force=0
if [[ $# -gt 0 ]] && [[  "$1" = "-f" ]] ; then
	force=1
	echo "force!!"
fi

source="_publications"
#dest="/Users/barrault/Sites/loicbarrault.git/_publications"
dest="/Users/loicbarrault/Documents/git/loicbarrault.github.io/_publications"


for file in `ls $source/`
do
	#echo "Processing $file"
	if [ ! -e $dest/$file ] || [ $force -eq 1 ]; then
		echo "copying $file"
		cp $source/$file $dest/
#	else
#		echo "already there, skipping..."
	fi

done





