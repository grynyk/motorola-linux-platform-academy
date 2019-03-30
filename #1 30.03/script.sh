#!/bin/bash

text="test text";

echo $text;

echo $0;
echo $1;
echo $2;
echo $#;
echo $@;

katalog=$(pwd);
echo "jestem w katalogu $katalog";
