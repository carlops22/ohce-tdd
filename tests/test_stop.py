import pytest
from app.ohce_kata import Ohce

def test_stop_command(capfd):
    ohce_instance = Ohce("Pedro") 

    input_sequence = ["hola", "Stop!"]
    def input_func(prompt):
        return input_sequence.pop(0)

    with pytest.raises(SystemExit):
        ohce_instance.ohce(input=input_func)

    captured = capfd.readouterr()
    assert "Adios Pedro" in captured.out