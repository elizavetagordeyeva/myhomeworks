import re

forms = []
sitwords = []

with open ('carriedaway.txt', 'r', encoding = 'UTF-8') as f:
    text = f.read().replace('\n', ' ')
    words = text.split()
    
    testword = '((с|C)и(жу|д(и(шь|т|м|те)?|е(ть|л(а|о|и)?|вш.+)|я.+)(ся)?))'
    for word in words:
        word = word.strip('.,!:')
        m = re.match(testword, word)
        if m!= None:    
            forms.append(word)
    for word in forms:
        if word not in sitwords:
            sitwords.append(word )
    print(sitwords)
            
            
