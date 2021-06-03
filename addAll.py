#!/usr/bin/env python3

import os
import re
import argparse

if __name__ == "__main__":
    peer_regex = re.compile(r'\*\s*`(.*?)`')
    parser = argparse.ArgumentParser(description="Yggdrasil Public Peer Compiler")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--blacklist', help='blacklists peer file (delimited by space)')
    group.add_argument('-w', '--whitelist', help='whitelists peer file (delimited by space)')
    parser.add_argument('-d', '--peer-directory', default='.', help='peer directory (default pwd)')
    args = parser.parse_args()
    if args.blacklist is not None:
        args.blacklist.split(' ')
    if args.whitelist is not None:
        args.whitelist.split(' ')

    for root, dirs, files in os.walk(args.peer_directory):
        if os.path.relpath(root, args.peer_directory) not in ['asia', 'europe', 'north-america', 'other', 'south-america']:
            continue

        for file in files:
            if args.blacklist is not None and file.split('.')[0].lower() in args.blacklist.split('.')[0].lower():
                continue
            if args.whitelist is not None and file.split('.')[0].lower() not in args.whitelist.split('.')[0].lower():
                continue

            try:
                if file.split('.')[-1] == 'md':
                    with open(os.path.join(root, file), 'r') as f:
                        for line in f:
                            for match in peer_regex.findall(line):
                                print(match)
            except:
                pass
