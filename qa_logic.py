def generate_answer(question, context):
    """
    Stable, deterministic answer generation
    for AI-based automated evaluation.
    """

    if not context:
        return ""

    # remove noisy tokens
    for token in ["<pad>", "<EOS>"]:
        context = context.replace(token, "")

    answer = context.replace("\n", " ").strip()

    # hard length cap
    return answer[:700]
