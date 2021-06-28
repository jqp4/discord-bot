
import json
import requests

print('\n'*10)

#url0 = 'https://vk.com/z3rtt'
#response = requests.get(url0) # Get-запрос
#json_data = json.loads(response.text) # Извлекаем JSON
#print(f'\n{json_data}\n')


d = {'a':1, 'b':2, 'n':5}
print(d)

for key in ['a', 'c']:
    d.pop(key, None)

if 'b' in d:
    print(d)
