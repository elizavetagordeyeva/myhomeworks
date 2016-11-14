words=[]
i=0
print('Введите 8 слов: ')
while i!=8:
    word=input()
    words.append(word)
    i+=1

pairs=[]
i=0
while i<=6:
    pair =(words[i]+words[i+1])
    i+=2
    pairs.append(pair)
for p in pairs:
    print(p)
