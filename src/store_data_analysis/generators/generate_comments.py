from store_data_analysis.config import COMMENTS_FILE


def generate_comments():
    comments = [
        "La atención fue excelente y el proceso fue muy sencillo.",
        "El pedido llegó en buenas condiciones.",
        "El servicio al cliente fue muy bueno.",
        "La entrega fue rápida y sin problemas.",
        "La atención del personal fue excelente.",
        "El pedido tardó demasiado en llegar.",
        "La entrega tuvo un retraso considerable.",
        "El pedido llegó más tarde de lo esperado.",
        "La atención al cliente fue muy lenta.",
        "El proceso de entrega fue demasiado tardado.",
        "El servicio fue profesional y eficiente.",
        "La compra fue sencilla y rápida.",
    ]

    COMMENTS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    COMMENTS_FILE.write_text(
        "\n".join(comments) + "\n",
        encoding="utf-8",
    )
