import re


with open ('isll.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    tag = '</teiHeader>'
    amount = 0
    for line in lines:
        amount += 1
        m = re.search(tag, line)
        if m != None:
            with open ('res.txt', 'w', encoding = 'utf-8') as result:
                result.write(str(amount))
        
            
   
