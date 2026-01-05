import pandas as pd
from lxml import etree
from tqdm import tqdm

def parse_posts_xml(xml_path: str, max_rows: int | None = None) -> pd.DataFrame:
    """
    Parse Stack Exchange Posts.xml into a DataFrame.
    Reads <row ... /> entries using streaming iterparse to handle large XML files.

    Parameters
    - xml_path: path to Posts.xml
    - max_rows: optional cap for Colab constraints

    Returns
    - DataFrame of post rows with attributes as columns
    """
    context = etree.iterparse(xml_path, events=("end",), tag="row")
    rows = []

    for _, elem in tqdm(context, desc="Parsing Posts.xml"):
        rows.append(dict(elem.attrib))
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

        if max_rows is not None and len(rows) >= max_rows:
            break

    return pd.DataFrame(rows)
