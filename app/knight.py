class Knight:
    # Adicionamos 'dict' para o config e 'None' para o retorno
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.power: int = config["power"]
        self.protection: int = 0

        for armour_part in config["armour"]:
            self.protection += armour_part["protection"]

        self.power += config["weapon"]["power"]

        potion = config.get("potion")
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    # Adicionamos 'int' para o dano e 'None' para o retorno
    def receive_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage
        
        if self.hp < 0:
            self.hp = 0
