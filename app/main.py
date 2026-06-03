from app.Data.knights import KNIGHTS
from app.Services.factory import KnightFactory
from app.Services.battle import battle

knights = KnightFactory.create_knights(KNIGHTS)

for key, knight in knights.items():
    print(f"{key}: {type(knight)}")

result = battle(knights)
print(result)
