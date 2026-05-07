"""
Division By Zero Error Module
=============================
Custom exception for division by zero errors.
"""

class DivisionByZeroError(Exception):
    """Custom exception for Division by Zero errors."""
    
    def __init__(self, message: str = "Cannot divide by zero!"):
        """Initialize the exception."""
        self.message = message
        super().__init__(self.message)
