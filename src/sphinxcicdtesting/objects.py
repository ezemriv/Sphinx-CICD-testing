import polars as pl
import pandas as pd

def read_parquet_with_polars(file_path):
    """
    Reads a Parquet file using Polars.

    Args:
        file_path (str): Path to the Parquet file.

    Returns:
        polars.DataFrame: The loaded Polars DataFrame.
    """
    return pl.read_parquet(file_path)

def read_parquet_with_pandas(file_path):
    """
    Reads a Parquet file using Pandas.

    Args:
        file_path (str): Path to the Parquet file.

    Returns:
        pandas.DataFrame: The loaded Pandas DataFrame.
    """
    return pd.read_parquet(file_path)
