from app.main import battle
from app.config import KNIGHTS

def test_battle_results():
    results = battle(KNIGHTS)
    assert "Lancelot vs Mordred" in results
    assert "Arthur vs Red Knight" in results

    for match in results.values():
        for hp in match.values():
            assert isinstance(hp, int)
            assert hp >= 0