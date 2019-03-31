a="rower";
echo $a;
echo "to jest $a";
echo "to jest ${a}ek"

echo ${b:=rolki}
echo $b

#Test czy zostal podany argument

arg=${1:?Nie podano argumentu}
echo $arg;
