def perform_battle(knight1, knight2):
    # Simulate battle logic (simplified for illustration)
    # Adjust the logic to fit your battle simulation requirements
    
    # Apply damage based on power and protection
    damage_to_knight2 = max(0, knight1.power - knight2.protection)
    damage_to_knight1 = max(0, knight2.power - knight1.protection)
    
    # Update HPs
    knight1.hp -= damage_to_knight1
    knight2.hp -= damage_to_knight2
    
    # Ensure HP doesn't drop below 0
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
    
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}