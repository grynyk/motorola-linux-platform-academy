#!/bin/bash

echo "podaj numer bramki"
read bramka

case "$bramka" in
	"1") echo "jedynka";;
	"2") echo "dwojka";;
	"3") echo "trojka";;
	*) echo "Niedobra bramka;;
esac
