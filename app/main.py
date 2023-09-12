from app.knights_dict.config import KNIGHTS
from app.knights_dict.knights import Knights


knight = Knights(KNIGHTS)

lancelot = knight.knight_kingdom("lancelot")
arthur = knight.knight_kingdom("arthur")
mordred = knight.knight_kingdom("mordred")
red_knight = knight.knight_kingdom("red_knight")

# -------------------------------------------------------------------------------
# BATTLE:

# 1 Lancelot vs Mordred:
lancelot["hp"] -= mordred["power"] - lancelot["protection"]
mordred["hp"] -= lancelot["power"] - mordred["protection"]

# check if someone fell in battle
if lancelot["hp"] <= 0:
    lancelot["hp"] = 0

if mordred["hp"] <= 0:
    mordred["hp"] = 0

# 2 Arthur vs Red Knight:
arthur["hp"] -= red_knight["power"] - arthur["protection"]
red_knight["hp"] -= arthur["power"] - red_knight["protection"]

# check if someone fell in battle
if arthur["hp"] <= 0:
    arthur["hp"] = 0

if red_knight["hp"] <= 0:
    red_knight["hp"] = 0

# Print battle results:
print({
    lancelot["name"]: lancelot["hp"],
    arthur["name"]: arthur["hp"],
    mordred["name"]: mordred["hp"],
    red_knight["name"]: red_knight["hp"],
})
