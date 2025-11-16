import polars as pl

file_path = "data/Deltagere - 361222.csv"

# You can use file on mac/linux to find the correct encoding
participants = pl.read_csv(file_path, encoding="8859", separator=";")

emails = list(participants["Email"])

# [print(f"{mail}; ") for mail in emails]


def find_duplicates(files: list, columns: list = ["Email"]) -> list:
    """Find participants who participated in multiple events based on selected column(s). Can be combined multiple times to do lookups across multiple columns.

    Args:
        files (list): list containing file paths to relevant files.

    Returns:
        list: Returns a list with the unique duplicates. Can easily be count
    """

    df_all = []

    if len(files) > 1:
        for file in files:
            df = (
                pl.read_csv(file, encoding="8859", separator=";", skip_rows=1)
                .select(
                    ["Email", "Antal", "Tilmeldingstidspunkt", "Afmeldingstidspunkt"]
                )
                .filter(pl.col("Afmeldingstidspunkt").is_null())
            )
            df_all.append(df)

    else:
        df_all = pl.read_csv(files[0], encoding="8859", separator=";", skip_rows=1)

    # find duplicates
    df_final = pl.concat(df_all)
    n_duplicates = (
        df_final.select(pl.col("Email"))
        .filter(pl.col("Email").is_duplicated())
        .unique()
    )
    print(n_duplicates.height)


find_duplicates(["data/Deltagere - 361185.csv", "data/Deltagere - 361187.csv"])
