#!/bin/bash

PIN=1

short='sleep 0.2'
long='sleep 0.5'
ledon='gpio write 1 1'
ledoff='gpio write 1 0'

gpio mode $PIN out

while true
do

for i in {1..3}
do
	echo on
	$ledon
	$short
	echo off
	$ledoff
	$short
done

for i in {1..3}
do
	echo on
	$ledon
	$long
	echo off
	$ledoff
	$long
done

done
