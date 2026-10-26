import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="CapitalQuiz/1.0 (annecke@gmail.com)",
    language="de"
)

page_py = wiki_wiki.page("Berlin")

print("Titel:", page_py.title)

correct_answer = "Berlin"

guess = input("Welche Hauptstadt ist gesucht? ")

if guess.strip().lower() == correct_answer.lower():
    print("Richtig!")
else:
    print("Leider falsch. Hier kommt ein neuer Hinweis.")
    print(page_py.summary)