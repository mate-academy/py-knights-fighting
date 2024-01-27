from app.knights_battle.knight import Knight



def battle(knightsConfig):
    
    knights = {}

  
    for name, details in knightsConfig.items():
        
        knights[name] = Knight(name=details["name"], power=details["power"], 
                               hp=details["hp"], armour=details["armour"], 
                               weapon=details["weapon"], potion=details["potion"])
    

    
    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    simulate_fight(knights["lancelot"], knights["mordred"])
    simulate_fight(knights["arthur"], knights["red_knight"])

    # Prepare and return battle results
    return {knight.name: knight.hp for knight in knights.values()}

def simulate_fight(knight1, knight2):
    # Calculate the battle outcome between two knights
    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)

    # Ensure HP does not fall below zero
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
