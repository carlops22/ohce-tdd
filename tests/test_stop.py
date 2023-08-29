import pytest
def test_stop_command(capfd):
    ohce_instance = Ohce("Pedro") 

    input = "Stop!"

    # Capture the output using the capfd fixture
    with pytest.raises(SystemExit):
        ohce_instance.ohce(input_func=input, output_func=print)

    # Check if the "Adios" message is in the captured output
    captured = capfd.readouterr()
    assert "Adios Pedro" in captured.out