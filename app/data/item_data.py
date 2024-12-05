class ItemData:
    def __init__(self, config: dict):
        if config.get("name", None):
            self.name = config.get("name")
        elif config.get("part", None):
            self.name = config.get("part")
        else:
            self.name = "Item"

        self.effect = config.get("effect", None)
        self.power = config.get("power", 0)
        self.protection = config.get("protection", 0)
