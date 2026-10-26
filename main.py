
from gameplay import play_round
from storage.game_logic import check_answer

def show_instructions():
    """Displays the game instructions."""
    pass


def show_categories():
    """Displays the available game categories."""
    categories = [
        "European capitals",
    ]

    print("\nAvailable game categories:")

    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")


def select_category():
    """Allows the player to select a game category."""
    categories = ["European capitals"]

    while True:
        show_categories()
        choice = input("Please select a category (enter 1): ")

        if choice == "1":
            return categories[0]

        print("Invalid selection. Please try again.")


def start_game():
    """Starts a round of the game."""
    category = select_category()

    if category is None:
        return

    print(f"\nStarting a new game in the category: {category}")
    print("Try to guess the correct answer.")

    play_round()


def get_random_sentence(category):
    """Returns a random sentence from an article."""
    pass


def hide_hints(sentence):
    """Masks identifying clues in the sentence."""
    pass


def get_user_input():
    """Asks the player to enter an answer."""
    pass


def evaluate_game():
    """Evaluates the game result."""
    pass


def ask_to_continue():
    """Asks whether the player wants to continue playing."""
    while True:
        choice = input("Would you like to play again? (y/n): ")
        choice = choice.strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False

        print("Invalid input. Please enter 'y' or 'n'.")


def main():
    """Controls the main game flow."""
    print("Welcome to Wiki-Game!")

    while True:
        start_game()

        if not ask_to_continue():
            print("Thanks for playing Wiki-Game!")
            break


if __name__ == "__main__":
    main()