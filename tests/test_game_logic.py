import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

@pytest.mark.parametrize("guess, secret, expected", [
    (50, 50, ("Win", "🎉 Correct!")),       # exact match
    (51, 50, ("Too High", "📉 Go LOWER!")),  # just above
    (49, 50, ("Too Low", "📈 Go HIGHER!")),  # just below
    (100, 1, ("Too High", "📉 Go LOWER!")),  # far above
    (1, 100, ("Too Low", "📈 Go HIGHER!")),  # far below
])
def test_check_guess_outcomes(guess, secret, expected):
    # check_guess returns (outcome, message) relative to the secret
    assert check_guess(guess, secret) == expected

@pytest.mark.parametrize("raw, expected", [
    ("42", (True, 42, None)),                 # plain integer
    ("3.9", (True, 3, None)),                 # float string is truncated to int
    ("-7", (True, -7, None)),                 # negative integer
    ("-2.8", (True, -2, None)),               # negative float truncated toward zero
    ("", (False, None, "Enter a guess.")),    # empty input
    (None, (False, None, "Enter a guess.")),  # missing input
    ("abc", (False, None, "That is not a number.")),  # non-numeric
])
def test_parse_guess(raw, expected):
    # parse_guess returns (ok, guess_int, error_message)
    assert parse_guess(raw) == expected

@pytest.mark.parametrize("difficulty, expected", [
    ("Easy", (1, 20)),       # easy range
    ("Normal", (1, 100)),    # normal range
    ("Hard", (1, 50)),       # hard range
    ("Unknown", (1, 100)),   # unrecognized falls back to default
])
def test_get_range_for_difficulty(difficulty, expected):
    # get_range_for_difficulty returns the (low, high) inclusive range
    assert get_range_for_difficulty(difficulty) == expected
