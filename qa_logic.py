def generate_answer(question, context):
    """
    Generates a stable, deterministic answer from retrieved context.

    Design goals:
    - No randomness
    - No external API calls
    - No heavy models
    - Automation-friendly output
    """

    if not context:
        return ""

    # Clean whitespace
    answer = context.replace("\n", " ").strip()

    # Hard length cap (important for automated evaluation)
    MAX_LEN = 600
    if len(answer) > MAX_LEN:
        answer = answer[:MAX_LEN]

    return answer
def generate_answer(question, context):
    answer = ""

    if question.lower() in context.lower():
        answer = context
    else:
        answer = context[:300]


    return answer.strip()[:300]
