def calculate_protection(armour_parts):
  return sum(part["protection"] for part in armour_parts)

def apply_potion(knight, effects):
  knight.hp += effects.get("hp", 0)
  knight.power += effects.get("power", 0)
  knight.protection += effects.get("protection", 0)
