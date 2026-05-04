"""
Calculator Base Module
=====================
Abstract base class for calculator operations.
Provides common functionality for all calculator operations.
"""

from abc import ABC, abstractmethod
from typing import Optional


class CalculatorBase(ABC):
    """
    Abstract base class for calculator operations.
    
    This class provides the foundation for all mathematical operations
    in the calculator application. It enforces implementing classes to
    define their own calculate method.
    """
    
    def __init__(self):
        """Initialize the calculator base."""
        self._result: Optional[float] = None
        self._error_message: Optional[str] = None
    
    @property
    def result(self) -> Optional[float]:
        """Get the result of the last calculation."""
        return self._result
    
    @property
    def error_message(self) -> Optional[str]:
        """Get the error message if there's an error."""
        return self._error_message
    
    @property
    @abstractmethod
    def operation_name(self) -> str:
        """Get the name of the operation."""
        pass
    
    @property
    @abstractmethod
    def operation_symbol(self) -> str:
        """Get the symbol of the operation."""
        pass
    
    @abstractmethod
    def calculate(self, x: float, y: float) -> float:
        """
        Perform the calculation.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            Result of the calculation
        """
        pass
    
    def execute(self, x: float, y: float) -> float:
        """
        Execute the calculation with error handling.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            Result of the calculation
        """
        try:
            self._result = self.calculate(x, y)
            self._error_message = None
            return self._result
        except (ArithmeticError, ValueError) as e:
            self._error_message = str(e)
            raise
    
    def _get_float_input(self, prompt: str) -> float:
        """
        Get a valid float input from the user.
        
        Args:
            prompt: The prompt to display to the user
            
        Returns:
            The valid float value
        """
        while True:
            try:
                user_input = input(f"  {prompt}: ")
                return float(user_input)
            except EOFError:
                print("\n  Input cancelled. Exiting.")
                raise KeyboardInterrupt
            except ValueError:
                print(f"  Error: '{user_input}' is not a valid number. Please enter a numeric value.")

    def get_input_numbers(self) -> tuple[float, float]:
        """
        Get two numbers from the user with validation.
        
        Returns:
            Tuple of (x, y) as floats
        """
        x = self._get_float_input("Enter the first number")
        y = self._get_float_input("Enter the second number")
        return x, y
    
    def display_welcome(self) -> None:
        """Display welcome message for the operation."""
        banner_width = max(32, len(self.operation_name) + 20)
        border = "+" + "-" * (banner_width + 2) + "+"
        
        print(f"\n  {border}")
        print(f"  |  {self.operation_name} Operation".ljust(banner_width + 3) + "|")
        print(f"  {border}")
