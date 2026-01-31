def generate_answer(question, context):
    if not context:
        return ""

    answer = context.replace("\n", " ").strip()

    # Hard limit for evaluator safety
    return answer[:300]
