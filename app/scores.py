from app.knights_stats1 import TheKnight


class Scores:

    @staticmethod
    def battle_scores(contender1: TheKnight, contender2: TheKnight) -> dict:
        print(f"The battle between {contender1.name} "
              f"and {contender2.name} started!")
        contender1.hp -= contender2.power - contender1.protection
        contender2.hp -= contender1.power - contender2.protection
        if contender1.hp < 0:
            contender1.hp = 0
            print(f"{contender1.name} fell! "
                  f"Congratulations to {contender2.name}!")
        elif contender2.hp < 0:
            contender2.hp = 0
            print(f"{contender2.name} fell! "
                  f"Congratulations to {contender1.name}!")
        else:
            print("Both knights survived in this battle")
        return {contender1.name: contender1.hp, contender2.name: contender2.hp}
