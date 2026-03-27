from app.AppPackage.Items.Armour import Armour
from app.AppPackage.Items.Weapon import Weapon


class Character:
    def __init__(self, character_data: dict) -> None:
        self.name = character_data["name"]
        self.power = character_data["power"]
        self.hp = character_data["hp"]
        self.armour = Armour(character_data["armour"])
        self.weapon = Weapon(character_data["weapon"])

        if character_data.get("potion") is not None:
            self.apply_potion(character_data["potion"]["effect"])

    def apply_potion(self, effect_data: dict) -> None:
        if effect_data.get("power") is not None:
            self.power += effect_data["power"]
        if effect_data.get("hp") is not None:
            self.hp += effect_data["hp"]
        if effect_data.get("protection") is not None:
            self.armour.protection += effect_data["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def am_i_dead(self) -> None:
        if self.hp <= 0:
            print(f"{self.name} is dead!")
            self.hp = 0

    def fight(self, initiator: "Character") -> None:
        self.hp -= initiator.power - self.armour.protection
        print(
            f"\n{self.name}: \nhp: {self.hp}\narm: "
            f"{self.armour.protection}\npower: {self.power}"
        )
        print(
            f"{initiator.name}: \nhp: {initiator.hp}\narm: "
            f"{initiator.armour.protection}\npower: {initiator.power}\n"
        )
        initiator.hp -= self.power - initiator.armour.protection

        self.am_i_dead()
        initiator.am_i_dead()
