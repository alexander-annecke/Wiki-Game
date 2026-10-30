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
    sentences = re.split(r"(?<=[.!?])\s+", article_text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def play_round():
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="Wiki-Game/1.0 (noreply@whatiki.example)",
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

# Korrigierter Abschnitt: vorhandene Sätze weiterverwenden