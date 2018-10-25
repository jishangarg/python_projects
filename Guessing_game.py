import random
def my_guess():
    return list(input("What is your guess ?"))

def generate_code():
    digit=[]
    for num in range(10):
        digit.append(str(num))
    random.shuffle(digit)
    return digit[:3]

def comparision(secret_code,guess):
    if secret_code==guess:
        return 'CODE CRACKED !'
    clue=[]

    for ind,num in enumerate(guess):
        if secret_code[ind]==num:
            clue.append('match')
        elif num in secret_code:
            clue.append('close')

    if clue==[]:
        return ['Nope']
    else:
        return clue

print("Hare Krishna everyone and Welcome to code Breaker !")
secret_code=generate_code()
guess='1'
while guess!=secret_code:
    guess=my_guess()
    print('Status of ur guess: ')
    clue_arr=comparision(secret_code,guess)
    for clue in clue_arr:
        print(clue)



