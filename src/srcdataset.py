import os
import pandas as pd

def extract_primary_tag(tag_str: str) -> str:
    """
    Extract primary tag from Stack Exchange tag format like: |python|pandas|
    Returns 'unknown' if missing/unparseable.
    """
    if not isinstance(tag_str, str) or tag_str.strip() == "":
        return "unknown"
    parts = [t for t in tag_str.split("|") if t.strip()]
    return parts[0] if parts else "unknown"

def primary_tag(tags):
    """
    Same intent as notebook: derive a primary tag label.
    Kept for compatibility with notebook naming.
    """
    return extract_primary_tag(tags)

def build_working_dataset() -> pd.DataFrame:
    """
    Notebook-compatible placeholder.

    In the notebook, build_working_dataset() relied on variables and paths
    already defined in the runtime (parsed posts, constructed Q+A pairs).
    For the repo, we keep the function name but require the caller to pass
    or load the necessary intermediate dataset in the notebook itself.

    Recommended usage:
    - Run the notebook for the full build
    - Use this src module mainly for code organization and reuse
    """
    raise NotImplementedError(
        "This function is notebook-runtime dependent. "
        "Run the notebook to construct the working dataset, "
        "or refactor this function to accept input DataFrames."
    )
