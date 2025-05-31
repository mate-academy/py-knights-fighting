from app.pidg import apply_stats


def battle(kn_battle: dict) -> dict:
    for knight in kn_battle.values():
        apply_stats(knight)
    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for knight1, knight2 in battles:
        kn_battle[knight1]["hp"] = max(
            0,
            kn_battle[knight1]["hp"]
            - kn_battle[knight2]["power"]
            + kn_battle[knight1]["protection"]
        )
        kn_battle[knight2]["hp"] = max(
            0,
            kn_battle[knight2]["hp"]
            - kn_battle[knight1]["power"]
            + kn_battle[knight2]["protection"]
        )
    return {knight["name"]: knight["hp"] for knight in kn_battle.values()}
