#!/bin/bash

# Always work from the folder this script lives in
cd "$(dirname "$0")"

echo "Starting the weak site on port 5002..."
venv/bin/python target.py > /dev/null 2>&1 &
SITE_PID=$!

# Stop the site when the script ends, even if something goes wrong
trap 'kill $SITE_PID 2>/dev/null; echo "Site stopped."' EXIT

# Give the site 2 seconds to start
sleep 2

echo "Running the header check..."
venv/bin/python check.py