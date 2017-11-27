#!/bin/bash
clear
for NUM in {1..3}
do
	file_name=tsp_example_${NUM}.txt
	python ./tsp-verifier.py $file_name ${file_name}.tour
done
for NUM in {2..8}
do
	file_name=test-input-${NUM}.txt
	python ./tsp-verifier.py $file_name ${file_name}.tour
done