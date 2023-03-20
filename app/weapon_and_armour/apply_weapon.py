class ApplyWeapon:
    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config
        self.knights_config["power"] += \
            self.knights_config["weapon_and_armour"]["power"]
