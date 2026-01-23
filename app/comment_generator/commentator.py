import random
import textwrap
from typing import Generator


def generator_phrases_on_preparation() -> Generator[str, None, None]:
    phrases_to_preparation = [
        "{name} is suiting up in armor, struggling a bit. Maybe he "
        "shouldn't have had extra pie last night!",

        "Watch as {name} dons his helmet with flourish — oh, wait, "
        "it's backwards. Can someone help him out?",

        "Here comes {name}, brandishing his sword like swatting a "
        "fly. Let's hope his aim gets better before the battle!",

        "Sir {name} picked up his sword and... yep, he's talking "
        "to it again. It's just a regular sword, not Excalibur!",

        "Ah, {name} takes a swig of his mystery potion. Hopefully, "
        "it's a strength elixir, not last night's bean soup.",

        "And there's {name}, mistaking his shield for a dinner "
        "plate. Hopefully, he realizes before the battle starts."
    ]

    random.shuffle(phrases_to_preparation)
    for phrase in phrases_to_preparation:
        yield phrase


phrases_on_preparation = generator_phrases_on_preparation()


def comment_on_preparation(name: str) -> str:
    global phrases_on_preparation
    while True:
        try:
            message = next(phrases_on_preparation).format(name=name)
            return textwrap.fill(message, 95)
        except StopIteration:
            phrases_on_preparation = generator_phrases_on_preparation()
            continue


def generator_phrases_on_duel_ending() -> Generator[str, None, None]:
    end_of_duel_phrases = [
        "{winner} emerges victorious! {loser} might be counting "
        "stars after that knock!",

        "And it's over! {winner} stands tall, while {loser} is "
        "probably wondering what just happened.",

        "{winner} wins! As for {loser}, well, let's hope they "
        "remember their name after that!",

        "The battle is won! {winner} triumphs, and {loser}... "
        "better luck next time!",

        "{winner} has done it! Seems like {loser} is going to "
        "need a long rest after this duel.",

        "What a duel! {winner} takes the day, leaving {loser} to "
        "pick up their pride off the ground."
    ]

    random.shuffle(end_of_duel_phrases)
    for phrase in end_of_duel_phrases:
        yield phrase


phrases_on_duel_ending = generator_phrases_on_duel_ending()


def comment_of_end_duel(winner: str, loser: str) -> str:
    global phrases_on_duel_ending
    while True:
        try:
            return next(phrases_on_duel_ending).format(
                winner=winner, loser=loser)
        except StopIteration:
            phrases_on_duel_ending = generator_phrases_on_duel_ending()
            continue


def generator_ads() -> Generator[str, None, None]:
    duel_ads = [
        "Quench your thirst with 'Knight's Ale' – fit for a hero!",
        "'Sturdy Shields' – your trusted battle companion!",
        "Start your day with 'Warrior's Coffee'. Stay sharp!",
        "Heal swiftly with 'Nature's Potions' – nature's gift!",
        "Shine bright with 'Armor Glow' polish. Be seen!",
        "Power up with 'Battle Bars'. Fight longer!",
        "'Iron Underwear': Ultimate protection, ultimate comfort!",
        "Gallop to glory on 'Swift Steeds' – speed wins!",
        "'Blade Masters' – where sharpness meets mastery!",
        "Boost health with 'Magic Elixir'. Feel the magic!"
    ]
    random.shuffle(duel_ads)
    for ads in duel_ads:
        yield ads


advertising_message = generator_ads()


def advertising() -> str:
    global advertising_message
    while True:
        try:
            message = next(advertising_message)
            return message.center(95, "-")
        except StopIteration:
            advertising_message = generator_ads()
            continue


def generator_phrases_to_end_the_tournament() -> Generator[str, None, None]:
    phrases_to_end = [
        "And there we have it! {first_place} wins by not tripping over his "
        "own sword. {second_place} was so close, only distracted by a "
        "butterfly. {third_place} and {fourth_place} were too busy arguing "
        "about who had the shiniest armor!",

        "{first_place} emerges as the champion, mainly because his opponents, "
        "{second_place}, {third_place}, and {fourth_place}, were arguing "
        "about who forgot to bring the snacks to the duel.",

        "What a turn of events! {first_place} wins just by staying awake "
        "longer than {second_place}, while {third_place} and {fourth_place} "
        "were caught napping on horseback!",

        "In a surprising twist, {first_place} wins after {second_place}, "
        "{third_place}, and {fourth_place} got lost on the way to the arena "
        "and ended up at a nearby tavern instead.",

        "Miraculously, {first_place} claims victory after {second_place}, "
        "{third_place}, and {fourth_place} were too busy taking selfies to "
        "actually fight.",

        "As the dust settles, {first_place} stands victorious, mainly because "
        "{second_place}, {third_place}, and {fourth_place} were playing "
        "rock-paper-scissors to decide who should win."
    ]

    random.shuffle(phrases_to_end)
    for phrase in phrases_to_end:
        yield phrase


final_message = generator_phrases_to_end_the_tournament()


def the_results_of_the_match(
        first_place: str,
        second_place: str,
        third_place: str,
        fourth_place: str
) -> str:
    global final_message
    while True:
        try:
            message = next(final_message).format(
                first_place=first_place,
                second_place=second_place,
                third_place=third_place,
                fourth_place=fourth_place
            )
            return textwrap.fill(message, 95)
        except StopIteration:
            final_message = generator_phrases_to_end_the_tournament()
            continue
