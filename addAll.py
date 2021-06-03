#!/usr/bin/env python3

import os
import re
import socket
import argparse

def is_ipv4(value):
    try:
        socket.inet_aton(value)
        return True
    except:
        return False

def is_ipv6(value):
    try:
        socket.inet_pton(socket.AF_INET6, value)
        return True
    except:
        return False

def check_if_domain(value):
    # Regex from https://github.com/kvesteri/validators/blob/master/validators/domain.py#L5-L10
    return re.match(
        r'^(?:[a-zA-Z0-9]'  # First character of the domain
        r'(?:[a-zA-Z0-9-_]{0,61}[A-Za-z0-9])?\.)'  # Sub domain + hostname
        r'+[A-Za-z0-9][A-Za-z0-9-_]{0,61}'  # First 61 characters of the gTLD
        r'[A-Za-z]$'  # Last character of the gTLD
        , value.split(':')[0]
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Yggdrasil Public Peer Compiler")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--blacklist', help='blacklists peer file (delimited by space)')
    group.add_argument('-w', '--whitelist', help='whitelists peer file (delimited by space)')
    parser.add_argument('-d', '--peer-directory', default='.', help='peer directory (default pwd)')
    parser.add_argument('-4', '--ipv4', help='only show ipv4 peers', action='store_true')
    parser.add_argument('-6', '--ipv6', help='only show ipv6 peers', action='store_true')
    parser.add_argument('-a', '--dns', help='only show dns peers', action='store_true')
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
                            for match in re.findall(r'\*\s*`(.*?)`', line):
                                if args.ipv4 or args.ipv6 or args.dns:
                                    proto = match.split(':')[0]
                                    host = match.split('/')[2]
                                    if proto not in ['tcp','tls']: continue

                                    try:
                                        if args.ipv4 and is_ipv4(host.split(':')[0]):
                                                print(match)
                                                continue
                                    except:
                                        pass

                                    try:
                                        if args.ipv6 and is_ipv6(host.split('[')[1].split(']')[0]):
                                                print(match)
                                                continue
                                    except:
                                        pass

                                    try:
                                        if args.dns and check_if_domain(host):
                                                print(match)
                                                continue
                                    except:
                                        pass
                                else:
                                    print(match)
            except:
                pass
