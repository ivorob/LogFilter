#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('search')
parser.add_argument('regex')
args = parser.parse_args()

combine = {}
with open(args.filename, 'r') as logfile:
    for line in logfile:
        if args.search in line:
            match = re.search(args.search + args.regex, line);
            if match:
                key = match.group(match.lastindex)
                combine[key] = combine.get(key, 0) + 1

sortedKeys = sorted(combine, key=lambda key: -1 * combine[key])
for key in sortedKeys:
    print('Search: ', key, ', Count: ', combine[key])

