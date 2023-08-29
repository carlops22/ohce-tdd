import pytest
from app.ohce_kata import Ohce

def test_stop_command(capfd):
    ohce_instance = Ohce("Pedro") 

    input = "Stop!"


    with pytest.raises(SystemExit):
        ohce_instance.ohce(input=input, output_f=print)

    captured = capfd.readouterr()
    assert "Adios Pedro" in captured.out