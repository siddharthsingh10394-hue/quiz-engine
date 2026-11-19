import string
import sys
import unittest

# Multiple Choice Dataset: (Question, [Options A-D], Correct Answer, Explanation)
QUESTIONS = [
    ("Difference between a Python list and a tuple?",
     ["Lists are mutable; tuples are immutable", "Lists are immutable; tuples are mutable", "Lists only store ints", "Tuples cannot be sliced"],
     "A", "Lists can be modified in-place; tuples cannot."),
    ("Built-in function returning both index and element during iteration?",
     ["zip()", "map()", "enumerate()", "filter()"],
     "C", "enumerate() yields (index, item) pairs."),
    ("Average time complexity of key lookup in a Python dictionary?",
     ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
     "B", "Python dicts use hash tables, providing O(1) average lookup."),
    ("What does bool([]) evaluate to in Python?",
     ["True", "False", "None", "TypeError"],
     "B", "Empty collections evaluate to False in boolean context."),
    ("Keyword used to catch exceptions that occur in a try block?",
     ["catch", "handle", "except", "trap"],
     "C", "Python uses try...except blocks for error handling."),
    ("Data structure operating on Last-In, First-Out (LIFO)?",
     ["Queue", "Stack", "Tree", "Graph"],
     "B", "Stacks follow the LIFO principle."),
    ("What does str.strip() do on a Python string?",
     ["Splits words", "Removes leading/trailing whitespace", "Lowercases string", "Reverses string"],
     "B", "strip() trims leading and trailing whitespaces."),
    ("Operator used for floor division in Python?",
     ["/", "%", "//", "**"],
     "C", "// performs floor division."),
    ("Which sequence data type in Python is immutable?",
     ["list", "set", "str", "dict"],
     "C", "Strings (str) in Python are immutable."),
    ("What is the purpose of the break statement in a loop?",
     ["Skips one iteration", "Terminates the loop immediately", "Restarts the loop", "Exits program"],
     "B", "break immediately terminates the enclosing loop."),
]

def sanitize(inp: str) -> str:
    """Trim whitespace and convert to uppercase."""
    return (inp or "").strip().upper()

def calc_percent(score: int, total: int) -> float:
    """Calculate percentage score safely avoiding ZeroDivisionError."""
    return round((score / total) * 100, 2) if total > 0 else 0.0

def prompt_choice(valid_keys: list[str]) -> str:
    """Prompt user repeatedly until a valid option or 'Q' is entered."""
    while True:
        try:
            choice = sanitize(input(f"Choice ({'/'.join(valid_keys)}) or 'Q' to quit: "))
        except (KeyboardInterrupt, EOFError):
            return "Q"
        if choice in valid_keys or choice == "Q":
            return choice
        print(f"  [!] Invalid choice '{choice}'. Please enter one of: {', '.join(valid_keys)}")

def run_quiz():
    """Run interactive multiple-choice quiz."""
    print("=" * 60 + "\n        INTERACTIVE QUIZ ENGINE (B4)\n" + "=" * 60)
    score, attempted = 0, 0
    for idx, (q, opts, ans, exp) in enumerate(QUESTIONS, 1):
        labels = list(string.ascii_uppercase[:len(opts)])
        print(f"\n[Q{idx}/{len(QUESTIONS)}] {q}")
        for lbl, opt in zip(labels, opts):
            print(f"  [{lbl}] {opt}")
        choice = prompt_choice(labels)
        if choice == "Q":
            print("\nQuiz terminated early by user.")
            break
        attempted += 1
        correct = (choice == ans)
        score += int(correct)
        status = "[✓] Correct!" if correct else f"[✗] Incorrect! Correct: [{ans}]"
        print(f"  {status}\n  [i] {exp}\n  Score: {score}/{attempted}")

    pct = calc_percent(score, attempted)
    print("\n" + "=" * 60 + f"\nFINAL SCORE: {score}/{attempted} ({pct}%)\n" + "=" * 60)

class TestQuizEngine(unittest.TestCase):
    """5+ unit tests covering core logic and required edge cases."""
    def test_sanitize_normal_and_whitespace(self):
        self.assertEqual(sanitize("  a  "), "A")
        self.assertEqual(sanitize("b"), "B")

    def test_edge_case_empty_input(self):
        """EDGE CASE 1: Empty or whitespace-only input."""
        self.assertEqual(sanitize(""), "")
        self.assertEqual(sanitize("   "), "")
        self.assertEqual(sanitize(None), "")

    def test_edge_case_invalid_option_rejection(self):
        """EDGE CASE 2: 'E' or numeric inputs outside valid A-D range."""
        valid = ["A", "B", "C", "D"]
        for bad in ["E", "1", "@", "AB"]:
            self.assertNotIn(sanitize(bad), valid)

    def test_percentage_calculation_and_zero_division(self):
        self.assertEqual(calc_percent(8, 10), 80.0)
        self.assertEqual(calc_percent(0, 5), 0.0)
        self.assertEqual(calc_percent(0, 0), 0.0)

    def test_questions_data_integrity(self):
        self.assertGreaterEqual(len(QUESTIONS), 8)
        for _, opts, ans, _ in QUESTIONS:
            self.assertEqual(len(opts), 4)
            self.assertIn(ans, string.ascii_uppercase[:len(opts)])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        unittest.main(argv=[sys.argv[0]])
    else:
        run_quiz()
