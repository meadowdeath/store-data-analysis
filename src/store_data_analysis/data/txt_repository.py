from store_data_analysis.config import COMMENTS_FILE


def load_comments():
    return COMMENTS_FILE.read_text(
        encoding="utf-8",
    ).splitlines()