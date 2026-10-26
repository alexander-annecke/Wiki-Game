import wikipediaapi
import random

capitals = [
    "Berlin",
    "Paris",
    "Rome",
    "Madrid",
    "Lisbon",
    "Vienna",
    "Brussels",
    "Prague",
    "Copenhagen",
    "Stockholm"
]

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="CapitalQuiz/1.0 (annecke@gmail.com)",
    language="en"
)
correct_answer = random.choice(capitals)

page_py = wiki_wiki.page(correct_answer)


complete_content = page_py.text
list_of_sentences = complete_content.split(".")
first_random_sentence = random.choice(list_of_sentences)

print("Here comes the first clue:")
print(first_random_sentence)

while True:
    guess = input("Which capital are we looking for? ")
    more_random_sentences = random.choice(list_of_sentences)

    if guess.strip().lower() == correct_answer.lower():
        print("Correct!")
        break
    else:
        print("Wrong! Here comes another clue:")
        print(more_random_sentences)