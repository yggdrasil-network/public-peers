#!/usr/bin/env python3
import re
import os
import sys
import logging
import asyncio
from datetime import datetime

get_loop = asyncio.get_running_loop if hasattr(asyncio, "get_running_loop") else \
    asyncio.get_event_loop
PEER_REGEX = re.compile(r"`(tcp|tls)://([a-z0-9\.\-\:\[\]]+):([0-9]+)`")

def get_peers(data_dir, regions=None, countries=None):
    """Scan repository directory for peers"""
    assert os.path.exists(os.path.join(data_dir, "README.md")), "Invalid path"
    peers = []
    ALL_REGIONS = [d for d in os.listdir(data_dir) if \
            os.path.isdir(os.path.join(data_dir, d)) and \
            not d in [".git", "other"]]

    ALL_COUNTRIES = []
    for region in ALL_REGIONS:
        ALL_COUNTRIES += [f for f in os.listdir(os.path.join(data_dir, region)) if \
            f.endswith(".md")]

    if not regions: regions = ALL_REGIONS
    if not countries: countries = ALL_COUNTRIES

    for region in regions: 
        for country in countries:
            cfile = os.path.join(data_dir, region, country)
            if os.path.exists(cfile):
                with open(cfile) as f:
                    for p in PEER_REGEX.findall(f.read()):
                        peers.append(
                            {"uri": p, "region": region, "country": country})

    return peers

async def resolve(name):
    """Get IP address or none to skip scan"""
    if name.startswith("["): return name[1:-1] # clear ipv6 address
    addr = name

    try:
        info = await get_loop().getaddrinfo(name, None)
        addr = info[0][4][0]
    except Exception as e:
        logging.debug("Resolve error %s: %s", type(e), e)
        addr = None

    return addr

async def isup(peer):
    """Check if peer is up and measure latency"""
    peer["up"] = False
    peer["latency"] = None
    addr = await resolve(peer["uri"][1])
    if addr:
        start_time = datetime.now()

        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(
                    addr, peer["uri"][2]), 5)
            peer["latency"] = datetime.now() - start_time
            writer.close()
            await writer.wait_closed()
            peer["up"] = True
        except Exception as e:
            logging.debug("Connection error %s: %s", type(e), e)

    return peer

def print_results(results):
    print("Dead peers:\n")
    for p in filter(lambda p: not p["up"], results):
        print("{}://{}:{}".format(*p["uri"]), "\t",
              "{}/{}".format(p["region"], p["country"]))

    
    print("\n\nAlive peers (sorted by latency):\n")
    print("URI", "\t", "Latency (ms)", "\t", "Location")
    alive_peers = filter(lambda p: p["up"], results)
    for p in sorted(alive_peers, key=lambda x: x["latency"]):
        latency = round(p["latency"].total_seconds() * 1000, 3)
        print("{}://{}:{}".format(*p["uri"]), "\t", 
              latency, "\t", 
              "{}/{}".format(p["region"], p["country"]))

async def main(peers):
    results = await asyncio.gather(*[isup(p) for p in peers])
    print_results(results)

if __name__ == "__main__":
    data_dir = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()

    print("Report date:", datetime.utcnow().strftime("%c"))
    peers = get_peers(data_dir)
    asyncio.run(main(peers))
