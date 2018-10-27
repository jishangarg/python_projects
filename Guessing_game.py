import random
def my_guess():
    return list(input("-Guess a 3 digit no. with non-repeating digits "))

def generate_code():
    digit=[]
    for num in range(10):
        digit.append(str(num))
    random.shuffle(digit)
    if digit[0]=='0':
        digit[0]=digit[9]
    return digit[:3]

def comparision(secret_code,guess):
    if len(guess)!=len(secret_code):
        return '**Invalid guess ! Dont\'t u know d meaning of 3 digit no. !'
    if secret_code==guess:
        return 'H U R R A Y ! CODE CRACkED !'
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
count=0
while guess!=secret_code:
    guess=my_guess()
    count+=1
    print('Status of ur guess: ')
    clue_arr=comparision(secret_code,guess)
    if(type('rr')==type(clue_arr)):
        print(clue_arr)
    else:
        for clue in clue_arr:
            print(clue)

print('u took {x} turns to guess correctly'.format(x=count))

