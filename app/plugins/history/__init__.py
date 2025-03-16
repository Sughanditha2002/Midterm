import os
import pandas as pd
from app.commands import Command

class HistoryCommand(Command):
    """Handles the calculator history commands."""

    FILE_PATH = "logs/history.csv"

    def execute(self, action=None):
        """Execute history-related actions: view, clear, or delete."""
        if action == "view":
            return self.view_history()
        elif action == "clear":
            return self.clear_history()
        return "Invalid history command. Use: history view | history clear"

    def view_history(self):
        """Return history as a formatted string."""
        if os.path.exists(self.FILE_PATH):
            df = pd.read_csv(self.FILE_PATH)
            return df.to_string(index=False)
        return "No history found."

    def clear_history(self):
        """Clear the history file."""
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)
            return "History cleared."
        return "No history to clear."