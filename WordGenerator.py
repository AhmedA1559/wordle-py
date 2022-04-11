import random


class WordGenerator:
    def __init__(self):
        with open("wordlist.txt", 'r') as file:
            self.words = file.readlines()

    def generate(self) -> str:
        return random.choice(self.words).strip()