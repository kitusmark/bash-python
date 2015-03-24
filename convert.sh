!/bin/bash

dirImatges=~/Escriptori/Conversio/ImatgesProva
afegir=gris

cd $dirImatges
Imatges=`echo *`

for i in $Imatges; 
    do convert -colorspace gray $i ${i/.jpg/_gris.png};
    done

