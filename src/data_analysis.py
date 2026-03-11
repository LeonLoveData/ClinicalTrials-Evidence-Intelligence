import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sentence_transformers import SentenceTransformer, util
from data_process import clean_text, extract_year, FIG_DIR

class TrialEmbeddingSearch:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        texts = []
        for _, row in df.iterrows():
            text = f"{clean_text(row['conditions'])}. {clean_text(row['interventions'])}"
            texts.append(text)
        self.df["embedding_text"] = texts
        self.embeddings = self.model.encode(texts, convert_to_tensor=True, show_progress_bar=True)

    def search(self, query: str, top_k: int = 5) -> pd.DataFrame:
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_emb, self.embeddings)[0]
        scores_np = scores.cpu().numpy()
        idx = np.argpartition(-scores_np, top_k)[:top_k]
        idx = idx[np.argsort(-scores_np[idx])]
        results = self.df.iloc[idx].copy()
        results["similarity"] = scores_np[idx]
        return results

def trial_trend_analysis(df: pd.DataFrame):
    df["start_year"] = df["start_date"].apply(extract_year)
    trend = (
        df.groupby("start_year")["nct_id"]
        .count()
        .reset_index()
        .rename(columns={"nct_id": "trial_count"})
    )
    return trend

def create_pseudo_labels(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["enrollment"] = pd.to_numeric(df["enrollment"], errors="coerce").fillna(0)
    df["has_primary"] = df["primary_outcomes"].notna().astype(int)
    df["is_interventional"] = (df["study_type"] == "Interventional").astype(int)
    score = (
        (df["enrollment"] > df["enrollment"].median()).astype(int)
        + df["has_primary"]
        + df["is_interventional"]
    )
    df["include_label"] = (score >= 2).astype(int)
    return df

def train_inclusion_model(df: pd.DataFrame):
    df = create_pseudo_labels(df)
    X = df[["enrollment", "has_primary", "is_interventional"]]
    y = df["include_label"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return model, scaler, cm, report

def evidence_gap_analysis(df: pd.DataFrame):
    df["enrollment"] = pd.to_numeric(df["enrollment"], errors="coerce")
    gap_df = (
        df.groupby("conditions")["enrollment"]
        .median()
        .sort_values()
        .head(10)
    )
    return gap_df
