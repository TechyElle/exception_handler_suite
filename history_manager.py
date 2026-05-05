"""
History Manager Module
======================
Handles storage and retrieval of calculation history.
Demonstrates File I/O with Exception Handling.
"""

import os
from datetime import datetime


class HistoryManager:
    """
    Manages calculation history.
    
    Stores history in memory and optionally persists to a file.
    """
    
    def __init__(self, filename: str = "calculation_history.txt"):
        """
        Initialize the history manager.
        
        Args:
            filename: File to store history in
        """
        self._filename = filename
        self._history = []
        self._load_from_file()
    
    def add_entry(self, operation: str, symbol: str, x: float, y: float, result: float) -> None:
        """
        Add a new calculation to history.
        
        Args:
            operation: Name of the operation
            symbol: Symbol of the operation
            x: First operand
            y: Second operand
            result: Result of the calculation
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {operation}: {x} {symbol} {y} = {result}"
        self._history.append(entry)
        self._save_to_file(entry)
    
    def get_history(self) -> list:
        """Get the full history."""
        return self._history
    
    def clear_history(self) -> bool:
        """
        Clear the history.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if os.path.exists(self._filename):
                os.remove(self._filename)
            self._history = []
            return True
        except OSError as e:
            print(f"  Error clearing history file: {e}")
            return False
            
    def _save_to_file(self, entry: str) -> None:
        """
        Save a single entry to the file.
        
        Args:
            entry: The history entry to save
        """
        try:
            with open(self._filename, "a", encoding="utf-8") as f:
                f.write(entry + "\n")
        except (IOError, OSError) as e:
            print(f"  Warning: Could not save history to file: {e}")

    def _load_from_file(self) -> None:
        """Load history from file with exception handling."""
        if not os.path.exists(self._filename):
            return
            
        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                self._history = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            # Should not happen due to exists() check, but good for robustness
            self._history = []
        except OSError as e:
            print(f"  Warning: Could not read history file: {e}")

    def display_history(self) -> None:
        """Display the history to the console."""
        print("\n  +--------------------------------+")
        print("  |      CALCULATION HISTORY       |")
        print("  +--------------------------------+")
        
        if not self._history:
            print("  |   No history available yet.    |")
        else:
            for i, entry in enumerate(self._history, 1):
                print(f"  {i}. {entry}")
                
        print("  +--------------------------------+")
