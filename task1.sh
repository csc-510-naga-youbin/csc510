#!/bin/bash

# Find the process ID (PID) of the running infinite.sh script
# ps aux to monitor running process
# grep to filter the infinite.sh file which run infinitely in the background
# grep -v to invert its output
# awk to manipulate data
PID=$(ps aux | grep infinite.sh | grep -v grep | awk '{print $2}')

# Check if PID is not empty
if [ -n "$PID" ]; then
  # Kill the process
  kill -9 $PID
  echo "Process infinite.sh with PID $PID has been killed."
else
  echo "No running process found for infinite.sh."
fi
