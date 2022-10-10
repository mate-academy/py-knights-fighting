class Knights:
    def __init__(self, lord: dict):
        self.name = lord["name"]
        self.hp = lord["hp"]
        self.power = lord["power"]
        self.protection = 0
        self.armour = lord["armour"]
        self.weapon = lord["weapon"]
        self.potion = lord["potion"]

    def preparations(self):
        # apply armour
        for armo in self.armour:
            self.protection += armo["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def main_battle(self, another):
        self.hp -= another.power - self.protection
        another.hp -= self.power - another.protection

        if self.hp <= 0:
            self.hp = 0

        if another.hp <= 0:
            another.hp = 0

    def battle_to_death(self, another):
        deaths = 0
        while deaths == 0:
            self.hp -= another.power - self.protection
            another.hp -= self.power - another.protection

            if self.hp <= 0:
                self.hp = 0
                deaths += 1

            if another.hp <= 0:
                another.hp = 0
                deaths += 1
        if deaths == 2:
            print(f"{self.name} and {another.name} are defeated!")
            return "Draw"
        if another.hp == 0:
            print(f"{another.name} is defeated in a fair fight!")
            print(f"{self.name} wins")
            return self
        if self.hp == 0:
            print(f"{self.name} is defeated in a fair fight!")
            print(f"{another.name} wins")
            return another

    @staticmethod
    def championship(members: list):
        finalists = [
            members[i].battle_to_death(members[i + 1])
            for i in range(0, len(members), 2)
        ]
        winner = finalists[0].battle_to_death(finalists[1])
        if winner == "Draw":
            print("All knights is dead")
            print("It was beautiful and spectacular championship")
        else:
            print(f"winner of championship is {winner.name}!")
