class Battle:
    def __init__(self, knight_a, knight_b):
        self.knight_a = knight_a
        self.knight_b = knight_b

    def execute(self):
        self.knight_a.calculate_stats()
        self.knight_b.calculate_stats()

        damage_to_a = max(0, self.knight_b.effective_power - self.knight_a.protection)
        damage_to_b = max(0, self.knight_a.effective_power - self.knight_b.protection)

        self.knight_a.take_damage(damage_to_a)
        self.knight_b.take_damage(damage_to_b)

        return {
            self.knight_a.name: self.knight_a.effective_hp,
            self.knight_b.name: self.knight_b.effective_hp
        }
