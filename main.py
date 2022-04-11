from Attempt import Attempt
from WordGenerator import WordGenerator

correct_word = WordGenerator().generate()
print(correct_word)
for i in range(5):
    if Attempt(correct_word).attempt(input()):
        print("You won with %d attempts!" % (i+1))
        break
