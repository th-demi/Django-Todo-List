#!/bin/bash

# Ensure python and pip are available
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but it's not installed. Aborting."; exit 1; }
command -v pip3 >/dev/null 2>&1 || { echo >&2 "Pip 3 is required but it's not installed. Aborting."; exit 1; }

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run any additional build steps if needed
# For example, collect static files for Django
python3 manage.py collectstatic --noinput
