#!/bin/bash

echo "deploying..."
mpremote cp config.py :config.py
mpremote cp boot.py :boot.py
mpremote cp main.py :main.py
