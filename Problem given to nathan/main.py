# Problem

'''
Twenty random card are placed in a row all face down. A tuen consists of taking two adjacent cards where the left one is face up and the right one is flipped ie (if face down then face up and vice versa). Show that this process must terminate. (All cards are face up.)
'''

def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
    return b

if __name__ == "__main__":
    cardsList = list('11111111111111111111') # --> Down state in represented by 1 and up state by 0.
    print(cardsList)

    while cardsList != transform(cardsList.copy()):
        cardsList  = transform(cardsList.copy())
    
    print(cardsList)
    print("The process has been terminated.")