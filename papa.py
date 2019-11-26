import urllib.request
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--city", type=str, help="filter city (in russian!!!)", default="")
parser.add_argument("-o", "--output", type=str, help="output file", default="codes.txt")
args = parser.parse_args()

with urllib.request.urlopen("https://www.papajohns.by/api/stock/codes") as url:
    data = json.loads(url.read().decode())

codes = data['codes']
with open(args.output, 'w') as output:
    for code in codes:
        if args.city in code['name']:
            print(code['name'])
            output.write(f"{code['name']}\n")
output.close()
