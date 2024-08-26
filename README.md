# Knights Fighting

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

## Story

In the Kingdom of Camelot the greatest championship of
knights is taking place. The most powerful and strong
knights ready to give their lives here. So, lets the battle begin!

At first, you have knights stats as dictionary:
```python
KNIGHTS = {
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    }
    # ...
}
```
So basically, each knight has `name`, `power` and `hp` (Health Points).

Additionally, knights have:
- `armour` with `name` and `protection` (more than 1 part of armour is possible, 0 armour also possible).
  - All armour is applied to each knight before entering the battle.
  - Armour adds additional stat to knight, known as `protection`.
  - Base protection of unarmoured knight is always 0.
  - Armour is additional, so `helmet` with 10 `protection` and `boots` with 5 `protection` means 15 `protection` in total.
- `weapon` with `name` and `power` (everyone has exactly one weapon, because knights cannot fight unarmed opponent).
  - Weapon is applied to each knight before entering the battle.
  - Weapon makes knight more powerful - it just add-up with basic knight `power`.
- `potion` with `name` and `effect` (effects may be somehow positive and somehow negative). Potion may exist, but may be just `None` also.
  - Potion (if exists) is applied to each knight before entering the battle.
  - Potion `effect` may improve/worsen one of 3 main stats of knight: `hp`, `power` or `protection`.
  - If `effect` value is positive - it improves this stat on that value, if negative - worsen.

So, for `red_knight` we have before the battle next stats:
```python
red_knight_stats = {
    "hp": 80,  # 70 + 10
    "power": 90,  # 40 + 45 + 5
    "protection": 25,  # 0 + 25
}
```

Imagine, that another knight (let us call him `x_knight`) has next stats before battle:
```python
x_knight_stats = {
    "hp": 100,
    "power": 70,
    "protection": 35,
}
```

When the battle begins between them:
- They lose their `hp` based on `power` of opponent and self `protection` using next formula:
```python
red_knight_stats["hp"] -= x_knight_stats["power"] - red_knight_stats["protection"]
x_knight_stats["hp"] -= red_knight_stats["power"] - x_knight_stats["protection"]
```

So the result `hp` of this battle is:
```python
battle_result_hp = {
    "Red Knight": 35,  # 80 - (70 - 25)
    "X Knight": 45,  # 100 - (90 - 35)
}
```

In this battle no one fell, but if someone will have `hp <= 0` - it means
this knight is defeated - and his `hp` must be equal to `0`.

## Task
So up to this moment, you will have `KNIGHTS` config with parameters
of 4 knights in Kingdom: `Lancelot`, `Arthur`, `Mordred` and `Red Knight`.

It is already chosen, that `Lancelot` is battling versus `Mordred` and
`Arthur` versus `Red Knight`.

In the code (`app/main.py`) you already have everything ready for calculation the result of the battle.
(All tests are passing, if you run `pytest`).

But you will notice, that it is achieved not in the best-practice way of coding.

So, your task will be next: 
- Make this code work in more `best-practice` way.
- Split functionality to different `modules` and `packages` as you think will be the most meaningful.
- `Refactor` existing logic, if needed.
- Be as `creative` as possible - in this task you are not obliged to write everything by our scenario.
- Use classes if you like classes (preferable), and use functions, if you like functions (functions also ok here).
- Make sure, that your final code pass `flake8` and `pytest`

Obligations:
- In this task we test only 1 `battle` function from `app.main` - make sure it works 
  correctly after all your changes applied to the project.

P.S: You could add your own logic to this project, if you want: just be creative here :)

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
