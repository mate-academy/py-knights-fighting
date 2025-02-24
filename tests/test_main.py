import pytest
from app.knight import Knight
from app.battle import battle

@pytest.mark.parametrize(
    "knight1, knight2, expected",
    [
        (
            {"name": "Knight A", "power": 50, "hp": 100, "armour": [{"part": "helmet", "protection": 10}],
             "weapon": {"name": "Axe", "power": 30}, "potion": None},
            {"name": "Knight B", "power": 60, "hp": 100, "armour": [{"part": "chestplate", "protection": 20}],
             "weapon": {"name": "Sword", "power": 25}, "potion": None},
            {"Knight A": 25, "Knight B": 40}  # Оновлений очікуваний результат
        ),
    ]
)
def test_battle(knight1, knight2, expected):
    k1 = Knight(**knight1)
    k2 = Knight(**knight2)
    assert battle(k1, k2) == expected