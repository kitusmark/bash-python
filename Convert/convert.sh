#!/bin/bash

dirImatges=./Images
color=_gris

cd $dirImatges
Imatges=`echo *`

for i in $Imatges; 
    do convert -colorspace gray $i ${i/.jpg/$color.png};
    done

