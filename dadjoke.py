import json
import random

class DadJoke:
    def __init__(self):
        f = open("jokes.json")
        self.jokes = json.load(f)["list"]
        f.close()

    def print_joke(self):
        print(random.choice(self.jokes))
    
    def print_list(self):
        print(self.jokes)

if __name__ == "__main__":
    jokes = DadJoke()
    jokes.print_joke()