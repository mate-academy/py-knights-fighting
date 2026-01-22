class Potion:
    def __init__(self, name: str, effects: dict):
        self.name = name
        self.effects = effects

    def get_effects(self) -> dict[str, int]:
        
        return {effect: self.effects.get(effect, 0) for effect in self.effects}