#!/bin/zsh

LN='wc -l 1-1.txt'
file=./1-1.txt

FI="${mapfile[$file]}"


for x in $LN
do
	a=${FI[$x]}
	echo "a = $a"
	x=x+1
	for y in $LN
	do
		b=${FI[$y]}
		echo "b = $b"
		if [ $a+$b  == 2020 ]
		then
			echo "a = $a, b = $b"
			c=$a*$b
			echo "c = $c"
		fi
		y=y+1
	done
done
