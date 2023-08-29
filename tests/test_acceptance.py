"""
def test_ohce_acceptance():
    input_stream = ["Pedro", "hola", "oto", "stop"]
    output_stream = []

    def mock_input(prompt):
        return input_stream.pop(0)

    def mock_output(message):
        output_stream.append(message)

    ohce(mock_input, mock_output)

    expected_output = [
        "¡Buenos días Pedro!",
        "aloh",
        "oto",
        "¡Bonita palabra!",
        "pots",
        "Adios Pedro"
    ]
    assert output_stream == expected_output
"""