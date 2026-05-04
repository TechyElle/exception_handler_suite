# Building From Scratch - Activity 6

This guide shows the step-by-step process of building the Calculator App with Exception Handling from an empty repository.

## Step 0: Setup

Initial files available:

- TODO.md (empty)
- main.py (empty 0 bytes)
- BUILD_FROM_SCRATCH.md (empty)
- CMPE-103-Module-3-Exception-Handling-in-Python.pptx (reference material)

## Committing Milestones (Grade Requirement)

Commit after each milestone (small, descriptive commits).
Suggested workflow:

1. Make one logical change (ex: create one module/class or one method)
2. Verify it still runs (quick manual check)
3. Stage only the relevant files: `git add <changed_files>`
4. Commit with a descriptive message (start with `docs:`, `feat:`, `fix:`, `refactor:`, or `chore:`)

This repo is expected to have milestone-focused commit history (not one single final commit).


## Committing Milestones (Grade Requirement)

Commit after each milestone (small, descriptive commits). Suggested workflow:

1. Make one logical change (ex: create one module/class or one method)
2. Verify it still runs (optional fast manual check)
3. Stage only what you changed:
   - `git add <changed_files>`
4. Commit with a descriptive message:
   - `docs: ...`, `feat: ...`, `refactor: ...`, `fix: ...`, `chore: ...`
5. Repeat until the project is complete.

This repo is expected to have milestone-focused commit history (not one single final commit).

## Step 1: Analyze Requirements

From Slide 21 - Programming Exercise:

1. Ask user to choose math operation (Add, Subtract, Multiply, Divide)
2. Ask for two numbers
3. Display result
4. Ask if want to try again
5. Exit or repeat
6. Use Python Functions and Exceptions

## Step 2: Create TODO.md

Created comprehensive TODO.md with:

- Task requirements
- Coding standards from Activity 5
- Implementation plan

## Step 3: Create Base Architecture (calculator_base.py)

Created Abstract Base Class CalculatorBase with:

- Abstract methods (operation_name, operation_symbol)
- calculate() method
- get_input_numbers() with error handling
- display_result() with try-except
- Property getters

## Step 4: Create Math Operation Base (math_operation.py)

Created MathOperation class that inherits from CalculatorBase:

- Properties for first_number, second_number
- set_numbers() method
- perform_operation() method
- display_operation_info()

## Step 5: Create Concrete Operations

Created 4 operation classes:

### 5.1 addition_operation.py

- Inherits from MathOperation
- calculate(): returns x + y
- add_numbers(): handles multiple numbers

### 5.2 subtraction_operation.py

- Inherits from MathOperation
- calculate(): returns x - y
- subtract_numbers(): handles multiple numbers

### 5.3 multiplication_operation.py

- Inherits from MathOperation
- calculate(): returns x * y
- multiply_numbers(): handles multiple numbers

### 5.4 division_operation.py

- Inherits from MathOperation
- Custom DivisionByZeroError exception
- calculate(): raises exception if divisor is zero
- calculate_safe(): returns tuple (success, result_or_error)
- get_division_input(): special validation

## Step 6: Create Calculator App (calculator_app.py)

Created CalculatorApp with:

- _operations dictionary
- display_banner() / display_menu()
- get_user_choice()
- process_choice()
- handle_operation() with full try-except-finally
- ask_try_again()
- run() - main loop
- display_goodbye()

## Step 7: Create Main Entry Point (main.py)

Created main.py with:

- display_intro()
- main() function
- Exception handling
- Clean exit

## Step 8: Test and Verify

Tested all operations:

- 10 + 5 = 15
- 10 - 5 = 5
- 10 * 5 = 50
- 10 / 5 = 2.0
- Division by zero correctly raises exception

## Step 9: Create Documentation

Created README.md with:

- Project overview
- Features
- Architecture
- File structure
- Exception handling details
- Usage example

## Final File Structure

```
Activity 6/
├── calculator_base.py       # Abstract base class
├── math_operation.py      # Base class for operations
├── addition_operation.py  # Addition (+)
├── subtraction_operation.py  # Subtraction (-)
├── multiplication_operation.py # Multiplication (x)
├── division_operation.py    # Division (/) with exceptions
├── calculator_app.py     # Interactive menu
├── main.py               # Entry point
├── TODO.md               # Task list
├── README.md             # Documentation
└── BUILD_FROM_SCRATCH.md # This file
```

## OOP Principles Applied

1. **Abstraction**: CalculatorBase ABC with abstract methods
2. **Encapsulation**: Private attributes (_result, _error_message)
3. **Inheritance**: All operations inherit from MathOperation
4. **Polymorphism**: Different operations implement calculate() differently

## Exception Handling Applied

1. **try-except**: In get_input_numbers() for ValueError
2. **try-except-finally**: In handle_operation()
3. **Custom Exception**: DivisionByZeroError
4. **Raise Statement**: In division_operation.py
5. **Multiple except**: Catch different exception types

## References

Based on CMPE-103-Module-3-Exception-Handling-in-Python.pptx

- Slide 7: Handling Unchecked Exception (try, except, finally)
- Slide 8: Exception Handling Structure
- Slide 13: Raise an Exception
- Slide 21: Programming Exercise
