from app.services.battle import battle
from app.models.knight import KNIGHTS
if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
