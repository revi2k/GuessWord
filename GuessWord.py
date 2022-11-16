import numpy as np
import random
import string

class RandomArray():
    def __init__(self, word):
        self.word = word
    def size(self):
        return self.sizeArray
    def create(self):
        self.array = np.array(())
        alphabet = list(string.ascii_lowercase)
        for element in range (0,len(self.word)):
            self.array = np.append(self.array, random.choice(alphabet))
    def return_word(self):
        return ''.join(self.array)
    def guess(self):
        count = 0
        while self.word != self.return_word():
            count += 1
            self.create()
            self.return_word()
        return "It taked "+str(count)+" tries"


table = RandomArray('gue')



table.create()
print(table.guess())