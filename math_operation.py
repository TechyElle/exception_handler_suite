"""
Math Operation Module
===================
Base class for mathematical operations.
Provides common functionality for all math operations.
"""

from calculator_base import CalculatorBase


class MathOperation(CalculatorBase):
    """
    Base class for mathematical operations.
    
    This class inherits from CalculatorBase and provides
    a foundation for all specific mathematical operations.
    """
    
    def __init__(self):
        """Initialize the math operation."""
        super().__init__()
        self._first_number: float = 0.0
        self._second_number: float = 0.0
    
    @property
    def first_number(self) -> float:
        """Get the first number."""
        return self._first_number
    
    @property
    def second_number(self) -> float:
        """Get the second number."""
        return self._second_number
    
    @first_number.setter
    def first_number(self, value: float) -> None:
        """Set the first number."""
        self._first_number = value
    
    @second_number.setter
    def second_number(self, value: float) -> None:
        """Set the second number."""
        self._second_number = value
    
    def set_numbers(self, x: float, y: float) -> None:
        """
        Set both numbers.
        
        Args:
            x: First number
            y: Second number
        """
        self._first_number = x
        self._second_number = y
    
    def get_numbers_from_input(self) -> tuple[float, float]:
        """
        Get two numbers from the user.
        
        Returns:
            Tuple of (first_number, second_number) as floats
        """
        self._first_number, self._second_number = self.get_input_numbers()
        return self._first_number, self._second_number
    
    def perform_operation(self) -> float:
        """
        Perform the operation with the stored numbers.
        
        Returns:
            Result of the calculation
        """
        return self.execute(self._first_number, self._second_number)
    
    def display_operation_info(self) -> None:
        """Display information about the operation."""
        print(f"\n  Operation: {self.operation_name}")
        print(f"  Symbol: {self.operation_symbol}")
        print(f"  " + "=" * 30)
