import random
import re

import wikipediaapi


CAPITALS = [
    "Amsterdam",
    "Athens",
    "Berlin",
    "Bratislava",
    "Brussels",
    "Bucharest",
    "Budapest",
    "Copenhagen",
    "Dublin",
    "Helsinki",
    "Lisbon",
    "Ljubljana",
    "Luxembourg",
    "Madrid",
    "Nicosia",
    "Paris",
    "Prague",
    "Riga",
    "Rome",
    "Sofia",
    "Stockholm",
    "Tallinn",
    "Valletta",
    "Vienna",
    "Vilnius",
    "Warsaw",
    "Zagreb",
]


def create_wikipedia_client():
    return wikipediaapi.Wikipedia(
        user_agent="CapitalQuiz/1.0 (your-email@example.com)",
        language="en",
    )


def redact_city(sentence, city):
    pattern = r"\b" + re.escape(city) + r"\w*"
    return re.sub(pattern, "XXX", sentence, flags=re.IGNORECASE)


def get_clues(city, wiki):
    page = wiki.page(city)

    if not page.exists():
        raise ValueError(f"No Wikipedia page found for {city}.")

    sentences = [
        sentence.strip()
        for sentence in page.text.split(". ")
        if len(sentence.strip()) > 40
    ]

    if not sentences:
        raise ValueError(f"No usable clues found for {city}.")

    return sentences


def play_game():
    wiki = create_wikipedia_client()
    correct_answer = random.choice(CAPITALS)
    clues = get_clues(correct_answer, wiki)

    print("Welcome to CAPITAL CLUES!\n")
    print("Here comes the first clue:")

    first_clue = redact_city(random.choice(clues), correct_answer)
    print(f'"{first_clue}"')

    while True:
        guess = input("\nWhich capital are we looking for? ").strip()

        if guess.casefold() == correct_answer.casefold():
            print("Correct!")
            break

        print("\nWrong! Here comes another clue:")
        next_clue = redact_city(random.choice(clues), correct_answer)
        print(f'"{next_clue}"')


def main():
    play_game()


if __name__ == "__main__":
    main()