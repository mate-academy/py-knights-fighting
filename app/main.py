# app/main.py

"""
Główny plik aplikacji.
"""

from app.config import KNIGHTS
from app.models.knight import Knight
from app.services.battle_logic import calculate_battle_result


def battle(knight_a_name: str, knight_b_name: str) -> dict:
    """
    Publiczna funkcja `battle` używana przez testy.
    """
    if knight_a_name not in KNIGHTS:
        raise KeyError(f"Rycerz '{knight_a_name}' nie znaleziony w KNIGHTS.")
    if knight_b_name not in KNIGHTS:
        raise KeyError(f"Rycerz '{knight_b_name}' nie znaleziony w KNIGHTS.")

    # 1. Pobierz surowe dane z konfiguracji
    knight_a_data = KNIGHTS[knight_a_name]
    knight_b_data = KNIGHTS[knight_b_name]

    # 2. Utwórz obiekty Knight (statystyki zostaną obliczone w __init__)
    knight_a = Knight(knight_a_data)
    knight_b = Knight(knight_b_data)

    # 3. Wywołaj logikę bitwy i zwróć wynik
    return calculate_battle_result(knight_a, knight_b)


def run_championship() -> None:
    """
    Uruchamia predefiniowane walki mistrzowskie i drukuje wyniki.
    """
    print("--- Rozpoczynają się Wielkie Mistrzostwa Camelotu! ---")

    # Zdefiniuj listę walk do przeprowadzenia.
    # Każdy element to krotka: (tytuł walki, klucz_rycerza_1, klucz_rycerza_2)
    battle_configurations = [
        ("Walka 1: Lancelot vs Mordred", "lancelot", "mordred"),
        ("Walka 2: Arthur vs Red Knight", "arthur", "red_knight")
        # Możesz łatwo dodać tu więcej walk!
        # Np. ("Walka 3: Arthur vs Lancelot", "arthur", "lancelot")
    ]

    # Użyj jednej pętli do przetworzenia wszystkich walk
    for title, knight_a_key, knight_b_key in battle_configurations:
        print(f"\n{title}")
        try:
            # Użyj dynamicznych kluczy do wywołania bitwy
            battle_result = battle(knight_a_key, knight_b_key)

            print("Wyniki walki:")
            for knight, hp in battle_result.items():
                print(f"  {knight}: {hp} HP pozostało")
                if hp == 0:
                    print(f"  {knight} został pokonany!")
        except Exception as e:
            # Wyświetl błąd dla konkretnej walki
            print(f"Nie można było przeprowadzić walki ({title}): {e}")

    print("\n--- Mistrzostwa zostały zakończone! ---")


if __name__ == "__main__":
    run_championship()
