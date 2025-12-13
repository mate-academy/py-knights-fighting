from app.main import battle
from app.config import KNIGHTS

def test_battle_results():
    results = battle(KNIGHTS)

    expected_names = ["Arthur", "Lancelot", "Mordred", "Red Knight"]
    for name in expected_names:
        assert name in results
        assert isinstance(results[name], int)
        assert results[name] >= 0
