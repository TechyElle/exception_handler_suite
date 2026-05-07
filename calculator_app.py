"""
Calculator App Module
==================
Interactive menu system for calculator operations.
Provides exception handling and user interaction.
"""

from addition_operation import AdditionOperation
from subtraction_operation import SubtractionOperation
from multiplication_operation import MultiplicationOperation
from division_operation import DivisionOperation, DivisionByZeroError
from history_manager import HistoryManager


class CalculatorApp:
    """
    Calculator Application class.
    
    This class manages the interactive calculator menu
    with proper exception handling.
    """
    
    def __init__(self):
        """Initialize the calculator app."""
        self._operations = {}
        self._initialize_operations()
        self._history = HistoryManager()
        self._running = False
    
    def _initialize_operations(self) -> None:
        """Initialize all calculator operations."""
        self._operations = {
            '1': AdditionOperation(),
            '2': SubtractionOperation(),
            '3': MultiplicationOperation(),
            '4': DivisionOperation()
        }
    
    def display_banner(self) -> None:
        """Display the banner."""
        print("\n" + "=" * 40)
        print("   SIMPLE CALCULATOR APP   ")
        print("   Exception Handling Edition")
        print("=" * 40)
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n  +--------------------------------+")
        print("  |     SELECT OPERATION           |")
        print("  +--------------------------------+")
        print("  |  [1] Addition       (+)        |")
        print("  |  [2] Subtraction    (-)        |")
        print("  |  [3] Multiplication (x)        |")
        print("  |  [4] Division       (/)        |")
        print("  |  [5] View History   (H)        |")
        print("  |  [0] Exit                      |")
        print("  +--------------------------------+")
    
    def get_user_choice(self) -> str:
        """
        Get user's operation choice.
        
        Returns:
            User's choice string
        """
        return input("  Enter your choice: ").strip()
    
    def process_choice(self, choice: str) -> None:
        """
        Process the user's choice.
        
        Args:
            choice: User's choice
        """
        # Handle History
        if choice == '5':
            self._history.display_history()
            return
        
        # Handle invalid choice
        if choice not in self._operations:
            print("\n  Error: Invalid choice! Please select 1-5 or 0.")
            return
        
        # Get the operation
        operation = self._operations[choice]
        
        # Handle the operation with exception handling
        try:
            self.handle_operation(operation)
        except KeyboardInterrupt:
            print("\n  Operation cancelled by user.")
    
    def handle_operation(self, operation) -> None:
        """
        Handle a specific operation with full exception handling.
        
        Args:
            operation: The operation object
        """
        # Display welcome
        operation.display_welcome()
        
        # Get numbers with error handling
        try:
            x, y = operation.get_input_numbers()
        except KeyboardInterrupt:
            print("\n  Input cancelled by user.")
            return
        
        # Calculate with exception handling
        try:
            result = operation.execute(x, y)
            print(f"\n  [OK] Success!")
            print(f"  Result: {x} {operation.operation_symbol} {y} = {result}")
            
            # Record in history
            self._history.add_entry(
                operation.operation_name, 
                operation.operation_symbol, 
                x, y, result
            )
            
        except (DivisionByZeroError, ZeroDivisionError, ArithmeticError) as e:
            print(f"\n  [ERROR] {e}")
            if isinstance(e, (DivisionByZeroError, ZeroDivisionError)):
                print("  Please try again with a non-zero divisor.")
        except ValueError as ve:
            print(f"\n  [ERROR] Invalid value: {ve}")
        except RuntimeError as e:
            print(f"\n  [ERROR] An unexpected runtime error occurred: {e}")
        
        finally:
            print(f"  " + "-" * 30)
    
    def ask_try_again(self) -> bool:
        """
        Ask user if they want to try again.
        
        Returns:
            True if want to try again, False otherwise
        """
        print("\n  Would you like to try again?")
        response = input("  Enter 'y' for Yes or 'n' for No: ").strip().lower()
        
        if response in ['y', 'yes', '1']:
            return True
        elif response in ['n', 'no', '0']:
            return False
        else:
            print("  Invalid input. Treating as 'No'.")
            return False
    
    def run(self) -> None:
        """Run the calculator application."""
        self.display_banner()
        self._running = True
        
        while self._running:
            try:
                # Display menu
                self.display_menu()
                
                # Get user choice
                choice = self.get_user_choice()
                
                # Handle exit choice
                if choice == '0':
                    break
                
                # Process other choices
                self.process_choice(choice)
                
                # Ask to try again ONLY after a math operation (choices 1-4)
                if choice in ['1', '2', '3', '4']:
                    if not self.ask_try_again():
                        break
                
            except KeyboardInterrupt:
                print("\n\n  Exiting calculator...")
                break
        
        # Display exit message
        self.display_goodbye()
    
    def display_goodbye(self) -> None:
        """Display goodbye message."""
        print("\n" + "=" * 40)
        print("   THANK YOU FOR USING   ")
        print("   THE CALCULATOR APP!")
        print("   See you next time!  ")
        print("=" * 40 + "\n")


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
