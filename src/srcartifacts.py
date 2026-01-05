import os
import json
import joblib

def safe_dump(obj, path):
    """
    Safely persist an artifact to disk.
    - joblib for sklearn objects
    - json for dict-like configs
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if path.endswith(".joblib"):
        joblib.dump(obj, path)
    elif path.endswith(".json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2)
    else:
        raise ValueError(f"Unsupported artifact type for path: {path}")
