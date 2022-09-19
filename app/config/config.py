from app.Heroes_and_Battle.fighters import Fighter
from app.Heroes_and_Battle.battle import Battle


class Preparation:
    def __init__(self, config: dict):
        self.config = config

    def start_of_tournament(self) -> dict:
        print("Lancelot drink points,"
              " sharpens her sword and ready to "
              "Battle!"
              )

        lancelot = Fighter(self.config["lancelot"])
        lancelot.take_ammunition()

        print("Mordred hungers for blood "
              "and ready to Battle!"
              )

        mordred = Fighter(self.config["mordred"])
        mordred.take_ammunition()

        print("Arthur took out Excalibur from"
              " a stone and ready to Battle!"
              )

        arthur = Fighter(self.config["arthur"])
        arthur.take_ammunition()

        print("Red_knight dismounted from the"
              " saddle, adjusted the rusty armor"
              )

        red_knight = Fighter(self.config["red_knight"])
        red_knight.take_ammunition()

        print(" ")
        print("Let the Battle begin!")
        print(" ")
        part1 = Battle(lancelot, mordred)
        part2 = Battle(arthur, red_knight)

        part1.result_of_battle()
        print("Round one:")
        part1.result_of_round()

        print(" ")

        print("Round two:")
        part2.result_of_battle()
        part2.result_of_round()

        print(" ")
        print("Tournament is over, results:")
        return {
            lancelot.name: lancelot.hp,
            mordred.name: mordred.hp,
            arthur.name: arthur.hp,
            red_knight.name: red_knight.hp
        }
