import random

tebakbahasa = {'mother':'ibu', 'father':'ayah', 'book':'buku'}

def language_guessing_game():
    words = list(tebakbahasa.keys())
    random.shuffle(words)

    score = 0

    for word in words:
        answer = input(f"What is the Indonesian word for '{word}'? ")
        if answer.lower() == tebakbahasa[word]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is '{tebakbahasa[word]}'.")

    print(f"Game over! Your final score is {score}/{len(tebakbahasa)}.")

if __name__ == "__main__":
    language_guessing_game()
