Enygmas = {}
keys = []

with open ('wordcomb.txt', 'r', encoding = 'UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        elem = line.split(',')
        keys.append(elem[0])
        Enygmas[elem[0]] = elem[1]
        elem[1] = elem[1].strip('\n')
    
    import random
    
    for i in range(10):
        word = random.choice(keys)
        print('Отгадайте слово! Вот подсказка: ', Enygmas[word])
        guess = input('Ваш ответ? ')
        if guess == word:
            with open ('congrats.txt', 'r', encoding = 'UTF-8') as congratulations:
                congrats = congratulations.readlines()
                print(random.choice(congrats))
        else:
            with open ('hatred.txt', 'r', encoding = 'UTF-8') as hate:
                hatred = hate.readlines()
                print(random.choice(hatred))
