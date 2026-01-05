import numpy as np
import pandas as pd

def fairness_report(df, group_col, target_cluster):
    """
    Proxy fairness-style report:
    compares cluster membership rates across groups.

    Parameters:
    - df: DataFrame with 'cluster' column
    - group_col: name of grouping column (e.g., cohort, engagement_bin)
    - target_cluster: cluster id (int)

    Returns:
    - DataFrame with rate per group and disparity summary
    """
    out = df.copy()
    out["is_target"] = (out["cluster"] == target_cluster).astype(int)

    grp = out.groupby(group_col)["is_target"].agg(["mean", "count"]).reset_index()
    grp = grp.rename(columns={"mean": "target_rate"})

    # Simple disparity indicators
    min_rate = grp["target_rate"].min()
    max_rate = grp["target_rate"].max()
    grp["rate_diff_vs_min"] = grp["target_rate"] - min_rate
    grp["rate_ratio_vs_min"] = grp["target_rate"] / (min_rate + 1e-9)

    summary = pd.DataFrame(
        {
            "group_col": [group_col],
            "target_cluster": [target_cluster],
            "min_rate": [min_rate],
            "max_rate": [max_rate],
            "max_minus_min": [max_rate - min_rate],
            "max_div_min": [max_rate / (min_rate + 1e-9)],
        }
    )

    return grp, summary
