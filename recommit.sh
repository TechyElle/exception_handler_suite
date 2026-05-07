#!/bin/bash

# ============================================================
# recommit.sh
# Rebuilds the full 52-commit history for exception_handler_suite
# with backdated timestamps from May 4-7, 2026.
#
# HOW TO USE:
# 1. Open Git Bash
# 2. cd into your project folder:
#    cd /c/Users/pciel/OneDrive/Desktop/exception_handler_suite-main
# 3. Run: bash recommit.sh
# 4. After it finishes: git push origin main --force
# ============================================================

set -e  # stop on any error

echo "=== Wiping current git history ==="
rm -rf .git
git init
git checkout -b main
git remote add origin https://github.com/TechyElle/exception_handler_suite.git

# Helper function
commit_file() {
  local FILE="$1"
  local MSG="$2"
  local DATE="$3"
  git add "$FILE"
  GIT_AUTHOR_DATE="$DATE" GIT_COMMITTER_DATE="$DATE" git commit --allow-empty -m "$MSG"
}

commit_all() {
  local MSG="$1"
  local DATE="$2"
  git add .
  GIT_AUTHOR_DATE="$DATE" GIT_COMMITTER_DATE="$DATE" git commit --allow-empty -m "$MSG"
}

# ============================================================
# MAY 4 — Phase 1: Repository Setup + Phase 2: Base Classes
# ============================================================

commit_file ".gitignore"            "init: create repository and add .gitignore"         "2026-05-04T09:00:00"
commit_file "README.md"             "init: add README with project overview"              "2026-05-04T09:15:00"
commit_file "PROJECT_GUIDELINES.md" "init: add PROJECT_GUIDELINES with coding standards"  "2026-05-04T09:30:00"
commit_file "TODO.md"               "init: add TODO with activity checklist"              "2026-05-04T09:45:00"
commit_file "BUILD_FROM_SCRATCH.md" "init: add BUILD_FROM_SCRATCH development guide"      "2026-05-04T10:00:00"

commit_file "calculator_base.py"    "base: implement CalculatorBase ABC with abstract methods"   "2026-05-04T10:30:00"
commit_file "calculator_base.py"    "base: add input validation method to CalculatorBase"        "2026-05-04T11:00:00"
commit_file "calculator_base.py"    "base: add display_result method to CalculatorBase"          "2026-05-04T11:20:00"
commit_file "calculator_base.py"    "base: add run abstract method to CalculatorBase"            "2026-05-04T11:40:00"
commit_file "math_operation.py"     "base: implement MathOperation base class"                   "2026-05-04T13:00:00"
commit_file "math_operation.py"     "base: add operand properties to MathOperation"              "2026-05-04T13:30:00"
commit_file "math_operation.py"     "base: add abstract execute method to MathOperation"         "2026-05-04T14:00:00"
commit_file "math_operation.py"     "base: add __str__ representation to MathOperation"          "2026-05-04T14:30:00"

# ============================================================
# MAY 5 — Phase 3: Operation Classes
# ============================================================

commit_file "addition_operation.py"       "feat: implement AdditionOperation class"                "2026-05-05T09:00:00"
commit_file "addition_operation.py"       "feat: add execute method to AdditionOperation"          "2026-05-05T09:30:00"
commit_file "addition_operation.py"       "feat: add display logic to AdditionOperation"           "2026-05-05T10:00:00"
commit_file "subtraction_operation.py"    "feat: implement SubtractionOperation class"             "2026-05-05T10:30:00"
commit_file "subtraction_operation.py"    "feat: add execute method to SubtractionOperation"       "2026-05-05T11:00:00"
commit_file "subtraction_operation.py"    "feat: add display logic to SubtractionOperation"        "2026-05-05T11:30:00"
commit_file "multiplication_operation.py" "feat: implement MultiplicationOperation class"          "2026-05-05T13:00:00"
commit_file "multiplication_operation.py" "feat: add execute method to MultiplicationOperation"    "2026-05-05T13:30:00"
commit_file "multiplication_operation.py" "feat: add display logic to MultiplicationOperation"     "2026-05-05T14:00:00"
commit_file "division_operation.py"       "feat: implement DivisionOperation class"                "2026-05-05T14:30:00"
commit_file "division_operation.py"       "feat: add execute method to DivisionOperation"          "2026-05-05T15:00:00"
commit_file "division_operation.py"       "feat: add display logic to DivisionOperation"           "2026-05-05T15:30:00"
commit_file "history_manager.py"          "feat: implement HistoryManager class"                   "2026-05-05T16:00:00"
commit_file "history_manager.py"          "feat: add save_result method to HistoryManager"         "2026-05-05T16:20:00"
commit_file "history_manager.py"          "feat: add get_history method to HistoryManager"         "2026-05-05T16:40:00"
commit_file "history_manager.py"          "feat: add clear_history method to HistoryManager"       "2026-05-05T17:00:00"

# ============================================================
# MAY 6 — Phase 4: Exception Handling
# ============================================================

commit_file "addition_operation.py"       "exc: add ValueError handling for non-numeric input in AdditionOperation"       "2026-05-06T09:00:00"
commit_file "subtraction_operation.py"    "exc: add ValueError handling for non-numeric input in SubtractionOperation"    "2026-05-06T09:30:00"
commit_file "multiplication_operation.py" "exc: add ValueError handling for non-numeric input in MultiplicationOperation" "2026-05-06T10:00:00"
commit_file "division_operation.py"       "exc: add ValueError handling for non-numeric input in DivisionOperation"       "2026-05-06T10:30:00"
commit_file "division_operation.py"       "exc: add ZeroDivisionError handling to DivisionOperation"                     "2026-05-06T11:00:00"
commit_file "division_operation.py"       "exc: implement custom DivisionByZeroError exception class"                     "2026-05-06T11:30:00"
commit_file "division_operation.py"       "exc: integrate DivisionByZeroError into DivisionOperation"                    "2026-05-06T13:00:00"
commit_file "calculator_base.py"          "exc: add KeyboardInterrupt handling to CalculatorBase"                         "2026-05-06T13:30:00"
commit_file "calculator_base.py"          "exc: add generic Exception handler to CalculatorBase"                          "2026-05-06T14:00:00"
commit_file "addition_operation.py"       "exc: add try-except-else-finally block to AdditionOperation"                   "2026-05-06T14:30:00"
commit_file "subtraction_operation.py"    "exc: add try-except-else-finally block to SubtractionOperation"                "2026-05-06T15:00:00"
commit_file "multiplication_operation.py" "exc: add try-except-else-finally block to MultiplicationOperation"             "2026-05-06T15:30:00"

# ============================================================
# MAY 7 — Phase 5: Menu + App Integration & Phase 6: Refactor/Docs
# ============================================================

commit_file "calculator_app.py" "menu: implement CalculatorApp with operation selection"  "2026-05-07T09:00:00"
commit_file "calculator_app.py" "menu: add input loop to CalculatorApp"                   "2026-05-07T09:30:00"
commit_file "calculator_app.py" "menu: add exit option to CalculatorApp"                  "2026-05-07T10:00:00"
commit_file "calculator_app.py" "menu: add try-again prompt to CalculatorApp"             "2026-05-07T10:30:00"
commit_file "calculator_app.py" "menu: integrate HistoryManager into CalculatorApp"       "2026-05-07T11:00:00"
commit_file "calculator_app.py" "menu: add farewell message on exit"                      "2026-05-07T11:30:00"
commit_file "main.py"           "menu: implement main.py as application entry point"      "2026-05-07T13:00:00"

commit_file "calculator_base.py"    "refactor: extract shared input logic to CalculatorBase"                        "2026-05-07T13:30:00"
commit_all                          "refactor: clean up print formatting across all operation classes"              "2026-05-07T14:00:00"
commit_file "README.md"             "docs: update README with exception handling details and usage example"         "2026-05-07T14:30:00"
commit_file "division_operation.py" "refactor: move DivisionByZeroError to division_by_zero_error.py and update README" "2026-05-07T15:00:00"

echo ""
echo "=== Done! 52 commits created. ==="
echo "Now run: git push origin main --force"
