"""
Division Operation Module
========================
Concrete class for division operation with proper exception handling.
"""

from math_operation import MathOperation
from division_by_zero_error import DivisionByZeroError


class DivisionOperation(MathOperation):
    """
    Division operation class.
    
    This class performs division of two numbers.
    Includes proper exception handling for division by zero.
    """
    
    def __init__(self):
        """Initialize the division operation."""
        super().__init__()
    
    @property
    def operation_name(self) -> str:
        """Get the name of the operation."""
        return "Division"
    
    @property
    def operation_symbol(self) -> str:
        """Get the symbol of the operation."""
        return "÷"
    
    def calculate(self, x: float, y: float) -> float:
        """
        Perform division with exception handling.
        
        Args:
            x: First number (dividend)
            y: Second number (divisor)
            
        Returns:
            Quotient of x divided by y
            
        Raises:
            DivisionByZeroError: If divisor is zero
        """
        if y == 0:
            raise DivisionByZeroError()
        
        return x / y
    
    def display_operation_info(self) -> None:
        """Display information about the division operation."""
        super().display_operation_info()
        print(f"  Description: Divides first number by second")
        print(f"  Note: Second number cannot be zero!")
        print(f"  " + "=" * 30)
