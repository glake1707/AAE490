#!/bin/bash

echo "starting relay..."
python /home/DBT490/AAE490/relay.py
echo "resetting relay..."
python /home/DBT490/AAE490/relayReset.py
echo "relay off"
