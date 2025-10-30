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

    # Walka 1: Lancelot vs Mordred
    print("\nWalka 1: Lancelot vs Mordred")
    try:
        battle_1_result = battle("lancelot", "mordred")
        print("Wyniki walki:")
        for knight, hp in battle_1_result.items():
            print(f"  {knight}: {hp} HP pozostało")
            if hp == 0:
                print(f"  {knight} został pokonany!")
    except Exception as e:
        print(f"Nie można było przeprowadzić walki: {e}")

    # Walka 2: Arthur vs Red Knight
    print("\nWalka 2: Arthur vs Red Knight")
    try:
        battle_2_result = battle("arthur", "red_knight")
        print("Wyniki walki:")
        for knight, hp in battle_2_result.items():
            print(f"  {knight}: {hp} HP pozostało")
            if hp == 0:
                print(f"  {knight} został pokonany!")
    except Exception as e:
        print(f"Nie można było przeprowadzić walki: {e}")

    print("\n--- Mistrzostwa zostały zakończone! ---")


if __name__ == "__main__":
    run_championship()
