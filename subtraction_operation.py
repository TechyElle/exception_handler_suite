"""
Subtraction Operation Module
=========================
Concrete class for subtraction operation.
"""

from math_operation import MathOperation


class SubtractionOperation(MathOperation):
    """
    Subtraction operation class.
    
    This class performs subtraction of two numbers.
    """
    
    def __init__(self):
        """Initialize the subtraction operation."""
        super().__init__()
    
    @property
    def operation_name(self) -> str:
        """Get the name of the operation."""
        return "Subtraction"
    
    @property
    def operation_symbol(self) -> str:
        """Get the symbol of the operation."""
        return "-"
    
    def calculate(self, x: float, y: float) -> float:
        """
        Perform subtraction.
        
        Args:
            x: First number (minuend)
            y: Second number (subtrahend)
            
        Returns:
            Difference of x and y
        """
        return x - y
    
    def display_operation_info(self) -> None:
        """Display information about the subtraction operation."""
        super().display_operation_info()
        print(f"  Description: Subtracts second number from first")
        print(f"  " + "=" * 30)
