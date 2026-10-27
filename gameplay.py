import wikipediaapi
import random
import re

capitals = [
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
    "Nikosia",
    "Paris",
    "Prague",
    "Riga",
    "Rome",
    "Sofia",
    "Stockholm",
    "Tallinn",
    "Valetta",
    "Vienna",
    "Vilnius",
    "Warsaw",
    "Zagreb"
]

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="CapitalQuiz/1.0 (annecke@gmail.com)",
    language="en"
)

def categories():
    pass

def redact_city(sentence, city):
    pattern = r"\b" + re.escape(city) + r"\b"
    return re.sub(pattern, "██████", sentence, flags=re.IGNORECASE)

correct_answer = random.choice(capitals)

page_py = wiki_wiki.page(correct_answer)


complete_content = page_py.text
list_of_sentences = complete_content.split(".")
first_random_sentence = random.choice(list_of_sentences)
first_redacted_sentence = redact_city(first_random_sentence, correct_answer)

print("Here comes the first clue:")
print(first_redacted_sentence)

while True:
    guess = input("Which capital are we looking for? ")
    more_random_sentences = random.choice(list_of_sentences)
    more_redacted_sentences = redact_city(more_random_sentences, correct_answer)

    if guess.strip().lower() == correct_answer.lower():
        print("Correct!")
        break
    else:
        print("Wrong! Here comes another clue:")
        print(more_redacted_sentences)