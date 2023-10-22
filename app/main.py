from app.knight import Knight

# Create Knights
Arthur = Knight("Arthur", 45, 75)
Lancelot = Knight("Lancelot", 50, 75)
Mordred = Knight("Mordred", 30, 90)
Red_Knight = Knight("Red_Knight", 40, 70)

# first battle
print("""

    FIRST BATTLE:
    
""")
Knight.versus("Lancelot", "Mordred")

# second battle
print("""

    SECOND BATTLE:

""")
Knight.versus("Arthur", "Red_Knight")
