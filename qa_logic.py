def generate_answer(question, context):
    answer = ""

    if question.lower() in context.lower():
        answer = context
    else:
        answer = context[:300]

    return answer.strip()[:300]