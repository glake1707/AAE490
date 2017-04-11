#!/bin/bash

echo "starting relay...\n"
python /home/DBT490/AAE490/relay.py
echo "resetting relay...\n"
python /home/DBT490/AAE490/relayReset.py
echo "relay off\n"
