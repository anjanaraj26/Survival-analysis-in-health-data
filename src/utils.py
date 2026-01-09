import pandas as pd

def check_required_columns(df: pd.DataFrame, required: list[str]) -> None:
    """
    Check whether required columns exist in the dataframe.
    """
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
