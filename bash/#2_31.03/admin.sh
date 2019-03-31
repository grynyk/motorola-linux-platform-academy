#!/bin/bash

working_dir="/home";
user_name="root";


options=("Wyszukaj pliki po rozmiarze" "Wyszukaj pliki po nazwie uzytkownika" \
"Zmien katalog roboczy" "Drop cache" "Wyjdz");

select opt in "${options[@]}" ; do
	case "$opt" in 
        	"Wyszukaj pliki po rozmiarze")
			 echo "${options[0]}"
		;;

        	"Wyszukaj pliki po nazwie uzytkownika")

			read -p	"Podaj nazwe uzytkownika [$user_name]:"	new_user_name
                        if [ -n "$new_user_name" ] ; then
				if id -u "$new_user_name" 1>/dev/null 2>&1  ; then
                                	user_name="$new_user_name"
                        	else
                                	echo "Nie ma takiego uzytkownika . . ."
					echo
					continue;
				fi
                        fi 
			file_list=$(find "$working_dir" -type f ! -iname ".*" ! -path "/proc/*" ! -path "/syst/*" -user "$user_name" 2>/dev/null)
                        if [ -z $file_list  ] ; then
                        	echo "nie znaleziono plikow . . .";
                                echo
                        else
                                echo "lista znalezionych plikow: ";
                               	for file_name in "$file_list" ; do
                        		echo "$file_name"
                        	done
                        fi

		;;

		"Zmien katalog roboczy")
			read -p "Podaj nazwe katalogu [$working_dir]:" new_working_dir
		if [ -n "$new_working_dir" ] ; then
			if [ -d "$new_working_dir" ] ; then
				working_dir="$new_working_dir"
				$(cd $new_working_dir && pwd);
				
				echo "katalog zostal zmieniony . . ."
				echo "$(pwd)"
			else
				echo "Nie istnieje takiego katalogu . . ."
				echo
			fi

		else
			echo "Nie podano katalogu . . ."
		fi
		;;
		"Drop cache")
			sudo sysctl vm.drop_caches=3;
			echo "Cache zostal wyczyszczony . . ."
		;;
		
		"Wyjdz") 
			exit  
		;;

		*) echo "Wybierz opcje od 1 do 5";;
	esac
done

