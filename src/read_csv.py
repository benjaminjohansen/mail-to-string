import polars as pl

file_path = "data/Deltagere - 361222.csv"

# You can use file on mac/linux to find the correct encoding
participants = pl.read_csv(file_path, encoding="8859", separator=";")

emails = list(participants["Email"])

[print(f"{mail}; ") for mail in emails]

def find_duplicates(files:list, columns:list=["Email"])->list:
    """Find participants who participated in multiple events based on selected column(s). Can be combined multiple times to do lookups across multiple columns.

    Args:
        files (list): list containing file paths to relevant files.

    Returns:
        list: Returns a list with the unique duplicates. Can easily be count
    """

    df_all = pl.DataFrame()
    
    if len(files) > 1:
        for file in files:
            df = pl.read_csv(file,encoding="8859", separator=";" )

            df_all = pl.union([df_all, df])
    else:
        df_all =pl.read_csv(files[0],encoding="8859", separator=";" ) 

    # find duplicates
    n_duplicates =df_all.select(pl.col(columns)).unique().height
    print(n_duplicates)

find_duplicates([file_path])