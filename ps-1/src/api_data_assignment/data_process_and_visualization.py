
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from ..config import OUTPUT_DIR


CSV_URL = (
    "https://raw.githubusercontent.com/ciDSproj/students_scores/"
    "refs/heads/main/Students%20Scores.csv"
)

SCORE_COLUMNS = ["MathScore", "ReadingScore", "WritingScore"]


def fetch_student_scores(url: str = CSV_URL) -> pd.DataFrame:
    response = pd.read_csv(url)
    return response


def calculate_average_scores(dataframe: pd.DataFrame) -> dict[str, float]:
    numeric_scores = dataframe[SCORE_COLUMNS].apply(
        pd.to_numeric,
        errors="coerce"
    )

    average_scores = {}

    for column in SCORE_COLUMNS:
        average_scores[column] = numeric_scores[column].mean()

    return average_scores


def create_bar_chart(
    average_scores: dict[str, float],
    output_path: Path | None = None
) -> Path:

    if output_path is None:
        output_path = OUTPUT_DIR / "average_student_scores.png"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    subjects = [
        column.replace("Score", "")
        for column in average_scores.keys()
    ]

    scores = list(average_scores.values())

    figure, axis = plt.subplots(figsize=(8, 5))

    bars = axis.bar(
        subjects,
        scores,
        color=["blue", "orange", "green"]
    )

    axis.set_title("Average Student Scores by Subject")
    axis.set_xlabel("Subject")
    axis.set_ylabel("Average Score")
    axis.set_ylim(0, 100)

    for bar, score in zip(bars, scores):
        if pd.notna(score):
            axis.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1,
                f"{score:.2f}",
                ha="center",
                va="bottom"
            )

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path


def process_and_visualize_scores() -> tuple[
    pd.DataFrame,
    dict[str, float],
    Path
]:
    dataframe = fetch_student_scores()

    average_scores = calculate_average_scores(dataframe)

    chart_path = create_bar_chart(average_scores)

    return dataframe, average_scores, chart_path
