#!/bin/bash

dir_name=$1

if [ ! -d "$dir_name" ] ; then
	echo "Tworze katalog";
	mkdir "$dir_name";	
else
	echo "Katalog juz istnieje";
fi

if [ 1 -lt 2 ] ; then
	echo "true";
elif [ true ] ; then
	echo "elif then";
else
	echo "else";
fi
