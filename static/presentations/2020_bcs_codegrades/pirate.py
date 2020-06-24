import random

pirate_dictionary = {
    "hello": "ahoy",
    "you": "ye",
    "my": "me",
    "where": "whar",
    "is": "be",
}

pirate_phrases = ["thar she blows!", "arrr!", "avast ye!", ]

def translate(english):
    words = english.lower().split(" ")
    pirate = [pirate_dictionary.get(word, word) for word in words]
    if random.randint(0, 5) == 0:
        pirate.append(random.choice(pirate_phrases))
    return " ".join(pirate)
