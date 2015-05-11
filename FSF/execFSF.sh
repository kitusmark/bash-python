#!/bin/bash
# Cerca el string de "Free Software Foundation" en els executables 
# del directori $1

directori=$1

fstring="Free Software Foundation"

for fitxer in $( find $directori -type f -executable -name '*' | sort )
do
  if (strings -f $fitxer | grep "$fstring" > /dev/null)
     then 
        echo ` basename $fitxer` és de FSF
  fi
done  

exit $?

