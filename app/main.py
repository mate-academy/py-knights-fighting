from app.players import knights
from app.battle import knight_fighting
from app.knight import knights_preparing


def battle(knights_config: dict) -> dict:
    for knight in list(knights_config.values()):
        knights_preparing(knight)
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]
    knight_fighting(lancelot, mordred)
    knight_fighting(red_knight, arthur)
    return {lancelot["name"]: lancelot["hp"],
            mordred["name"]: mordred["hp"],
            arthur["name"]: arthur["hp"],
            red_knight["name"]: red_knight["hp"]}


battle_results = battle(knights)
print("--- Battle Results ---")
for knight_name, hp in battle_results.items():
    print(f"{knight_name}: {max(0, hp)} HP")
