
import pytest
from app.ohce_kata import Ohce

def test_palindrome(capfd):
    ohce_instance= Ohce("Pedro")
    input_sequence=["oto","Stop!"]
    expected_output = "¡Bonita palabra!"
    def input_func(prompt):
        return input_sequence.pop(0)
    with pytest.raises(SystemExit):
        ohce_instance.ohce(input= input_func)
    captured= capfd.readouterr()

    assert expected_output in captured.out