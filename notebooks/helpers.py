import pandas as pd

def missing_summary(df):
    summary = pd.DataFrame({
        "dtype": df.dtypes,
        "missing_count": df.isna().sum(),
        "missing_pct": df.isna().mean() * 100,
        "unique_values": df.nunique(),
    })

    return summary.sort_values("missing_pct", ascending=False)