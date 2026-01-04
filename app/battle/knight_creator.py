class Knight:

    def __init__(
            self,
            knight_nik: str,
            knight_params: dict,
            list_order: int
    ) -> object:

        """
        Args:
            knight_nik (str):
            The nickname of the Knight.

            knight_params (dict):
            The dictionary containing the parameters of the Knight.

            list_order (int):
            The position of the Knight in the list.

        Returns:
            object: The Knight object.
        """

        self.nik = knight_nik
        self.name = knight_params["name"]
        self.power = knight_params["power"]
        self.hp = knight_params["hp"]
        self.armour = self.full_armour(knight_params["armour"])
        self.weapon = knight_params["weapon"]
        self.potion = knight_params["potion"]
        self.list_order = list_order

    def __repr__(self) -> str:
        # Returns a string representation of the knight.

        return f"{self.name} - Health: {self.hp}"

    def __str__(self) -> str:
        # Returns a string representation of the knight.

        return f"{self.name} - Health: {self.hp}"

    def __getitem__(self, key: str) -> str:
        # Returns the value of the specified attribute.

        return getattr(self, key)

    def full_armour(self, armour: list) -> int:
        """
        Calculates the total armour value
        by adding up the protection values of each armour part.
        """
        output_armour = 0
        for part in armour:
            output_armour += part["protection"]
        return output_armour

    def use_potion(self) -> None:
        # Check if the Knight has a potion and apply its effects.

        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if key == "power":
                    self.power += value
                if key == "hp":
                    self.hp += value
                if key == "protection":
                    self.armour += value

    def attack(self) -> int:
        """
        Calculates the Knight's attack value as the sum
        of their power and weapon power.
        """

        return sum([self.power, self.weapon["power"]])

    def defence(self, damage: int) -> None:
        """
        Reduces the Knight's hp by the amount of damage they received
        minus their armour value.
        """
        self.hp -= damage - self.armour

        # Set the Knight's hp to 0 if it falls below 0.
        if self.hp <= 0:
            self.hp = 0
