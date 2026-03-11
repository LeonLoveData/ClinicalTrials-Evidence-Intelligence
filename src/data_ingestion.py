import os
import re
import random
import numpy as np
import pandas as pd

DATA_PATH = "data/raw/clinicaltrials_real_data.csv"
FIG_DIR = "figures"
RANDOM_SEED = 42

os.makedirs(FIG_DIR, exist_ok=True)
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_text(text: str) -> str:
    if pd.isna(text):
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()

def extract_year(date_str):
    if pd.isna(date_str):
        return None
    try:
        return int(str(date_str).split("-")[0])
    except:
        return None
