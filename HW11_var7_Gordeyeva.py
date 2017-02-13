import re

def f1():
    with open ('birds.txt', 'r', encoding = 'utf-8') as article:
        lines = article.read()
    return lines

def f2(lines):
    lines = re.sub(r'\bптиц', r'\bрыб', lines)
    lines = re.sub(r'\bПтиц', r'\bРыб', lines)
    lines = re.sub(r'\bптице.', r'\bрыбо.', lines)
    lines = re.sub(r'\bПтице.', r'\bРыбо.', lines)
    return lines

def f3(lines):
    with open ('fishbirds.txt', 'w', encoding = 'utf-8') as blank:
        blank.write(lines)

a = f1()
b = f2(a)
f3(b)

        
        
        
