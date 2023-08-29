import pytest
from app.ohce_kata import Ohce
@pytest.mark.parametrize("current_hour, expected_greeting", [
    (7, "¡Buenos días"),
    (15, "¡Buenas tardes"),
    (22, "¡Buenas noches")
    ])

def test_get_greeting(current_hour, expected_greeting):
    ohce_instance = Ohce("Pedro")
    greeting = ohce_instance.get_greeting(current_hour)
    assert greeting == expected_greeting
def test_get_greeting_invalid_hour():
    ohce_instance = Ohce("Pedro")  #
    with pytest.raises(ValueError):
        ohce_instance.get_greeting(-1)  