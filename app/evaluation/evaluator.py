from .dataset import evaluation_dataset


def evaluate_answer(answer: str, expected: str) -> bool:

    answer = answer.lower()
    expected = expected.lower()

    important_words = [
        word.strip(".,!?")
        for word in expected.split()
        if len(word) > 4
    ]

    matched_words = 0

    for word in important_words:
        if word in answer:
            matched_words += 1

    if not important_words:
        return False

    score = matched_words / len(important_words)

    return score >= 0.5


def run_evaluation(answer_function):

    results = []

    for item in evaluation_dataset:

        question = item["question"]
        expected = item["expected"]

        answer = answer_function(question)

        passed = evaluate_answer(
            answer,
            expected
        )

        results.append({
            "question": question,
            "expected": expected,
            "answer": answer,
            "passed": passed
        })

    return results