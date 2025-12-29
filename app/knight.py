class Knight:
    def __init__(self, config):
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        # Aplicar Armadura
        for armour_part in config["armour"]:
            self.protection += armour_part["protection"]

        # Aplicar Arma
        self.power += config["weapon"]["power"]

        # Aplicar Poção (se existir)
        potion = config.get("potion")
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def receive_damage(self, opponent_power):
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage
        
        # Garante que o HP não seja negativo
        if self.hp < 0:
            self.hp = 0
