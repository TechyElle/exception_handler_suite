# Repository Guidelines

## Project Structure & Module Organization

The project follows a strict Object-Oriented Programming (OOP) hierarchy for a calculator application:

- **`.\main.py`**: The application entry point.
- **`.\calculator_app.py`**: Manages the interactive menu system and handles the high-level execution flow, including global exception handling.
- **`.\calculator_base.py`**: Defines the `CalculatorBase` abstract base class (ABC) with core properties and abstract methods.
- **`.\math_operation.py`**: A base class inheriting from `CalculatorBase` that provides shared functionality for mathematical operations.
- **Concrete Operations**: `.\addition_operation.py`, `.\subtraction_operation.py`, `.\multiplication_operation.py`, and `.\division_operation.py` implement the specific calculation logic.
- **`.\history_manager.py`**: (If present) Manages operation history.

## Build, Test, and Development Commands

This is a pure Python project without external dependencies.

- **Run Application**: `python .\main.py`
- **Manual Verification**: Run the application and select operations 1-4. Ensure that invalid inputs (non-numeric) and division by zero are handled gracefully.

## Coding Style & Naming Conventions

The project adheres to PEP-8 standards with specific naming conventions:

- **Classes**: `PascalCase` (e.g., `AdditionOperation`)
- **Methods & Functions**: `snake_case` (e.g., `perform_operation`)
- **Variables**: `snake_case` (e.g., `first_number`)
- **Files**: `snake_case` (e.g., `math_operation.py`)
- **Private Attributes**: Prefixed with an underscore (e.g., `_result`)

## Exception Handling Guidelines

Exception handling is a core component of this repository. Follow these patterns:

- **Input Validation**: Use `try-except ValueError` when converting user input to floats.
- **Specific Exceptions**: Always prefer specific exceptions (e.g., `ZeroDivisionError`) over generic `Exception` blocks.
- **Custom Exceptions**: Use `DivisionByZeroError` (defined in `.\division_operation.py`) for custom division-related errors.
- **Control Flow**: Utilize `try-except-else-finally` blocks to ensure resources are managed and users are informed of errors without application crashes.
