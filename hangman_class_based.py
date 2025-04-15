import random
import requests


class Hangman:
    def __init__(self):
        self.word = self.choose_word()
        self.guessed_letters = set()
        self.attempts = 6

    def choose_word(self):
        try:
            response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            if response.status_code == 200:
                return response.json()[0]
        except Exception:
            print("Error fetching word, using default list.")
        return random.choice(['python', 'hangman', 'developer', 'challenge', 'programming'])

    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def guess_letter(self, letter):
        letter = letter.lower()

        if not letter.isalpha() or len(letter) != 1:
            return "Please enter a single valid letter."

        if letter in self.guessed_letters:
            return "You already guessed that letter."

        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.attempts -= 1
            return f"Incorrect! {self.attempts} attempts left."

        return "Correct!"

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def play(self):
        print("Welcome to Hangman!")

        while self.attempts > 0:
            print("\n" + self.display_word())
            print("Guessed letters:", ' '.join(sorted(self.guessed_letters)))
            guess = input("Guess a letter: ")

            message = self.guess_letter(guess)
            print(message)

            if self.is_word_guessed():
                print(f"\n{self.display_word()}")
                print(f"Congratulations! You guessed the word: {self.word}")
                return

        print(f"Game over! The word was: {self.word}")


if __name__ == "__main__":
    game = Hangman()
    game.play()
