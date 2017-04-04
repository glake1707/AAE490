#!/bin/bash

echo "starting relay..."
python relay.py
echo "resetting relay..."
python relayReset.py
