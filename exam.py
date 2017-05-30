import re

with open ('mz.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    words = text.split()
    i = 0
    phrases = []
    names = []
    for word in words:
        phrase = (word[i] + ' ' + word[i+1])
        phrases.append(phrase)
        i += 1
        name = '(ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ)/\s/(ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ).+)'
        m = re.search(name, phrase)
        if m != None:
             names.append(phrase)
print(names)
        
        
        
            
