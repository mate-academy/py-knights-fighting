from app.utils.conventor import convertor
from app.data.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict[str, int]:
    knights = convertor(knights_config)
    knights["Lancelot"].attack(knights["Mordred"])
    knights["Arthur"].attack(knights["Red Knight"])
    result_battle_hp = {
        knight_name: knight_data.hp
        for knight_name, knight_data in knights.items()
    }
    print(result_battle_hp)
    return result_battle_hp


battle(KNIGHTS)
