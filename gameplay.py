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
    "Valletta",
    "Vienna",
    "Vilnius",
    "Warsaw",
    "Zagreb"
]



wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="CapitalQuiz/1.0 (annecke@gmail.com)",
    language="en"
)



def redact_city(sentence, city):
    pattern = r"\b" + re.escape(city) + r"\w*"
    return re.sub(pattern, "️XXX️", sentence, flags=re.IGNORECASE)

correct_answer = random.choice(capitals)

page_py = wiki_wiki.page(correct_answer)

complete_content = page_py.text
list_of_sentences = complete_content.split(". ")
list_of_sentences = [s.strip() for s in list_of_sentences if len(s.strip()) > 40 and len(s.strip()) < 200]
first_random_sentence = random.choice(list_of_sentences)
first_redacted_sentence = redact_city(first_random_sentence, correct_answer)

print("Welcome to CAPITAL CLUES!\n")

print("Here comes the first clue:")
print(f'"{first_redacted_sentence}"')

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

    if guess.strip().lower() == correct_answer.lower():
        print("Correct!")
        break
    else:
        print("\nWrong! Here comes another clue:")
        print(f'"{more_redacted_sentences}"')
        wrong_attempts += 1
        if wrong_attempts == 3:
            print(f"\nChoose one of these options: {options}")

# def main():
#    if __name__ == "__main__":
#     main()