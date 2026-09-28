from app.evaluation.evaluator import run_evaluation
from app.langchain_module.chains import ask_question


def test_evaluation():

    results = run_evaluation(
        ask_question
    )

    passed = 0
    failed = 0

    for result in results:

        print("\n" + "=" * 60)

        print("Question:")
        print(result["question"])

        print("\nExpected:")
        print(result["expected"])

        print("\nActual:")
        print(result["answer"])

        if result["passed"]:
            print("\nResult: PASS")
            passed += 1

        else:
            print("\nResult: FAIL")
            failed += 1

    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)

    print(f"Total: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")