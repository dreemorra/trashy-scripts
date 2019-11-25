import json
import pingparsing
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="input file with ping stat")
parser.add_argument("-p", "--ping", type=float, help="acceptable ping, 100 by default",
                    default=100)
args = parser.parse_args()

with open(args.input) as file:
    file_contents = file.read()

parser = pingparsing.PingParsing()
stats = parser.parse(file_contents)

print("[extract ping statistics]")
stats_dict = stats.as_dict()
print(json.dumps(stats_dict, indent=4))
print("\n[extract icmp replies]")

for i, icmp_reply in zip(range(0, len(stats.icmp_replies)), stats.icmp_replies):
    time = icmp_reply['time']
    g_rate = round(args.ping/time, 2)
    r_rate = round(time/args.ping, 2)
    if (r_rate <= 1):
        plt.bar(i, time, width=1, align='edge', color=(r_rate, 1, 0))
    else: plt.bar(i, time, width=1, align='edge', color=(1, g_rate, 0))
    print(icmp_reply)
plt.show()