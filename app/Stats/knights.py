from app.Stats.equipment import Equipment


class Knight:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary["name"]
        self.power = dictionary["power"]
        self.hp = dictionary["hp"]
        self.prot = 0
        self.equip = Equipment(dictionary["weapon"],
                               dictionary["armour"],
                               dictionary["potion"]
                               )

    def ready_for_battle(self) -> None:
        """
        this method could be implemented in init but separating them
         allows knights to go to fight without equipment ready if necessary
        :return: None
        """
        needed_equipment = ", ".join(self.equip.equip_list)
        print(f"{self.name} equipment is {needed_equipment}")

        self.power += self.equip.power_boost
        self.hp += self.equip.hp_boost
        self.prot += self.equip.prot
