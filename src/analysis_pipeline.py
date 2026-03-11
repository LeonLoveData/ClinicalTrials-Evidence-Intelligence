from data_ingestion import load_data, DATA_PATH, FIG_DIR
from evidence_extraction import (
    trial_trend,
    TrialEmbeddingSearch,
    train_inclusion_model,
    evidence_gap
)
import matplotlib.pyplot as plt

def plot_trial_trend(trend_df):
    plt.figure(figsize=(7, 4))
    plt.plot(trend_df["start_year"], trend_df["trial_count"], marker="o", color="#4C72B0")
    plt.title("Clinical Trial Count by Start Year")
    plt.xlabel("Start Year")
    plt.ylabel("Number of Trials")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/trial_count_trend.png")
    plt.close()

def plot_embedding_search(results):
    plt.figure(figsize=(6, 4))
    plt.barh(results["nct_id"], results["similarity"], color="#55A868")
    plt.gca().invert_yaxis()
    plt.title("Embedding Search – Top Results")
    plt.xlabel("Similarity Score")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/embedding_search_example.png")
    plt.close()

def plot_inclusion_confusion_matrix(cm):
    plt.figure(figsize=(4, 4))
    plt.imshow(cm, cmap="Blues")
    plt.title("Inclusion Model – Confusion Matrix")
    plt.colorbar()
    plt.xticks([0, 1], ["Pred 0", "Pred 1"])
    plt.yticks([0, 1], ["True 0", "True 1"])
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/inclusion_model_performance.png")
    plt.close()

def plot_evidence_gap(gap_df):
    plt.figure(figsize=(7, 5))
    gap_df.plot(kind="barh", color="#C44E52")
    plt.title("Evidence Gap – Lowest Median Enrollment Conditions")
    plt.xlabel("Median Enrollment")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/evidence_gap_summary.png")
    plt.close()

def main():
    df = load_data(DATA_PATH)

    trend_df = trial_trend(df)
    plot_trial_trend(trend_df)

    search_engine = TrialEmbeddingSearch(df)
    query = "diagnostic accuracy device trials in heart failure"
    results = search_engine.search(query, top_k=5)
    plot_embedding_search(results)

    model, scaler, cm, report = train_inclusion_model(df)
    plot_inclusion_confusion_matrix(cm)

    gap_df = evidence_gap(df)
    plot_evidence_gap(gap_df)

    print("Analysis complete. Figures saved.")

if __name__ == "__main__":
    main()
