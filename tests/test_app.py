import pytest
from streamlit.testing.v1 import AppTest
#FIX: Copilot added new tets file to tets difficulties and game resetting after clicking new game
def test_new_game_resets_state():
    """Test that clicking 'New Game' properly resets the game state."""
    at = AppTest.from_file("app.py").run(timeout=10)

    # Set difficulty to Easy and run the app
    at.selectbox("Difficulty").select("Easy").run(timeout=10)

    # Verify initial state is set
    assert "secret" in at.session_state
    assert "attempts" in at.session_state
    assert "status" in at.session_state
    assert "score" in at.session_state
    assert "history" in at.session_state

    # Click the "New Game" button
    at.button("New Game 🔁").click().run(timeout=10)

    # Check that the state is reset
    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0
    assert at.session_state.history == []
    assert at.session_state.score == 0
    # Secret should be in the Easy range (1-20)
    assert 1 <= at.session_state.secret <= 20

def test_new_game_with_different_difficulties():
    """Test new game with Normal and Hard difficulties."""
    at = AppTest.from_file("app.py").run(timeout=10)

    # Test Normal difficulty
    at.selectbox("Difficulty").select("Normal").run(timeout=10)
    at.button("New Game 🔁").click().run(timeout=10)
    assert 1 <= at.session_state.secret <= 100

    # Test Hard difficulty
    at.selectbox("Difficulty").select("Hard").run(timeout=10)
    at.button("New Game 🔁").click().run(timeout=10)
    assert 1 <= at.session_state.secret <= 50