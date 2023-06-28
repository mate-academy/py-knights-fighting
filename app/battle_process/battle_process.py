def hp_count(knights: list[dict]) -> None:
    knights[0]["hp"] -= knights[1]["power"] - knights[0]["protection"]
    for knight in knights:
        knight["hp"] = 0 if knight["hp"] <= 0 else knight["hp"]


def battle_process(knights: list[str], config: dict) -> None:
    knight_pairs = [config[knight] for knight in knights]
    hp_count(knight_pairs)
    hp_count(knight_pairs[::-1])
