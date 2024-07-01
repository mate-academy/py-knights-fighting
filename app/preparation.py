from app.knights import Knight


class Preparation:
    def __init__(self, knight: Knight) -> None:
        self.knight = knight

    def full_preparation(self) -> None:
        setattr(
            self.knight, "power",
            getattr(self.knight, "power")
            + self.knight.weapon["power"]
        )

        for armour in self.knight.armour:
            setattr(
                self.knight, "protection",
                getattr(self.knight, "protection")
                + armour["protection"]
            )

        if self.knight.potion is not None:
            for name, boost in self.knight.potion["effect"].items():
                if name == "protection":
                    setattr(
                        self.knight, "protection",
                        getattr(self.knight, "protection")
                        + boost
                    )
                if name == "power":
                    setattr(
                        self.knight, "power",
                        getattr(self.knight, "power")
                        + boost
                    )
                if name == "armour":
                    setattr(
                        self.knight, "armour",
                        getattr(self.knight, "armour")
                        + boost
                    )
                if name == "hp":
                    setattr(
                        self.knight, "hp",
                        getattr(self.knight, "hp")
                        + boost
                    )
