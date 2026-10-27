import random
import re

import wikipediaapi


# Schlüssel: englischer Name, Wert: deutscher Name
CAPITALS = {
    "Amsterdam": "Amsterdam",
    "Athens": "Athen",
    "Berlin": "Berlin",
    "Bratislava": "Bratislava",
    "Brussels": "Brüssel",
    "Bucharest": "Bukarest",
    "Budapest": "Budapest",
    "Copenhagen": "Kopenhagen",
    "Dublin": "Dublin",
    "Helsinki": "Helsinki",
    "Lisbon": "Lissabon",
    "Ljubljana": "Ljubljana",
    "Luxembourg": "Luxemburg",
    "Madrid": "Madrid",
    "Nicosia": "Nikosia",
    "Paris": "Paris",
    "Prague": "Prag",
    "Riga": "Riga",
    "Rome": "Rom",
    "Sofia": "Sofia",
    "Stockholm": "Stockholm",
    "Tallinn": "Tallinn",
    "Valletta": "Valletta",
    "Vienna": "Wien",
    "Vilnius": "Vilnius",
    "Warsaw": "Warschau",
    "Zagreb": "Zagreb",
}

TEXTS = {
    "en": {
        "welcome": "Welcome to CAPITAL CLUES!",
        "first_clue": "Here comes the first clue:",
        "question": "Which capital are we looking for? ",
        "correct": "Correct!",
        "wrong": "Wrong! Here comes another clue:",
        "invalid_language": "Invalid selection. Please choose 1 or 2.",
        "page_error": "No Wikipedia page found for",
        "clue_error": "No usable clues found for",
    },
    "de": {
        "welcome": "Willkommen bei CAPITAL CLUES!",
        "first_clue": "Hier kommt der erste Hinweis:",
        "question": "Welche Hauptstadt suchen wir? ",
        "correct": "Richtig!",
        "wrong": "Falsch! Hier kommt ein weiterer Hinweis:",
        "invalid_language": "Ungültige Auswahl. Bitte wähle 1 oder 2.",
        "page_error": "Keine Wikipedia-Seite gefunden für",
        "clue_error": "Keine passenden Hinweise gefunden für",
    },
}


def create_wikipedia_client(language):
    return wikipediaapi.Wikipedia(
        user_agent="CapitalQuiz/1.0 (deine-echte-email@example.com)",
        language=language,
    )


def redact_city(sentence, city):
    pattern = r"\b" + re.escape(city) + r"\w*"
    return re.sub(pattern, "XXX", sentence, flags=re.IGNORECASE)


def get_clues(city, wiki, texts):
    page = wiki.page(city)

    if not page.exists():
        raise ValueError(f"{texts['page_error']} {city}.")

    sentences = [
        sentence.strip()
        for sentence in page.text.split(". ")
        if len(sentence.strip()) > 40
    ]

    if not sentences:
        raise ValueError(f"{texts['clue_error']} {city}.")

    return sentences


def play_game(language):
    texts = TEXTS[language]
    wiki = create_wikipedia_client(language)

    capital_en = random.choice(list(CAPITALS))
    correct_answer = CAPITALS[capital_en] if language == "de" else capital_en

    clues = get_clues(correct_answer, wiki, texts)

    print(f"\n{texts['welcome']}\n")
    print(texts["first_clue"])

    first_clue = redact_city(random.choice(clues), correct_answer)
    print(f'"{first_clue}"')

    while True:
        guess = input(texts["question"]).strip()

        if guess.casefold() == correct_answer.casefold():
            print(texts["correct"])
            break

        print(f"\n{texts['wrong']}")
        next_clue = redact_city(random.choice(clues), correct_answer)
        print(f'"{next_clue}"')


def menu():
    print("\n1. English\n2. Deutsch")
    choice = input("Please select a language / Bitte Sprache wählen: ").strip()

    if choice == "1":
        play_game("en")
    elif choice == "2":
        play_game("de")
    else:
        print(TEXTS["de"]["invalid_language"])


def main():
    menu()


if __name__ == "__main__":
    main()