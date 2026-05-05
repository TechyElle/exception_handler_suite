"""
Multiplication Operation Module
==============================
Concrete class for multiplication operation.
"""

from math_operation import MathOperation


class MultiplicationOperation(MathOperation):
    """
    Multiplication operation class.
    
    This class performs multiplication of two numbers.
    """
    
    def __init__(self):
        """Initialize the multiplication operation."""
        super().__init__()
    
    @property
    def operation_name(self) -> str:
        """Get the name of the operation."""
        return "Multiplication"
    
    @property
    def operation_symbol(self) -> str:
        """Get the symbol of the operation."""
        return "×"
    
    def calculate(self, x: float, y: float) -> float:
        """
        Perform multiplication.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            Product of x and y
        """
        return x * y
    
    def display_operation_info(self) -> None:
        """Display information about the multiplication operation."""
        super().display_operation_info()
        print(f"  Description: Multiplies two numbers together")
        print(f"  " + "=" * 30)
