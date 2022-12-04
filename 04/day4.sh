#!/bin/bash

input_file="input.txt"

# Star 1: fully enclosed ranges
counter=0
while IFS='-,' read -r a b c d
do
    if [[ $a -le $c && $b -ge $d ]] || [[ $c -le $a && $d -ge $b ]]
    then
        echo "$a $b $c $d"
        ((counter++))
    fi
done < "$input_file"
echo "$counter"
