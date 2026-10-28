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

complete_content = page_py.text
list_of_sentences = complete_content.split(". ")
list_of_sentences = [s.strip() for s in list_of_sentences if len(s.strip()) > 40 and len(s.strip()) < 200]
first_random_sentence = random.choice(list_of_sentences)
first_redacted_sentence = redact_city(first_random_sentence, correct_answer)
    if not sentences:
        raise ValueError(f"No usable clues found for {city}.")

    return sentences


wrong_attempts = 0

wrong_options = random.sample(
    [city for city in capitals if city != correct_answer], 2
)
options = wrong_options + [correct_answer]
random.shuffle(options)

while True:
    guess = input("\nWhich capital are we looking for? ")
    more_random_sentences = random.choice(list_of_sentences)
    more_redacted_sentences = redact_city(more_random_sentences, correct_answer)
def play_game():
    wiki = create_wikipedia_client()
    correct_answer = random.choice(CAPITALS)
    clues = get_clues(correct_answer, wiki)

    print("Here comes the first clue:")

    first_clue = redact_city(random.choice(clues), correct_answer)
    print(f'"{first_clue}"')

    while True:
        guess = input("\nWhich capital are we looking for? ").strip()

        if guess.casefold() == correct_answer.casefold():
            print("Correct!")
            break

        print("\nWrong! Here comes another clue:")
        print(f'"{more_redacted_sentences}"')
        wrong_attempts += 1
        if wrong_attempts == 3:
            print(f"\nChoose one of these options: {options}")
        next_clue = redact_city(random.choice(clues), correct_answer)
        print(f'"{next_clue}"')

# def menu():
#     print("\nWelcome to CAPITAL CLUES!\n")
#     print("1. English\n2. Deutsch")
#     language_selected = input("Please select a language: ")

    play_game()

def main():
    play_game()


if __name__ == "__main__":
    main()