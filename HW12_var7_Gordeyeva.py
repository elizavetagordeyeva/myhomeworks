import re

def f1():
    with open ('ann.txt', 'r', encoding = 'utf-8') as file:
        text = file.read()
        sentences = text.split('.')
        sentences = [sentence.lower() for sentence in sentences]
        sentences = [re.sub(r'[\,—:;"\()]', '', sentence) for sentence in sentences]
    return sentences

def f2(sentences):
    words = [sentence.split() for sentence in sentences]
    Dick = {word : sentence.count(word) for sentence in words for word in sentence if sentence.count(word) > 1 }
    return Dick

def f3(Dick):
    shablon = '{:^10} {:^10}'
    for ball in Dick:
        print(shablon.format(ball, Dick[ball]))
    
sentences = f1()
Dick = f2(sentences)
f3(Dick)
