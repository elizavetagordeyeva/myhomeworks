unwords = []

def f():
    words = []
    with open('test.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
        words = text.split()
    return words
        
def words():
    amount = 0
    words = f()
    for i in range(len(words)): 
        if words[i].startswith('un') : 
            unwords.append(words[i])
            amount += 1 
    return amount
print('There are', words(), 'words beginning with UN. ')

def percentage():
    quantity = 0
    percentage = 0
    check = input('Input you word: ')
    for n in range(len(unwords)):
        if len(unwords[n]) > len(check):
            quantity += 1
    percentage = (quantity/len(unwords))*100
    return percentage
print(percentage(), '% of words is longer than the input word. ')






