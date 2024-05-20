#!/bin/bash

# List all available modules
available_modules=$(find /lib/modules/$(uname -r)/kernel/ -type f -name '*.ko' | sed 's/.*\///;s/\.ko//')

# List all loaded modules
loaded_modules=$(lsmod | awk 'NR>1 {print $1}')

# Compare lists and show modules that are available but not loaded
echo "Available but not loaded modules:"
for module in $available_modules; do
  if ! echo "$loaded_modules" | grep -qw "$module"; then
    echo "$module"
  fi
done

