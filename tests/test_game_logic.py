from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests for the new logic ensuring secret is consistently int, but check_guess handles str for robustness
def test_check_guess_with_str_secret_win():
    # Test that check_guess handles str secret (from old buggy logic) correctly
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_with_str_secret_too_high():
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_with_str_secret_too_low():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
