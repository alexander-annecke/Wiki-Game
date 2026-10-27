
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
