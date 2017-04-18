#!/bin/bash

X=0
while [ $X -lt 1 ]; do
	python /home/DBT490/AAE490/relay.py &                 # run data collection programs
	python /home/DBT490/AAE490/top_block.py &
	sleep 20                                    # wait for the data collection to finish, should be (data collection timer time) + 4 sec minimum 
	python /home/DBT490/AAE490/relayReset.py &
	let X=X+1
done
