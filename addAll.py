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

def is_domain(value):
    # Regex from https://github.com/kvesteri/validators/blob/master/validators/domain.py#L5-L10
    return re.match(
        r'^(?:[a-zA-Z0-9]'  # First character of the domain
        r'(?:[a-zA-Z0-9-_]{0,61}[A-Za-z0-9])?\.)'  # Sub domain + hostname
        r'+[A-Za-z0-9][A-Za-z0-9-_]{0,61}'  # First 61 characters of the gTLD
        r'[A-Za-z]$'  # Last character of the gTLD
        , value.encode('idna').decode('ascii')
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Yggdrasil Public Peer Compiler")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--blacklist', help='blacklists peer file (delimited by space)')
    group.add_argument('-w', '--whitelist', help='whitelists peer file (delimited by space)')
    parser.add_argument('-d', '--peer-directory', default='.', help='peer directory (default pwd)')
    parser.add_argument('-p', '--protocol', help='only show specified protocol (delimited by space) (default tcp, tls for -46a and all for everything else)')
    parser.add_argument('-4', '--ipv4', help='only show ipv4 peers', action='store_true')
    parser.add_argument('-6', '--ipv6', help='only show ipv6 peers', action='store_true')
    parser.add_argument('-a', '--dns', help='only show dns peers', action='store_true')
    args = parser.parse_args()
    if args.blacklist is not None:
        args.blacklist = args.blacklist.split(' ')
    if args.whitelist is not None:
        args.whitelist = args.whitelist.split(' ')
    if args.protocol is not None:
        args.protocol = args.protocol.split(' ')
    else:
        if (args.ipv4 or args.ipv6 or args.dns):
            args.protocol = ['tcp','tls']
        else:
            args.protocol = ['tcp','tls','socks']

    for dir in ['asia', 'europe', 'north-america', 'other', 'south-america']:
        for file in os.listdir(os.path.join(args.peer_directory, dir)):
            if args.blacklist is not None and file.split('.')[0].lower() in [ x.split('.')[0].lower() for x in args.blacklist ]:
                continue
            if args.whitelist is not None and file.split('.')[0].lower() not in [ x.split('.')[0].lower() for x in args.whitelist ]:
                continue

            try:
                if file.split('.')[-1] == 'md' and os.path.isfile(os.path.join(args.peer_directory, dir, file)):
                    with open(os.path.join(args.peer_directory, dir, file), 'r') as f:
                        for line in f:
                            for match in re.findall(r'\*\s*`(.*?)`', line):
                                proto = match.split(':')[0]
                                if proto not in args.protocol: continue

                                if args.ipv4 or args.ipv6 or args.dns:
                                    host = match.split('/')[2]

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
                                        if args.dns and is_domain(host.split(':')[0]):
                                                print(match)
                                                continue
                                    except:
                                        pass
                                else:
                                    print(match)
            except:
                pass
