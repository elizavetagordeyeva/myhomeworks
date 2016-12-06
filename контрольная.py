spaces = 0

with open ('quotes.txt', 'r', encoding = 'UTF-8') as text:
    
    for line in text.readlines():
        
        dash = line.rfind('-')
        
        spaces = line[:dash].count(' ')
        
        if spaces < 9:
            print(line[:dash])
            
        
