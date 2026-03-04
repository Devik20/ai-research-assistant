from metadata import extract_metadata
from scorer import evaluate_paper


def run_full_evaluation(full_text, first_pages_text):
    metadata = extract_metadata(first_pages_text)
    scoring_report = evaluate_paper(full_text)

    return {
        "metadata": metadata,
        "scoring": scoring_report
    }