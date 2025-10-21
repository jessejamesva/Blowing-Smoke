#!/bin/bash
# Fully portable launcher for Blowing_Smoke

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 [admin|performance|character] [output_file] [num_rows]"
    exit 1
fi

CATEGORY=$1
OUTPUT_FILE=$2
NUM_ROWS=$3

# Resolve real path of the script, follow symlinks
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

PYTHON_SCRIPT="$SCRIPT_DIR/../Blowing_Smoke_pkg/generate_fake_data.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script not found at $PYTHON_SCRIPT"
    exit 1
fi

python3 "$PYTHON_SCRIPT" "$CATEGORY" "$OUTPUT_FILE" "$NUM_ROWS"
