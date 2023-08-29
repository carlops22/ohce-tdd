import pytest
from app.ohce_kata import Ohce

def test_reverse_echo():
    ohce_instance= Ohce("Pedro")

    input_word = "hola"
    expected_output = "aloh"
    with pytest.raises(SystemExit):
        ohce_instance.ohce(input_f= lambda _: input_word, output_f=print)
    captured= capfd.readouterr()

    assert expected_output in captured.out