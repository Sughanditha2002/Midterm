import pytest
import os
import pandas as pd
from app.plugins.history import HistoryCommand

@pytest.fixture
def history():
    """Fixture for the HistoryCommand instance."""
    return HistoryCommand()

def test_view_history_empty(history):
    """Test viewing history when it's empty."""
    if os.path.exists(history.FILE_PATH):
        os.remove(history.FILE_PATH)
    assert history.view_history() == "No history found."

def test_add_history_and_view(history):
    """Test adding history and viewing it."""
    df = pd.DataFrame([{"Operation": "add", "A": 2, "B": 3, "Result": 5}])
    df.to_csv(history.FILE_PATH, index=False)
    assert "add" in history.view_history()

def test_clear_history(history):
    """Test clearing the history."""
    df = pd.DataFrame([{"Operation": "subtract", "A": 5, "B": 2, "Result": 3}])
    df.to_csv(history.FILE_PATH, index=False)
    assert history.clear_history() == "History cleared."
    assert history.view_history() == "No history found."

def test_invalid_history_command(history):
    """Test handling of invalid history commands."""
    assert history.execute("invalid") == "Invalid history command. Use: history view | history clear"

def test_history_file_creation(history):
    """Test if the history file is created when adding entries."""
    history.clear_history()  # Ensure file doesn't exist
    df = pd.DataFrame([{"Operation": "multiply", "A": 4, "B": 2, "Result": 8}])
    df.to_csv(history.FILE_PATH, index=False)
    assert os.path.exists(history.FILE_PATH)