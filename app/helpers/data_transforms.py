from app.helpers.types import NewKnightsConfig
from app.heroes.knight import Knight
from app.equipment.knight import Weapon, ArmourComponent, Potion


def transform_to_new_knights_config(old_knights_config: dict) -> NewKnightsConfig:
    new_knights = []
    for name, data in old_knights_config.items():
        weapon = Weapon(data['weapon']['name'], data['weapon']['power'])
        armour = []
        for component in data.get('armour', []):
            armour.append(ArmourComponent(component['part'], component['protection']))
        potion_data = data.get('potion')
        potion = None
        if potion_data:
            potion = Potion(potion_data['name'], potion_data['effect'])
        knight = Knight(name, data['power'], data['hp'], weapon, armour, potion)
        new_knights.append(knight)
    # Pair the knights. Knight don't fight without pair
    return [
        (new_knights[i], new_knights[i + 1])
        for i in range(0, len(new_knights) - 1, 2)
    ]
