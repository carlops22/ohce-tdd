from app.ohce_kata import Ohce

def test_greeting():
    def test_greeting_morning():
        greeting = Ohce.get_greeting(7)
        assert greeting == "¡Buenos días"
    def test_greeting_afternoon():
        greeting = Ohce.get_greeting(15)
        assert greeting == "¡Buenas tardes"
    def test_greeting_evening():
        greeting = Ohce.get_greeting(22)
        assert greeting == "¡Buenas noches"

    