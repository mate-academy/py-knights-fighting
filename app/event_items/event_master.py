import time
from typing import Callable

import pygame

event_counter = 0


class Event:
    @staticmethod
    def narrative_speed(cps: float) -> Callable[[Callable[..., str]],
                                                Callable[..., None]]:
        def decorator(func: Callable[..., str]) -> Callable[..., None]:
            def wrapper(*args, **kwargs) -> str:
                text = str(func(*args, **kwargs))
                for char in text:
                    if char != "*":
                        print(char, end="", flush=True)
                        time.sleep(1 / cps)
                    else:
                        print(char, end="", flush=True)

            return wrapper

        return decorator

    @staticmethod
    def ambience() -> None:
        pygame.init()
        pygame.mixer.music.load(r"app\event_items\EVENT_AMBIENCE.mp3")
        pygame.mixer.music.play()

    @narrative_speed(cps=40)
    @staticmethod
    def event_start() -> str:
        print("*" * 79)
        print("\nIn the Kingdom of Mateland, "
              "in the mid to late XI-th century\n")
        with open(r"app\event_items\event_start.txt", "r") as file:
            text = file.read()
        time.sleep(3)
        return text

    @narrative_speed(cps=55)
    @staticmethod
    def event_fight(knight_1: object, knight_2: object) -> str:
        if knight_1.hp > knight_2.hp:
            winner = knight_1.name
            loser = knight_2.name
        else:
            winner = knight_2.name
            loser = knight_1.name
        global event_counter
        if event_counter == 0:
            event_path = r"app\event_items\event_fight_1.txt"
        else:
            event_path = r"app\event_items\event_fight_2.txt"
        with open(event_path, "r") as file:
            text = file.read().format(
                knight_1=knight_1.name,
                knight_1_hp=knight_1.hp,
                knight_1_weapon=knight_1.weapon["name"],
                knight_2=knight_2.name,
                knight_2_weapon=knight_2.weapon["name"],
                knight_2_hp=knight_2.hp,
                winner=winner,
                loser=loser)
        event_counter += 1
        time.sleep(3)
        return text

    @narrative_speed(cps=40)
    @staticmethod
    def event_result(result: dict) -> str:
        pygame.mixer.music.load(r"app\event_items\CHEERING_LOOP.ogg")
        pygame.mixer.music.play()
        items = result.items()
        result = [[k, v] for k, v in items]
        result.sort(key=lambda x: x[1], reverse=True)
        with open(r"app\event_items\event_result.txt", "r") as file:
            text = file.read().format(
                result=result)

        return text
