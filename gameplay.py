import random
import re
import wikipediaapi


def welcome_message():
    print("\nWelcome to the Wikipedia Guessing Game!")
    print("Choose a category and guess the correct answer.")
    print("Good luck!")


def instructions():
    print("\nHow to play:")
    print("1. Choose a category.")
    print("2. Read the sentences from the Wikipedia article sentences.")
    print("3. Guess the correct answer.")
    print("4. You have 5 attempts to guess the correct answer.")
    print("5. If your answer is incorrect, you will receive a hint.")
    print("6. Try to guess the correct answer!")


def choose_category():
    categories = {
        "1": "Cities",
        "2": "Countries",
        "3": "Celebrities",
        "4": "National dishes",
    }

    print("\nChoose a category:")
    for number, category in categories.items():
        print(f"{number}. {category}")

    while True:
        choice = input("Your choice: ")

        if choice in categories:
            return categories[choice]

        print("Invalid choice. Please try again.")


def get_article_sentences(article_text):
    """Splits a Wikipedia article into individual sentences."""
    sentences = re.split(r"(?<=[.!?])\s+", article_text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def play_round():
    """Runs one round of the Wikipedia guessing game."""
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="Wiki-Game/1.0 (annecke@gmail.com)",
        language="en",
    )

    page = wiki_wiki.page("Berlin")

    if not page.exists():
        print("The Wikipedia article could not be found.")
        return

    print("\nA new guessing round begins!")
    print("Which capital city are you looking for?")

    # Temporary test: display the beginning of the article.
    print("\nArticle text preview:")
    sentences = get_article_sentences(page.text)

    print("\nFirst three sentences from Wikipedia:")
    for sentence in sentences[:3]:
        print("-", sentence)

    correct_answer = page.title
    guess = input("Your answer: ")

    if check_answer(guess, correct_answer):
        print("Correct!")
    else:
        print("Incorrect! Here is a new hint:")
        print(page.summary)


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


def check_answer(user_input, correct_answer):
    """Checks the player's answer."""
    return user_input.strip().lower() == correct_answer.strip().lower()


def show_attempts(attempts):
    """Displays the number of attempts needed to find the correct answer."""
    print(f"\nYou found the correct answer in {attempts} attempts!")


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

## complete_content = page_py.text
## list_of_sentences = complete_content.split(". ")
## list_of_sentences = [s.strip() for s in list_of_sentences if len(s.strip()) > 40 and len(s.strip()) < 200]
## first_random_sentence = random.choice(list_of_sentences)
## first_redacted_sentence = redact_city(first_random_sentence, correct_answer)

    # Korrigierter Abschnitt: vorhandene Sätze weiterverwenden
    sentences = [
        sentence for sentence in sentences
        if len(sentence) < 200
    ]

    if not sentences:
        raise ValueError(f"{texts['clue_error']} {city}.")

    return sentences


def play_game(language):
    texts = TEXTS[language]
##     wiki = create_wikipedia_client(language)
## wrong_attempts = 0
##
## wrong_options = random.sample(
##     [city for city in capitals if city != correct_answer], 2
## )
## options = wrong_options + [correct_answer]
## random.shuffle(options)
##
## while True:
##     guess = input("\nWhich capital are we looking for? ")
##     more_random_sentences = random.choice(list_of_sentences)
##     more_redacted_sentences = redact_city(more_random_sentences, correct_answer)

## def play_game():
##     wiki = create_wikipedia_client()
##     correct_answer = random.choice(CAPITALS)
##     clues = get_clues(correct_answer, wiki)

    wiki = create_wikipedia_client("en")

    capital_en = random.choice(list(CAPITALS))
    correct_answer = CAPITALS[capital_en] if language == "de" else capital_en

    clues = get_clues(capital_en, wiki, texts)

    print(f"\n{texts['welcome']}\n")
    print(texts["first_clue"])

    first_clue = redact_city(random.choice(clues), capital_en)
    print(f'"{first_clue}"')

    wrong_attempts = 0

    while wrong_attempts < 5:
        guess = input(texts["question"]).strip()

        if check_answer(guess, correct_answer):
            print(texts["correct"])
            show_attempts(wrong_attempts + 1)
            break

        print(f"\n{texts['wrong']}")
##         print("\nWrong! Here comes another clue:")
##         print(f'"{more_redacted_sentences}"')

        wrong_attempts += 1

        if wrong_attempts == 3:
            wrong_options = random.sample(
                [city for city in CAPITALS.values() if city != correct_answer],
                2,
            )
            options = wrong_options + [correct_answer]
            random.shuffle(options)
            print(f"\nChoose one of these options: {options}")

        if wrong_attempts < 5:
            next_clue = redact_city(random.choice(clues), capital_en)
            print(f'"{next_clue}"')
    else:
        print(f"The correct answer was: {correct_answer}")


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
