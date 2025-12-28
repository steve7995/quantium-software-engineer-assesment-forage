#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
source venv/Scripts/activate

# Run test suite in headless mode
pytest --headless
