import polars as pl

file_path = "data/Deltagere - 361222.csv"

# You can use file on mac/linux to find the correct encoding
participants = pl.read_csv(file_path, encoding="8859", separator=";")

emails = list(participants["Email"])

[print(f"{mail}; ") for mail in emails]