#! /bin/bash

test_num=1


while [ $test_num -le 6  ]
do
	cp plantilla.py test_$test_num.py
	punto_num=$(( $test_num + 1 ))
done

