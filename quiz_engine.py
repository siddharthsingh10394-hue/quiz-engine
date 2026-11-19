"""
Interactive Quiz Engine (Project B4)
Track: Track B - Python
Description: A console-based interactive multiple-choice quiz engine with robust input validation,
             instant feedback, score tracking, percentage calculation, and built-in unit tests.
"""

import sys
import unittest
from typing import Dict, List, Any


def get_quiz_data() -> List[Dict[str, Any]]:
    """
    Returns the quiz questions dataset.
    Contains 10 curated multiple-choice questions on Python and computer science fundamentals.
    Each item contains the question prompt, four options (A, B, C, D), correct option, and an explanation.
    """
    return [
        {
            "id": 1,
            "question": "What is the primary difference between a Python list and a Python tuple?",
            "options": {
                "A": "Lists are immutable, while tuples are mutable",
                "B": "Lists are mutable, while tuples are immutable",
                "C": "Lists cannot hold heterogeneous data types",
                "D": "Tuples cannot be indexed or sliced",
            },
            "answer": "B",
            "explanation": "Lists can be modified after creation (mutable), whereas tuples cannot be modified once defined (immutable)."
        },
        {
            "id": 2,
            "question": "Which Python built-in function returns both the index and the item during iteration?",
            "options": {
                "A": "zip()",
                "B": "range()",
                "C": "enumerate()",
                "D": "map()",
            },
            "answer": "C",
            "explanation": "enumerate() returns an iterator yielding pairs of (index, item)."
        },
        {
            "id": 3,
            "question": "What is the average time complexity of looking up a key in a Python dictionary?",
            "options": {
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n log n)",
            },
            "answer": "A",
            "explanation": "Python dictionaries are implemented using hash tables, giving average O(1) time complexity for lookups."
        },
        {
            "id": 4,
            "question": "What will be the output of `bool([])` in Python?",
            "options": {
                "A": "True",
                "B": "False",
                "C": "None",
                "D": "TypeError",
            },
            "answer": "B",
            "explanation": "In Python, empty collections (such as empty lists, strings, or sets) evaluate to False in a boolean context."
        },
        {
            "id": 5,
            "question": "Which keyword is used to handle exceptions that occur in a `try` block?",
            "options": {
                "A": "catch",
                "B": "handle",
                "C": "except",
                "D": "error",
            },
            "answer": "C",
            "explanation": "Python uses `try ... except` blocks for exception handling."
        },
        {
            "id": 6,
            "question": "Which of the following data structures operates on a Last-In, First-Out (LIFO) basis?",
            "options": {
                "A": "Queue",
                "B": "Stack",
                "C": "Linked List",
                "D": "Binary Tree",
            },
            "answer": "B",
            "explanation": "A Stack follows the LIFO principle, where the most recently added item is removed first."
        },
        {
            "id": 7,
            "question": "What does the `strip()` method do on a Python string?",
            "options": {
                "A": "Splits the string into words based on spaces",
                "B": "Removes leading and trailing whitespace characters",
                "C": "Reverses the order of characters in the string",
                "D": "Converts all characters to lowercase",
            },
            "answer": "B",
            "explanation": "str.strip() returns a copy of the string with both leading and trailing whitespace characters removed."
        },
        {
            "id": 8,
            "question": "Which operator is used for floor division in Python?",
            "options": {
                "A": "/",
                "B": "%",
                "C": "//",
                "D": "**",
            },
            "answer": "C",
            "explanation": "`//` performs floor division (e.g., 7 // 2 yields 3), whereas `/` performs true float division."
        },
        {
            "id": 9,
            "question": "In Python, which of the following is an immutable sequence data type?",
            "options": {
                "A": "list",
                "B": "set",
                "C": "dict",
                "D": "str",
            },
            "answer": "D",
            "explanation": "Strings (`str`) in Python are immutable; once created, individual characters cannot be changed in-place."
        },
        {
            "id": 10,
            "question": "What is the purpose of the `break` statement in a loop?",
            "options": {
                "A": "Skips the current iteration and moves to the next",
                "B": "Terminates the loop immediately",
                "C": "Restarts the loop from the beginning",
                "D": "Exits the entire Python program",
            },
            "answer": "B",
            "explanation": "`break` terminates the enclosing loop immediately and transfers control to the statement following the loop."
        },
    ]


def sanitize_input(raw_input: str) -> str:
    """
    Trims whitespace and converts user input to uppercase.
    """
    if raw_input is None:
        return ""
    return raw_input.strip().upper()


def is_valid_choice(choice: str, valid_options: List[str]) -> bool:
    """
    Validates if the sanitized choice is among the valid option keys.
    """
    return choice in valid_options


def calculate_percentage(score: int, total: int) -> float:
    """
    Computes percentage score rounded to two decimal places.
    Handles edge case where total is 0 or negative.
    """
    if total <= 0:
        return 0.0
    return round((score / total) * 100, 2)


def get_performance_rating(percentage: float) -> str:
    """
    Returns a qualitative performance summary based on percentage score.
    """
    if percentage >= 90:
        return "Outstanding! Excellent command of the concepts."
    elif percentage >= 75:
        return "Great job! Strong understanding with minor gaps."
    elif percentage >= 50:
        return "Good effort! Review the questions you missed to reinforce your knowledge."
    else:
        return "Needs improvement. Spend some time reviewing the core topics."


def display_welcome_banner(total_questions: int) -> None:
    """
    Displays the introductory banner and quiz rules.
    """
    print("=" * 65)
    print("        WELCOME TO THE INTERACTIVE QUIZ ENGINE (B4)        ")
    print("=" * 65)
    print("Rules & Instructions:")
    print(f" • Total Questions: {total_questions}")
    print(" • Each question has 4 options: [A], [B], [C], [D]")
    print(" • Enter your choice (A, B, C, or D) and press Enter.")
    print(" • Input is case-insensitive ('a' or 'A' are both accepted).")
    print(" • Invalid entries (like 'E', empty string, or numbers) will prompt you again.")
    print(" • Type 'Q' or 'QUIT' anytime to terminate the quiz early.")
    print("=" * 65)
    print()


def prompt_user_choice(valid_options: List[str]) -> str:
    """
    Prompts the user repeatedly until a valid option or quit signal is provided.
    Rejects invalid inputs gracefully without crashing.
    """
    valid_set = set(valid_options)
    prompt_options = "/".join(valid_options)

    while True:
        try:
            raw_input = input(f"Enter your answer ({prompt_options}) or 'Q' to quit: ")
        except (EOFError, KeyboardInterrupt):
            print("\nQuiz interrupted by user.")
            return "QUIT"

        choice = sanitize_input(raw_input)

        if choice in ("Q", "QUIT"):
            return "QUIT"

        if is_valid_choice(choice, valid_options):
            return choice

        # Inform user why the input was rejected and guide them
        if not choice:
            print("  [!] Input cannot be blank. Please enter one of:", prompt_options)
        else:
            print(f"  [!] '{choice}' is not a valid option. Valid options are: {', '.join(valid_options)}.")


def run_quiz() -> None:
    """
    Main interactive loop for running the quiz.
    """
    questions = get_quiz_data()
    total_questions = len(questions)

    display_welcome_banner(total_questions)

    score = 0
    questions_attempted = 0
    review_log = []

    for idx, q_data in enumerate(questions, start=1):
        print(f"\n--- Question {idx} of {total_questions} ---")
        print(q_data["question"])
        print()

        options_keys = sorted(q_data["options"].keys())
        for key in options_keys:
            print(f"  [{key}] {q_data['options'][key]}")
        print()

        user_choice = prompt_user_choice(options_keys)

        if user_choice == "QUIT":
            print("\nExiting quiz early upon user request...")
            break

        questions_attempted += 1
        correct_answer = q_data["answer"]
        is_correct = (user_choice == correct_answer)

        if is_correct:
            score += 1
            print("  [✓] CORRECT!")
        else:
            print(f"  [✗] INCORRECT! Your answer: [{user_choice}], Correct answer: [{correct_answer}]")

        print(f"  [i] Explanation: {q_data['explanation']}")
        print(f"  Current Score: {score}/{questions_attempted}")

        review_log.append({
            "num": idx,
            "question": q_data["question"],
            "user_choice": user_choice,
            "correct_choice": correct_answer,
            "is_correct": is_correct
        })

    # Final summary display
    print("\n" + "=" * 65)
    print("                    QUIZ RESULTS SUMMARY                    ")
    print("=" * 65)

    if questions_attempted == 0:
        print("No questions were attempted.")
        print("Final Score: 0/0 (0.0%)")
        print("=" * 65)
        return

    percentage = calculate_percentage(score, questions_attempted)
    print(f" Questions Attempted : {questions_attempted} / {total_questions}")
    print(f" Correct Answers     : {score}")
    print(f" Incorrect Answers   : {questions_attempted - score}")
    print(f" Final Score         : {score} / {questions_attempted}")
    print(f" Percentage Score    : {percentage}%")
    print(f" Evaluation          : {get_performance_rating(percentage)}")
    print("-" * 65)
    print("Question Breakdown:")
    for item in review_log:
        status_tag = "CORRECT  " if item["is_correct"] else "INCORRECT"
        print(f" Q{item['num']:02d}: [{status_tag}] Chosen: [{item['user_choice']}] | Correct: [{item['correct_choice']}]")
    print("=" * 65)


# =====================================================================
# Built-in Automated Unit Tests
# Demonstrates 5+ rigorous tests including edge cases
# =====================================================================
class TestQuizEngine(unittest.TestCase):
    """
    Test suite validating core logic, input sanitation, scoring,
    and edge cases without requiring external testing packages.
    """

    def test_1_sanitize_input_normalization(self):
        """Test that inputs with spaces and mixed case are normalized to uppercase."""
        self.assertEqual(sanitize_input("a"), "A")
        self.assertEqual(sanitize_input("  b  "), "B")
        self.assertEqual(sanitize_input("c\n"), "C")
        self.assertEqual(sanitize_input("quit"), "QUIT")

    def test_2_is_valid_choice_valid_options(self):
        """Test validation against valid multiple-choice keys [A, B, C, D]."""
        valid_options = ["A", "B", "C", "D"]
        for opt in valid_options:
            self.assertTrue(is_valid_choice(opt, valid_options))

    def test_3_edge_case_invalid_option_rejection(self):
        """
        EDGE CASE 1: Test that entering 'E' or symbols/numbers is strictly rejected
        when valid options are A-D.
        """
        valid_options = ["A", "B", "C", "D"]
        self.assertFalse(is_valid_choice("E", valid_options))
        self.assertFalse(is_valid_choice("1", valid_options))
        self.assertFalse(is_valid_choice("@", valid_options))
        self.assertFalse(is_valid_choice("AB", valid_options))

    def test_4_edge_case_empty_and_none_input(self):
        """
        EDGE CASE 2: Empty string, whitespace-only, or None inputs.
        """
        self.assertEqual(sanitize_input(""), "")
        self.assertEqual(sanitize_input("    "), "")
        self.assertEqual(sanitize_input(None), "")
        valid_options = ["A", "B", "C", "D"]
        self.assertFalse(is_valid_choice("", valid_options))

    def test_5_calculate_percentage_and_boundary_conditions(self):
        """Test percentage calculation with regular, perfect, zero, and boundary scores."""
        self.assertEqual(calculate_percentage(10, 10), 100.0)
        self.assertEqual(calculate_percentage(7, 10), 70.0)
        self.assertEqual(calculate_percentage(1, 3), 33.33)
        self.assertEqual(calculate_percentage(0, 10), 0.0)
        # Edge case: zero total should return 0.0 without ZeroDivisionError
        self.assertEqual(calculate_percentage(0, 0), 0.0)
        self.assertEqual(calculate_percentage(5, -1), 0.0)

    def test_6_performance_rating_thresholds(self):
        """Test qualitative grading tiers."""
        self.assertIn("Outstanding", get_performance_rating(95.0))
        self.assertIn("Great", get_performance_rating(80.0))
        self.assertIn("Good", get_performance_rating(55.0))
        self.assertIn("Needs improvement", get_performance_rating(40.0))

    def test_7_quiz_dataset_integrity(self):
        """Verify dataset has at least 8 questions and each has 4 valid options."""
        questions = get_quiz_data()
        self.assertGreaterEqual(len(questions), 8)
        for q in questions:
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertEqual(len(q["options"]), 4)
            self.assertIn("answer", q)
            self.assertIn(q["answer"], q["options"])
            self.assertIn("explanation", q)


def main() -> None:
    """
    Entry point. If '--test' flag is passed, executes the unit test suite.
    Otherwise, starts the interactive quiz engine.
    """
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        print("Running Quiz Engine automated test suite...\n")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestQuizEngine)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)
    else:
        run_quiz()


if __name__ == "__main__":
    main()
