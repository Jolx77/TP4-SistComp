#!/bin/bash

# List all loaded modules
lsmod | awk 'NR>1 {print $1}' > loaded_modules.txt