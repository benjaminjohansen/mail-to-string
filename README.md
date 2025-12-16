# Read CSV files with participants and split them for mail forwarding

## Introduction

These few lines of code will help extract all email adresses from a CSV file. This is particular useful for volunteers in [IDA](https://ida.dk/).
As these files have a strange encoding.

## Getting started

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/). Check uv is installed with `uv` in your terminal
2. Add a data directory `data` and upload data. This directory is ignored by .gitignore
3. Check the encoding of your csv file. On unix systems you can use `file data/DATA_FILE_NAME` - replace DATA_FILE_NAME with the actual name
4. Update the encoding variable in the `src/read_csv.py` script
5. Run the script with `uv run src/read_csv.py`. On mac you can copy to clipboard by `uv run src/read_csv-py | pbcopy` on Linux you can `uv run src/read_csv.py | xclip -selection clipboard`
