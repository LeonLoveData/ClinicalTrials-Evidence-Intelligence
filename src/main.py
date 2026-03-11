from data_process import load_data, DATA_PATH
from data_analysis import (
    trial_trend_analysis,
    TrialEmbeddingSearch,
    train_inclusion_model,
    evidence_gap_analysis
)
from visualization import (
    plot_trial_trend,
    plot_embedding_search,
    plot_inclusion_confusion_matrix,
    plot_evidence_gap
)

def main():
    df = load_data(DATA_PATH)

    trend_df = trial_trend_analysis(df)
    plot_trial_trend(trend_df)

    search_engine = TrialEmbeddingSearch(df)
    query = "diagnostic accuracy device trials in heart failure"
    results = search_engine.search(query, top_k=5)
    plot_embedding_search(results)

    model, scaler, cm, report = train_inclusion_model(df)
    plot_inclusion_confusion_matrix(cm)

    gap_df = evidence_gap_analysis(df)
    plot_evidence_gap(gap_df)

    print("Analysis complete. Figures saved.")

if __name__ == "__main__":
    main()
