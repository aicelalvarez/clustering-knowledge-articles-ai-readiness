import re
import numpy as np
import pandas as pd
from .text_cleaning import strip_html, normalize_ws

def winsorize_series(s, p_low=0.01, p_high=0.99):
    """
    Winsorize numeric series by clipping to [p_low, p_high] quantiles.
    Mirrors notebook logic.
    """
    s = pd.to_numeric(s, errors="coerce")
    lo = s.quantile(p_low)
    hi = s.quantile(p_high)
    return s.clip(lower=lo, upper=hi)

def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add the engineered features exactly as used in the notebook.

    Expected columns:
    - title, question_body, answer_body, tags

    Returns
    - copy of df with engineered fields appended
    """
    work = df.copy()

    # Clean text fields
    work["title_clean"] = work["title"].map(strip_html).map(normalize_ws)
    work["question_clean"] = work["question_body"].map(strip_html).map(normalize_ws)
    work["answer_clean"] = work["answer_body"].map(strip_html).map(normalize_ws)

    work["article_text"] = (
        work["title_clean"] + " " + work["question_clean"] + " " + work["answer_clean"]
    )

    # Structural / clarity proxies
    work["num_words_answer"] = work["answer_clean"].str.split().str.len()
    work["num_words_question"] = work["question_clean"].str.split().str.len()

    # Step / instruction cues
    work["has_numbered_steps"] = (
        work["answer_body"].astype(str)
        .str.contains(r"(\bStep\b|\bstep\b|\d+\.)", regex=True)
        .astype(int)
    )
    work["num_bullets"] = work["answer_body"].astype(str).str.count(r"(<li>|•|\n- |\n\* )")

    # Link/reference signals
    work["num_links"] = work["answer_body"].astype(str).str.count(r"(http://|https://|www\.)")

    # Code heaviness proxy
    work["num_code_blocks"] = work["answer_body"].astype(str).str.count(r"(<pre>|<code>)")
    work["code_ratio_proxy"] = (work["num_code_blocks"] + 1) / (work["num_words_answer"] + 50)

    # Readability proxies
    def _avg_word_len(x: str) -> float:
        words = str(x).split()
        return float(np.mean([len(w) for w in words])) if len(words) else 0.0

    work["avg_word_len_answer"] = work["answer_clean"].apply(_avg_word_len)
    work["num_sentences_answer"] = work["answer_clean"].str.count(r"[.!?]") + 1
    work["words_per_sentence_answer"] = work["num_words_answer"] / work["num_sentences_answer"]

    # Tag count
    work["num_tags"] = work["tags"].astype(str).apply(lambda s: len([t for t in s.split("|") if t.strip()]))

    return work
