import random

def resposta(answerNumber):
    if answerNumber > 7:
        return "correto"
    elif answerNumber <= 7:
        return "errado"

r = random.randint(1, 15)
answer = resposta(r)
print(answer)

# abobora = random.randint(1, 100)
# print(abobora)