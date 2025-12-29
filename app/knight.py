class Knight:
    def __init__(self, name, hp, power, armour, weapon, potion):
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        
        # 1. Aplicar Proteção da Armadura (pode ser mais de uma parte)
        for part in armour:
            self.protection += part["protection"]
            
        # 2. Aplicar Poder da Arma
        self.power += weapon["power"]
        
        # 3. Aplicar Efeitos da Poção (se existir)
        if potion:
            self.hp += potion["effect"].get("hp", 0)
            self.power += potion["effect"].get("power", 0)
            self.protection += potion["effect"].get("protection", 0)

    def __repr__(self):
        """Opcional: ajuda a visualizar o objeto durante o debug"""
        return f"Knight(name={self.name}, hp={self.hp})"
