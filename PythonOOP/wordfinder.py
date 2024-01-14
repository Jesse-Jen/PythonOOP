import random


class WordFinder:

    def __init__(self, file):
        with open(file) as word_dict:
            self.words = self.parse(word_dict)
        print(f'There are {len(self.words)} words')
        
    def parse(self, word_dict):
        return [words.strip() for words in word_dict]
    
    def randomWord(self):
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    def parse(self, word_dict):
        return [words.strip() for words in word_dict
                if words.strip() and not words.startswith('#')]