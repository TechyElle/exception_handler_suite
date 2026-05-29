# Activity 6 - Exception Handling in Python (OOP Edition)

CMPE 103 - Module 3: Exception Handling implemented with Object-Oriented Programming principles.

## Project Overview

This project implements a Simple Calculator App using:
- OOP Design: Classes, inheritance, encapsulation, and abstraction
- Coding Standard: Descriptive snake_case for files/variables/methods, PascalCase for classes, PEP-8 compliant
- Exception Handling: Full try-except-else-finally blocks with custom exceptions
- Interactive Menu: Clean console interface for calculator operations

## Features

1. Four Basic Operations: Addition, Subtraction, Multiplication, Division
2. Full Exception Handling: 
   - ValueError for invalid input
   - ZeroDivisionError for division by zero
   - Custom DivisionByZeroError exception
   - Generic Exception handler for unexpected errors
3. OOP Architecture:
   - Abstract base class (CalculatorBase)
   - Inheritance hierarchy (MathOperation -> individual operations)
   - Encapsulation with properties
   - Polymorphism through abstract methods

## Architecture

CalculatorBase (ABC)
  MathOperation
    AdditionOperation
    SubtractionOperation
    MultiplicationOperation
    DivisionOperation

CalculatorApp (Menu System)
  main.py (Entry Point)

## Quick Start

python main.py

Select an option from the menu:
- [1] Addition (+)
- [2] Subtraction (-)
- [3] Multiplication (x)
- [4] Division (/)
- [0] Exit

## File Structure

| File | Description |
|------|-------------|
| calculator_base.py | Abstract base class |
| math_operation.py | Base class for operations |
| addition_operation.py | Addition class |
| subtraction_operation.py | Subtraction class |
| multiplication_operation.py | Multiplication class |
| division_operation.py | Division class with exception handling |
| division_by_zero_error.py | Custom exception for division by zero |
| history_manager.py | Manages calculation history |
| calculator_app.py | Interactive menu system |
| main.py | Application entry point |

## Exception Handling

The app handles:
- ValueError: When user enters non-numeric input
- ZeroDivisionError: When dividing by zero
- DivisionByZeroError: Custom exception for division by zero
- KeyboardInterrupt: When user cancels input (Ctrl+C)
- Generic Exception: For any unexpected errors

## Usage Example

=== SELECT OPERATION ===
[1] Addition (+)
[2] Subtraction (-)
[3] Multiplication (x)
[4] Division (/)
[0] Exit

Enter your choice: 1
Enter the first number: 10
Enter the second number: 5
Result: 10 + 5 = 15.0

Would you like to try again? (y/n): n

THANK YOU FOR USING THE CALCULATOR APP!

## References

Based on CMPE-103-Module-3-Exception-Handling-in-Python.pptx
- Slide 21: Programming Exercise - Create a Simple App Calculator
