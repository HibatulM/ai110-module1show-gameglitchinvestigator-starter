import pytest

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

@pytest.mark.parametrize("guess, secret, expected", [
    (50, 50, "Win"),       # exact match
    (51, 50, "Too High"),  # just above
    (49, 50, "Too Low"),   # just below
    (100, 1, "Too High"),  # far above
    (1, 100, "Too Low"),   # far below
])
def test_check_guess_outcomes(guess, secret, expected):
    # check_guess should report the correct outcome relative to the secret
    assert check_guess(guess, secret) == expected
