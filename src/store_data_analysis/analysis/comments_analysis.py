POSITIVE_WORDS = [
    "excelente",
    "bueno",
    "buena",
    "buenas",
    "buen",
    "sencillo",
    "sencilla",
    "rápido",
    "rápida",
    "profesional",
    "eficiente",
]

NEGATIVE_WORDS = [
    "lento",
    "lenta",
    "tardó",
    "tardado",
    "tardada",
    "tarde",
    "retraso",
    "retrasado",
    "deficiente",
    "dañado",
    "dañada",
]


def classify_comment(comment):
    text = comment.lower()

    positive_score = sum(
        word in text
        for word in POSITIVE_WORDS
    )

    negative_score = sum(
        word in text
        for word in NEGATIVE_WORDS
    )

    if positive_score > negative_score:
        return "Positive"

    if negative_score > positive_score:
        return "Negative"

    return "Neutral"


def classify_comments(comments):
    return [
        {
            "comment": comment,
            "classification": classify_comment(comment),
        }
        for comment in comments
    ]


def get_comment_counts(classified_comments):
    positive = sum(
        item["classification"] == "Positive"
        for item in classified_comments
    )

    negative = sum(
        item["classification"] == "Negative"
        for item in classified_comments
    )

    neutral = sum(
        item["classification"] == "Neutral"
        for item in classified_comments
    )

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
    }


def get_comment_percentages(classified_comments):
    counts = get_comment_counts(
        classified_comments
    )

    total = len(classified_comments)

    if total == 0:
        return {
            "positive": 0,
            "negative": 0,
            "neutral": 0,
        }

    return {
        "positive": counts["positive"] / total * 100,
        "negative": counts["negative"] / total * 100,
        "neutral": counts["neutral"] / total * 100,
    }


def get_most_common_problem(comments):
    problems = {
        "delivery_delay": [
            "tardó",
            "tardado",
            "tardada",
            "tarde",
            "retraso",
            "lento",
        ],
        "customer_service": [
            "deficiente",
            "atención lenta",
        ],
        "damaged_product": [
            "dañado",
            "dañada",
        ],
    }

    counts = {
        problem: 0
        for problem in problems
    }

    for comment in comments:
        text = comment.lower()

        for problem, keywords in problems.items():
            if any(
                keyword in text
                for keyword in keywords
            ):
                counts[problem] += 1

    return max(
        counts,
        key=counts.get,
    )
