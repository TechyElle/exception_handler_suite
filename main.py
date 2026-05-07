"""
Main Entry Point
==============
Activity 6 - Exception Handling in Python
Simple Calculator App with OOP

This is the main entry point for the Calculator Application.
It demonstrates:
- Object-Oriented Programming (OOP)
- Exception Handling
- Clean Architecture

Run: python main.py
"""

from calculator_app import CalculatorApp


def display_intro() -> None:
    """Display the introduction."""
    print("""
+------------------------------------------------------------+
|                                                            |
|   ACTIVITY 6 - Exception Handling in Python                |
|   CMPE 103 Module 3                                       |
|                                                            |
|   Simple Calculator App with OOP                           |
|                                                            |
|   Features:                                                |
|   * Addition, Subtraction, Multiplication, Division        |
|   * Full Exception Handling                                |
|   * Interactive Menu System                                |
|   * OOP Design (Classes, Inheritance, Abstraction)         |
|                                                            |
+------------------------------------------------------------+
""")


def main() -> None:
    """Main entry point for the calculator application."""
    try:
        display_intro()
        CalculatorApp().run()
    except KeyboardInterrupt:
        print("\n\n  Thank you! Goodbye!")
    except Exception as e:
        print(f"\n  Fatal error: {e}")
        print("  Please restart the application.")


if __name__ == "__main__":
    main()
