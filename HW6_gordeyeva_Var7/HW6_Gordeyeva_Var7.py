import random

def f1():
    with open ('first_line.txt', 'r', encoding = 'UTF-8') as f1:
        for line in f1:
            long_nouns = line.split()
            return random.choice(long_nouns)

def punctuation():
    marks = [".", ",", "?", "!", "...", "!!!"]
    return random.choice(marks)

def f2():
    with open ('sec_line_verb.txt', 'r', encoding = 'UTF-8') as f2:
        for line in f2:
            verbs = line.split()
            return random.choice(verbs)

def f3():
    with open ('sec_line_pronoun.txt', 'r', encoding = 'UTF-8') as f3:
        for line in f3:
            pronouns = line.split()
            return random.choice(pronouns)

def f4():
    with open ('sec_line_adv.txt', 'r', encoding = 'UTF-8') as f4:
        for line in f4:
            adverbs = line.split()
            return random.choice(adverbs)

def line1():
    return f1() + punctuation() + '\n'

def line2():
    return f2() + ' ' + f3() + ' ' + f4() + punctuation() + '\n'

def weird_verse():
    return line1() + line2() + line1() + line2() + line2()
print(weird_verse())









    
