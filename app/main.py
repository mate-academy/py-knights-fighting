from app.Data.knights import KNIGHTS
from app.Services.factory import KnightFactory
from app.Services.battle import battle

knights = KnightFactory.create_knights(KNIGHTS)
result = battle(knights)
print(result)
