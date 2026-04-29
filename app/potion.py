class Potion:
    def __init__(self, potion_dict: dict) -> None:

        self._name = None
        self._effect_dict = None
        self._power_effect = 0
        self._hp_effect = 0
        self._protection_effect = 0
        if potion_dict is not None:
            self._name = potion_dict["name"]

            if "effect" in potion_dict and potion_dict["effect"] is not None:
                self._effect_dict = potion_dict["effect"]
                effect_dict = potion_dict["effect"]

                for effect in effect_dict:
                    if effect == "power":
                        self._power_effect = effect_dict[effect]
                    elif effect == "hp":
                        self._hp_effect = effect_dict[effect]
                    elif effect == "protection":
                        self._protection_effect = effect_dict[effect]

    @property
    def name(self) -> str:
        return self._name

    @property
    def power_effect(self) -> int:
        return self._power_effect

    @property
    def hp_effect(self) -> int:
        return self._hp_effect

    @property
    def protection_effect(self) -> int:
        return self._protection_effect
