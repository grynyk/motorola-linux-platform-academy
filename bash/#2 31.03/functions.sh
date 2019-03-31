#!/bin/bash

random-string(){
	cat /dev/urandom | tr -dc ${1:?nie podano regex} | fold -w ${2:-10} | head -n 1
}

random-string 0-9 20
