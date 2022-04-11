class Attempt:
    def __init__(self, correct: str):
        self.correct = correct

    def attempt(self, attempt: str):
        assert(len(attempt) == len(self.correct))

        list = []

        for i in range(len(attempt)):
            charAtt = attempt[i]
            charCorrect = self.correct[i]

            if (charAtt == charCorrect):
                list.append('^')
            elif (charAtt in self.correct):
                list.append('+')
            else:
                list.append('x')

        print(*list)

        return list.count('^') == len(self.correct)