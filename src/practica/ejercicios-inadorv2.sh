#! /bin/bash

punto_num=3


while [ $punto_num -le 6  ]
do
	cp plantilla.py ejercicio$punto_num.py
	punto_num=$(( $punto_num + 1 ))
done

