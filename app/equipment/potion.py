from app.keys import KeysPotion


class Potion:
    def __init__(self, dict_potion: dict) -> None:
        if dict_potion is not None:
            self.name = dict_potion[KeysPotion.NAME.value]
            self.effect = dict_potion[KeysPotion.EFFECT.value]
