sentences = 0
longsentences = 0

with open ('story.txt', 'r', encoding = 'UTF-8') as story:
    
    for line in story.readlines() :
        sentences+=1
        spaces = line.count(' ')
        if spaces > 4:
            longsentences+=1
            
percentage = (longsentences/sentences*100)
print('процент строк с колчиеством слов больше 5: ', percentage)
