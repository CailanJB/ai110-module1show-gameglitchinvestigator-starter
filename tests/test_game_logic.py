from logic_utils import check_guess, parse_guess, update_score

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

# Tests for parse_guess
def test_parse_guess_valid_int():
    ok, guess, err = parse_guess("42")
    assert ok == True
    assert guess == 42
    assert err is None

def test_parse_guess_valid_float():
    ok, guess, err = parse_guess("42.0")
    assert ok == True
    assert guess == 42
    assert err is None

def test_parse_guess_invalid_string():
    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

def test_parse_guess_empty():
    ok, guess, err = parse_guess("")
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

# Tests for update_score
def test_update_score_win():
    new_score = update_score(100, "Win", 2)
    assert new_score == 100 + (100 - 10 * (2 + 1))  # 100 + 70 = 170

def test_update_score_win_minimum():
    new_score = update_score(0, "Win", 10)  # points = 100 - 10*11 = -10, but min 10
    assert new_score == 0 + 10

def test_update_score_too_high_even_attempt():
    new_score = update_score(50, "Too High", 1)  # attempt_number % 2 == 1, -5
    assert new_score == 50 - 5

def test_update_score_too_high_odd_attempt():
    new_score = update_score(50, "Too High", 0)  # attempt_number % 2 == 0, +5
    assert new_score == 50 + 5

def test_update_score_too_low():
    new_score = update_score(50, "Too Low", 3)
    assert new_score == 50 - 5

def test_update_score_unknown_outcome():
    new_score = update_score(50, "Unknown", 1)
    assert new_score == 50
