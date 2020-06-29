import urllib.request
import json
import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--city", type=str, help="filter city (in russian!!!)", default="")
parser.add_argument("-t", "--type", type=str, help="filter code type (in russian). Types: Выбор, Скидка", default="")
parser.add_argument("-o", "--output", type=str, help="output file", default="codes.txt")
args = parser.parse_args()

with urllib.request.urlopen("https://www.papajohns.by/api/stock/codes") as url:
    data = json.loads(url.read().decode())

codes = [item.get('name').split(' - ') for item in data['codes']]
codes = sorted(codes, key=lambda k: k[3].split(' ')[-2])

table = PrettyTable(['id', 'codes', 'description', 'cost', 'cities'])
for code in codes:
    if (args.city.lower() or "Все города".lower() in code[4].lower() or args.city == "") and (args.type.lower() in code[2].lower() or args.type == ""):
        # print(code)
        table.add_row(code)
table.align["cities"] = "l"
table.align["codes"] = "l"
print(table)

with open(args.output, 'w') as output:
    output.write(f"{table}\n")
output.close()
