# Package initializer
# Central place to keep column names consistent
TIME_COL = "time"
EVENT_COL = "event"

import pandas as pd

def check_required_columns(df: pd.DataFrame, required: list[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
      
import pandas as pd

def basic_preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Keep this minimal; expand later
    return df.copy()
