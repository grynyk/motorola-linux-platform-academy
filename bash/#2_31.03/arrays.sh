#!/bin/bash

tablica=(ala ma kota);
echo ${tablica[2]};
tablica[2]="pet"
echo ${tablica[@]}

tab2=("${tablica[@]:0:2}" "trzeci" "${tablica[@]:2}")
echo $tab2;

for i in ${tablica[@]} ; do
	echo "$i"
done
