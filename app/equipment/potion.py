from __future__ import annotations


class Potion:
    def __init__(self, potion: dict | None) -> None:
        if potion is not None:
            self.name = potion["name"]
            self.power_effect = (potion["effect"]["power"]
                                 if "power" in potion["effect"] else 0)
            self.hp_effect = (potion["effect"]["hp"]
                              if "hp" in potion["effect"] else 0)
            self.protection_effect = (potion["effect"]["protection"]
                                      if "protection" in potion["effect"]
                                      else 0)
        else:
            self.name = None
            self.power_effect = 0
            self.hp_effect = 0
            self.protection_effect = 0
