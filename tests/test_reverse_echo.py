import sys
import pytest
from app.ohce_kata import Ohce

def test_reverse_echo(capfd):
    ohce_instance= Ohce("Pedro")
    input_sequence=["hola","Stop!"]
    expected_output = "aloh"
    def input_func(prompt):
        return input_sequence.pop(0)
    with pytest.raises(SystemExit):
        ohce_instance.ohce(input= input_func)
    captured= capfd.readouterr()

    assert expected_output in captured.out