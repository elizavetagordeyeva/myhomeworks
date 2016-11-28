print('Введите слово')
word = input()
i = 0
j = 0
length = int(len(word))
while length>=1 :
    i+=1
    j-=1
    print (word[i:j])
    length-=2
    
