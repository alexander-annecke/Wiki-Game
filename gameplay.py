import random
import re

import wikipediaapi
import re

from storage.game_logic import check_answer


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
