"""
Addition Operation Module
======================
Concrete class for addition operation.
"""

from math_operation import MathOperation


class AdditionOperation(MathOperation):
    """
    Addition operation class.
    
    This class performs addition of two numbers.
    """
    
    def __init__(self):
        """Initialize the addition operation."""
        super().__init__()
    
    @property
    def operation_name(self) -> str:
        """Get the name of the operation."""
        return "Addition"
    
    @property
    def operation_symbol(self) -> str:
        """Get the symbol of the operation."""
        return "+"
    
    def calculate(self, x: float, y: float) -> float:
        """
        Perform addition.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            Sum of x and y
        """
        return x + y
    
    def display_operation_info(self) -> None:
        """Display information about the addition operation."""
        super().display_operation_info()
        print(f"  Description: Adds two numbers together")
        print(f"  " + "=" * 30)
