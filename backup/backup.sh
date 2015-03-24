#!/bin/bash
export MAILTO="root"
usuari=root
home=/root
dirBackup=/backup

arxiuBackup=$dirBackup/bck$(date +%Y%m%d%I%M%S).tgz
guarda=3
tar -zcf $arxiuBackup $home
echo Backup $arxiuBackup finalitzat
quants=$(ls -t $dirBackup/bck*.tgz | wc -l )

num=$(($quants-$guarda))
echo $quants $num
if [$num -gt 0]
    then l=$(ls -t $dirBackup/"bck*.tgz" | tail -n $num)
; echo esborrant $l ; "\rm" -f $l
fi