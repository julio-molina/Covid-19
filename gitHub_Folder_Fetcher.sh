#! /bin/bash

year=2020
if [ $year -le 2021 ]
then
	month=01
	let "month++"
	echo $month
fi
