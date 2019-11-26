# trashy_scripts

Welcome to the rice fields, lol

## papa.py

Downloads all Papa John's promo codes in format  
*[id] -  [code] - [description] - [condition] - [available cities]*,

prints into terminal and saves them in file *codes.txt*.

Dependencies
------------
* Python 3
* Urllib module
* Json module

Usage:
------------
    python3 papa.py [-h] [-c CITY]

See help (python3 papa.py -h) for detailed information.

## pingparser.py

That script displays ping information in a graph. It parses input file and builds a graph, where green-to-yellow lines are good->acceptable ping, yellow - acceptable ping (100 ms by default, but you can define it), yellow-to-red lines are acceptable->bad ping.

Dependencies
------------
* Python 3
* Pingparsing module
* Json module
* Argparse module
* Matplotlib module

Usage:
-----------
    python3 pingparser.py [-h] [-i INPUT] [-p PING]

See help (python3 pingparser.py -h) for detailed information.