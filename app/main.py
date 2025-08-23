from app.knights.knight import Knight
from app.battle.fight import fight
from app.knights.data import KNIGHTS


def battle(knights_config: dict) -> dict:

    # Cria instâncias da classe Knight a partir dos dados
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Simula as batalhas
    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # Retorna os resultados da batalha
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


# Bloco para executar e testar a função battle
if __name__ == "__main__":
    battle_results = battle(KNIGHTS)
    print("Resultado da Batalha:")
    for knight, hp in battle_results.items():
        print(f"- {knight}: {hp} HP")
