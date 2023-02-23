from app.hall.fighters import Fighters


class Prepare(Fighters):
    def fighter_preparation(self) -> None:
        self.armour_prepare()
        self.weapon_prepare()
        self.potion_prepare()

    def armour_prepare(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def weapon_prepare(self) -> None:
        self.power += self.weapon["power"]

    def potion_prepare(self) -> None:
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                old_value = getattr(self, key)
                setattr(self, key, old_value + value)
