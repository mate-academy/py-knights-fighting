from app.main import battle, KNIGHTS


def test_battle_result():
    result = battle(KNIGHTS)
    assert isinstance(result, dict)
    assert all(isinstance(hp, int) for hp in result.values())
    assert set(result.keys()) == {"Lancelot", "Arthur", "Mordred", "Red Knight"}
