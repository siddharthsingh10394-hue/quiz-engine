# Project B4 — Interactive Quiz Engine

**Track:** Track B — Python  
**Level:** Easy  
**Implementation:** Single-file application (`quiz_engine.py`)  
**Language & Libraries:** Python 3.10+ (Standard Library: `string`, `sys`, `unittest`)

---

## 1. Overview & Problem Statement

The **Interactive Quiz Engine** is a console-based multiple-choice assessment tool designed to evaluate knowledge of Python and computer science fundamentals. It features an ultra-concise, library-driven architecture (~110 lines of code) that delivers full functionality without external bloat:

- **10 Multiple-Choice Questions:** Exceeds the 8-question requirement, each providing 4 distinct options (`[A]`, `[B]`, `[C]`, `[D]`).
- **Dynamic Option Generation:** Uses `string.ascii_uppercase` and `zip()` to generate and validate option labels dynamically instead of repeating boilerplate dictionaries.
- **Answer Validation & Instant Feedback:** Every response is checked; feedback indicates whether the choice was correct or incorrect, shows the expected answer, and gives a concise explanation.
- **Score & Percentage Display:** Calculates final score and percentage (rounded to 2 decimal places), guarding against division by zero.
- **Self-Contained Unit Tests:** Employs standard `unittest` to provide automated regression and edge case tests within the single file.

---

## 2. Approach Note & Planned Logic

### Inputs & Normalization
- User input is gathered via `input()`.
- Inputs are normalized using `(inp or "").strip().upper()`, safely handling leading/trailing spaces, mixed case (`a` -> `A`), and empty inputs.

### Data Structures & Functions
- **`QUESTIONS` (List of Tuples):** Stored as compact tuples `(question, [opt1, opt2, opt3, opt4], answer_key, explanation)`.
- **`sanitize(inp)`:** Normalizes user input to uppercase and strips whitespace safely.
- **`calc_percent(score, total)`:** Computes percentage, guarding against `ZeroDivisionError` when `total == 0`.
- **`prompt_choice(valid_keys)`:** Continuously re-prompts if the user enters invalid keys (such as `"E"`, numbers, or blank input) until a valid choice or quit signal (`"Q"`) is received.
- **`run_quiz()`:** Manages quiz execution, prints formatted questions, evaluates answers, tracks running score, and prints final score/percentage.

### "Think Before You Code" Checkpoint (Handling `"E"`):
- If the user enters `"E"` when only `A`–`D` are valid, the engine intercepts the input:
  ```
  [!] Invalid choice 'E'. Please enter one of: A, B, C, D
  ```
  The user is re-prompted without consuming a question attempt, penalizing score, or crashing.

### Edge Cases Handled
1. **Edge Case 1 — Empty / Whitespace-only input:** Pressing enter or spaces triggers `[!] Invalid choice ''...` and re-prompts safely.
2. **Edge Case 2 — Out-of-bounds Options ("E", symbols, numbers):** Caught and rejected by membership check against dynamically generated labels.
3. **Edge Case 3 — Zero Division:** Guarded inside `calc_percent()` when `total <= 0`.
4. **Edge Case 4 — Interruption / Early Exit:** Typing `Q`, `Ctrl+C`, or EOF terminates cleanly with partial score calculated.

---

## 3. How to Run

### Interactive Quiz
```bash
python quiz_engine.py
```

### Run Automated Unit Tests
```bash
python quiz_engine.py --test
```

---

## 4. Test Matrix (Automated & Manual)

| Test ID | Method / Target | Scenario / Input | Expected Result | Pass/Fail |
|---|---|---|---|---|
| **TC-01** | `test_sanitize_normal_and_whitespace` | Mixed case & spaces (`"  a  "`, `"b"`) | Normalized to uppercase (`"A"`, `"B"`) | **PASS** |
| **TC-02** | **Edge Case 1:** `test_edge_case_empty_input` | Empty string `""`, `"   "`, `None` | Sanitized to `""` without crashing | **PASS** |
| **TC-03** | **Edge Case 2:** `test_edge_case_invalid_option_rejection` | Out-of-bounds `"E"`, `"1"`, `"@"`, `"AB"` | Rejected; not recognized as valid option | **PASS** |
| **TC-04** | `test_percentage_calculation_and_zero_division` | Regular (8/10), Zero (0/5), Empty (0/0) | Returns exact floats (`80.0%`, `0.0%`) safely | **PASS** |
| **TC-05** | `test_questions_data_integrity` | Minimum 8 questions, 4 options per question | Passes schema & answer key verification | **PASS** |
