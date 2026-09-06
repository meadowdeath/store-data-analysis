from store_data_analysis.analysis.comments_analysis import (
    classify_comment,
    classify_comments,
    get_comment_counts,
    get_comment_percentages,
)


def test_classify_positive_comment():
    result = classify_comment(
        "La atención fue excelente."
    )

    assert result == "Positive"


def test_classify_negative_comment():
    result = classify_comment(
        "El pedido llegó tarde."
    )

    assert result == "Negative"


def test_comment_counts():
    comments = [
        "La atención fue excelente.",
        "El pedido llegó tarde.",
    ]

    classified = classify_comments(comments)

    counts = get_comment_counts(classified)

    assert counts["positive"] == 1
    assert counts["negative"] == 1


def test_comment_percentages():
    comments = [
        "La atención fue excelente.",
        "El pedido llegó tarde.",
    ]

    classified = classify_comments(comments)

    percentages = get_comment_percentages(
        classified
    )

    assert percentages["positive"] == 50
    assert percentages["negative"] == 50