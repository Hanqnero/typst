#!/bin/bash

# Check if Jupyter is installed
echo "Checking if 'jupyter' is installed..."
if ! command -v jupyter &> /dev/null; then
    echo "Error: 'jupyter' is not installed or not in PATH. Please install it before running this script."
    exit 1
fi

# Check if jupyter nbconvert is available
echo "Checking if 'jupyter nbconvert' is available..."
if ! jupyter nbconvert --help &> /dev/null; then
    echo "Error: 'jupyter nbconvert' is not available. Please install it with 'pip install nbconvert'."
    exit 1
fi

# Get the absolute path of the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Define paths relative to script directory
REPORT_SOURCE   ="${SCRIPT_DIR}/report/report.typ"
REPORT_OUTPUT   ="${SCRIPT_DIR}/report.pdf"
NOTEBOOK_PATH   ="${SCRIPT_DIR}/python/notebook.ipynb"
SPLITTER_SCRIPT ="${SCRIPT_DIR}/process_notebook.py"

# Split notebook to cells
rm -fr $(dirname $SCRIPT_DIR)/cells && mkdir -p {$SCRIPT_DIR}/python/cells
python3 $SPLITTER_SCRIPT "$NOTEBOOK_PATH" "${SCRIPT_DIR}/python/cells"

if [ "$1" == "--execute" ]; then
    echo "Executing Jupyter notebook..."
    jupyter nbconvert --to notebook --execute "$NOTEBOOK_PATH" --inplace
else
    echo "Skipping notebook execution. Use '--execute' flag to execute the notebook."

echo "Checking if 'typst' is installed..."
if ! command -v typst &> /dev/null; then
    echo "Error: 'typst' is not installed or not in PATH. Please install it before running this script."
    exit 1
fi

# Generate the PDF report
echo "Generating PDF report..."
typst compile --root "$SCRIPT_DIR" "$REPORT_SOURCE" "$REPORT_OUTPUT"

touch "${SCRIPT_DIR}/python/cells/last_cell.txt"
ls -l ${SCRIPT_DIR}/python/cells | wc -n > "${SCRIPT_DIR}/python/cells/last_cell.txt" 

echo "Done! Report generated at $REPORT_OUTPUT"
