class Buffs:
    def __init__(self, buffs: dict):
        self.buffs = buffs

    def take_buff(self, knight):
        merlin_spell = {"hp": 0,
                        "protection": 0,
                        "power": 0}

        if self.buffs is not None:
            for baf in merlin_spell:
                if baf in self.buffs["effect"]:
                    merlin_spell[baf] += self.buffs["effect"][baf]

        knight.hp += merlin_spell.get("hp")
        knight.protection += merlin_spell.get("protection")
        knight.power += merlin_spell.get("power")
