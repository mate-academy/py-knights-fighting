class Battle:
    @staticmethod
    def do_battle(hp: int, power: int, protection: int) -> int:
        print(f"""
            {hp=}
            {power=}
            {protection=}
            {hp - (power - protection)=}
        """)
        return hp - (power - protection)

    @staticmethod
    def hp_to_zero(hp: int) -> int:
        return 0 if hp < 0 else hp
