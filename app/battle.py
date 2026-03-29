from knight import Knight


    def battle(knights_config, self=None):
        knights = {k: Knight(v) for k, v in knights_config.items()}
        for knight in knights.values():
            knight.prepare_for_battle()

            self.apply_potion()

        def attack(self, opponent):
            opponent.hp -= max(self.power - opponent.protection, 0)
            opponent.hp = max(opponent.hp, 0)

    def battle(knights_config):
        knights = {k: Knight(v) for k, v in knights_config.items()}
        for knight in knights.values():
            knight.prepare_for_battle()

        knights["lancelot"].attack(knights["mordred"])
        knights["mordred"].attack(knights["lancelot"])

        knights["arthur"].attack(knights["red_knight"])
        knights["red_knight"].attack(knights["arthur"])

        return {
            knights["lancelot"].name: knights["lancelot"].hp,
            knights["arthur"].name: knights["arthur"].hp,
            knights["mordred"].name: knights["mordred"].hp,
            knights["red_knight"].name: knights["red_knight"].hp,
        }
