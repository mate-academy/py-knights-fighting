from app.entities.equipment import calculate_protection, apply_potion

class Knight:
  def __init__(self, config):
    self.name = config["name"]
    self.base_power = config["power"]
    self.base_hp = config["hp"]
    self.armour = config.get("armour", [])
    self.weapon = config["weapon"]
    self.potion = config.get("potion")

    self.hp = self.base_hp
    self.power = self.base_power + self.weapon["power"]
    self.protection = calculate_protection(self.armour)

    if self.potion:
      apply_potion(self, self.potion["effect"])
