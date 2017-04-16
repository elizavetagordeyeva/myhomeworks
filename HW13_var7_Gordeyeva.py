import os
import re

n = 0
am = 0
cyr = ['йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ']
lat = ['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
for f in os.listdir('.'):
    if os.path.isdir(f) == 'True':
        m = re.match(cyr, f)
        if m != None:
            k = re.match(lat, f[i])
            if k != None:
                am += 1
print(am, 'folders containing both cyrillics and latinics')
