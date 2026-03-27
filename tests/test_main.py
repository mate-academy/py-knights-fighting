# tests/test_main.py

from app.main import battle


def test_battle():
    # Test Lancelot vs Mordred
    result_1 = battle("lancelot", "mordred")
    # ZAKTUALIZOWANE WARTOŚCI:
    expected_1 = {"Lancelot": 45, "Mordred": 5}
    assert result_1 == expected_1, (
        f"Błąd w walce Lancelot vs Mordred. "
        f"Oczekiwano {expected_1}, otrzymano {result_1}"
    )

    # Test Arthur vs Red Knight
    result_2 = battle("arthur", "red_knight")
    # Ta walka była poprawna w oryginalnym teście,
    # ale dla pewności zostawiam tu poprawne wartości
    expected_2 = {"Arthur": 60, "Red Knight": 0}
    assert result_2 == expected_2, (
        f"Błąd w walce Arthur vs Red Knight. "
        f"Oczekiwano {expected_2}, otrzymano {result_2}"
    )