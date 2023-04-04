class ApplyPotion:

    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config

        if self.knights_config["potion"] is not None:
            if "power" in self.knights_config["potion"]["effect"]:
                self.knights_config["power"] += \
                    self.knights_config["potion"]["effect"]["power"]

            if "protection" in self.knights_config["potion"]["effect"]:
                self.knights_config["protection"] += \
                    self.knights_config["potion"]["effect"]["protection"]

            if "hp" in self.knights_config["potion"]["effect"]:
                self.knights_config["hp"] += \
                    self.knights_config["potion"]["effect"]["hp"]
