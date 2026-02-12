from app.armament.armour import Armour
from app.armament.potion import Potion
from app.armament.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict[str: str | int],
                 potion: dict[str: str | dict[str: int]] | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp

        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.total_power = power
        self.total_armour = 0

    @classmethod
    def from_dict(cls, data: dict) -> "Knight":
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"]
        )

    def apply_armour(self) -> None:
        if self.armour:
            self.armour = [Armour.from_dict(armour) for armour in self.armour]
            self.total_armour = sum([ar.protection for ar in self.armour])

    def apply_weapon(self) -> None:
        self.weapon = Weapon.from_dict(self.weapon)
        self.total_power += self.weapon.power

    def drink_potion(self) -> None:
        if self.potion is not None:
            self.potion = Potion(self.potion["name"], self.potion["effect"])
            self.hp += self.potion.hp
            self.total_power += self.potion.power
            self.total_armour += self.potion.armour

    def take_damage(self, damage: int) -> None:
        print("Hp:", self.hp, " armour:",
              self.total_armour, " damage:", damage)
        self.hp += self.total_armour - damage
        if self.hp < 0:
            self.hp = 0

    def get_hp(self) -> int:
        return self.hp

    def get_stats(self) -> None:
        print(f"\n⚔️ Knight Stats: {self.name}")
        print("-" * 40)
        print(f"💪 Base Power: {self.power}")
        print(f"🛡️  Total Armour: {self.total_armour}")
        print(f"⚔️  Total Power: {self.total_power}")
        print(f"❤️  HP: {self.hp}")

        print("\n🗡️  Weapon:")
        if isinstance(self.weapon, Weapon):
            print(f"   • {self.weapon.name} (Power +{self.weapon.power})")
        else:
            print("   • None")

        print("\n🥾 Armour:")
        if (isinstance(self.armour, list)
                and all(isinstance(a, Armour) for a in self.armour)):
            for armour_piece in self.armour:
                print(
                    f"   • {armour_piece.part} (+{armour_piece.protection})"
                )
        else:
            print("   • None")

        print("\n🧪 Potion:")
        if isinstance(self.potion, Potion):
            print(f"   • {self.potion.name} "
                  f"(HP +{self.potion.hp}, "
                  f"Power +{self.potion.power}, "
                  f"Armour +{self.potion.armour})")
        else:
            print("   • None")

        print("-" * 40)
