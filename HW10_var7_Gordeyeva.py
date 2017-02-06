import re

def f1():
    with open ('language.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
        text1 = text.split('</a>')
        code = 'href="http:\/\/www-01\.sil\.org\/iso639-3\/documentation\.asp\?id=...">...'
        for i in text1:
            m = re.search(code, i)
            if m != None:
                result = i[len(i)-3:len(i)]
                break
    return result

def f2(result):
    with open ('musor.txt', 'w', encoding = 'utf-8') as blank:
        blank.write(result)
        
a = f1()
f2(a)
