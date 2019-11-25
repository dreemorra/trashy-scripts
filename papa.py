import urllib.request
import json
with urllib.request.urlopen("https://www.papajohns.by/api/stock/codes") as url:
    data = json.loads(url.read().decode())

codes = data['codes']
with open('codes.txt', 'w') as output:
    for code in codes:
        if 'Минск' in code['name']:
            print(code['name'])
            output.write(f"{code['name']}\n")
output.close()
