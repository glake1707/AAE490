#!/bin/bash

X=0
while [ $X -lt 5 ]; do
	python /home/DBT490/AAE490/relay.py &
	python /home/DBT490/AAE490/relayReset.py &
	python /home/DBT490/AAE490/top_block.py &
	sleep 10 
	let X=X+1
done
