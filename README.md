# Project B4 — Interactive Quiz Engine

**Track:** Track B — Python  
**Level:** Easy  
**Language:** Python 3.10+ (Standard Library only, zero external dependencies)  
**Implementation:** Single-file application (`quiz_engine.py`)

---

## 1. Overview & Problem Statement

The **Interactive Quiz Engine** is a console-based multiple-choice assessment tool designed to evaluate knowledge of Python and computer science fundamentals. It presents questions sequentially, enforces strict input validation, gives immediate feedback per question with conceptual explanations, and generates a detailed performance summary and breakdown upon completion.

### Core Requirements Met:
- **At least 8 questions & 4 options per question:** Includes 10 curated multiple-choice questions with 4 distinct options (`[A]`, `[B]`, `[C]`, `[D]`) each.
- **Answer validation & immediate feedback:** Every answer is validated before evaluation. Instant feedback indicates whether the selection was correct or incorrect, shows the expected answer, and displays an informative explanation.
- **Score & Percentage Display:** Computes and displays the user's score, percentage score (rounded to 2 decimal places), qualitative performance evaluation, and question-by-question review.
- **Single Python File Delivery:** Entire application logic, question data, interactive UI, and unit test suite are encapsulated cleanly inside `quiz_engine.py`.

---

## 2. Approach Note & Planned Logic

### Inputs
- User input via terminal/console for each question (`A`, `B`, `C`, `D`, or `Q` to quit).

### Data Structures & Functions
- **Question Store (`get_quiz_data`):** Stored as a list of dictionaries (`List[Dict[str, Any]]`). Each dictionary contains:
  - `id`: Question number
  - `question`: The question prompt string
  - `options`: Dictionary mapping keys (`"A"`, `"B"`, `"C"`, `"D"`) to answer text
  - `answer`: The key representing the correct answer
  - `explanation`: Contextual explanation reinforcing the core concept
- **Input Sanitization (`sanitize_input`):** Trims leading/trailing whitespace (`.strip()`) and normalizes case to uppercase (`.upper()`).
- **Validation Loop (`prompt_user_choice`):** Employs a `while True` loop to ensure the user provides a valid key (`A`-`D`). Invalid inputs (such as entering `"E"`, numbers, or empty strings) are intercepted and rejected with a helpful warning without advancing the question or mutating state.
- **Scoring & Review Log (`run_quiz`):** Tracks running total score, records user selection vs. correct answer, and computes percentage using `calculate_percentage()`.

### "Think Before You Code" Checkpoint: Invalid Input ("E")
- **Behavior Decision:** If a user enters `"E"` (or any key outside `A`–`D`), the engine prints:
  ```
  [!] 'E' is not a valid option. Valid options are: A, B, C, D.
  ```
  It will **not** consume an attempt, will **not** penalize the user, and will **not** advance to the next question. Instead, it re-prompts the user until a valid choice is supplied.

### Key Edge Case Handled
- **Edge Case 1 — Empty Input / Trailing Spaces:** Pressing Enter without typing anything or typing spaces only is rejected with `[!] Input cannot be blank.` without raising index errors.
- **Edge Case 2 — Zero Total Division:** The percentage calculator guards against divide-by-zero (`total <= 0`), safely returning `0.0%`.
- **Edge Case 3 — Early Exit / Interruption:** Users can enter `Q` or `QUIT` (or trigger `Ctrl+C` / `EOF`) at any prompt to exit cleanly while still receiving their partial performance breakdown.

---

## 3. Project Structure

```
quiz engine/
├── quiz_engine.py   # Complete implementation & automated unit test suite
└── README.md        # Documentation, test cases, and execution instructions
```

---

## 4. How to Run

### Requirements
- Python 3.10 or higher.
- Uses only built-in modules (`sys`, `unittest`, `typing`).

### Run the Interactive Quiz
Open a terminal in this directory and execute:
```bash
python quiz_engine.py
```

### Run the Automated Unit Tests
The single script includes a self-contained unit test suite. Run:
```bash
python quiz_engine.py --test
```

---

## 5. Documented Test Cases (Manual & Automated)

The project includes 7 automated tests covering normal paths and edge cases:

| Test ID | Test Category | Scenario / Input | Expected Result | Pass/Fail |
|---|---|---|---|---|
| **TC-01** | Input Normalization | Mixed case and spaces (`"  b  "`, `"a"`) | Normalized to uppercase (`"B"`, `"A"`) | **PASS** |
| **TC-02** | Valid Input Validation | Inputs `"A"`, `"B"`, `"C"`, `"D"` | Accepted by `is_valid_choice()` | **PASS** |
| **TC-03** | **Edge Case 1:** Out-of-bounds Options | Input `"E"`, `"1"`, `"@"`, `"AB"` | Rejected; returns `False`, prompts user again | **PASS** |
| **TC-04** | **Edge Case 2:** Empty / Whitespace Input | Empty string `""`, `"   "`, or `None` | Rejected; sanitized to `""`, triggers warning | **PASS** |
| **TC-05** | Calculation & Division Boundary | Normal (7/10), Perfect (10/10), Zero (0/10), Zero total (0/0) | Returns exact float (`70.0%`, `100.0%`, `0.0%`) without `ZeroDivisionError` | **PASS** |
| **TC-06** | Qualitative Rating | Scores across 95%, 80%, 55%, 40% | Categorized into appropriate performance bands | **PASS** |
| **TC-07** | Data Schema Verification | Checks question count ($\ge 8$) & 4 choices per question | Confirms 10 questions, each with options A-D and valid answers | **PASS** |

### Sample Execution of Automated Test Suite:
```
test_1_sanitize_input_normalization (__main__.TestQuizEngine) ... ok
test_2_is_valid_choice_valid_options (__main__.TestQuizEngine) ... ok
test_3_edge_case_invalid_option_rejection (__main__.TestQuizEngine) ... ok
test_4_edge_case_empty_and_none_input (__main__.TestQuizEngine) ... ok
test_5_calculate_percentage_and_boundary_conditions (__main__.TestQuizEngine) ... ok
test_6_performance_rating_thresholds (__main__.TestQuizEngine) ... ok
test_7_quiz_dataset_integrity (__main__.TestQuizEngine) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

## 6. Review Readiness

During the viva/code review, any of the following minor changes can be made immediately:
1. **Adding new questions:** Simply append a dictionary entry to `get_quiz_data()`.
2. **Changing passing thresholds:** Modify boundary conditions inside `get_performance_rating()`.
3. **Adding negative marking:** Adjust score increment logic inside `run_quiz()`.
