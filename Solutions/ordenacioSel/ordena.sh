#!/bin/bash

N=$1
export PATH=$PATH":."
if [ $N -gt 0 ];
   then if [ $N -gt 1 ]; then COMANDA="min "; fi
        i=1
        while [ $i -le $(($N-2)) ]; do
           COMANDA=$COMANDA" | min"
           i=$(($i+1))
        done
   else echo "Us "$0" N    on ha de ser N>0"
fi
if [ $N -eq 1 ]
   then COMANDA="presenta"
   elif [ $N -le 0 ]; then COMANDA=""
   else COMANDA=$COMANDA"| presenta"
fi
echo $COMANDA
eval $COMANDA
