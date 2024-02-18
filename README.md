# Public Peers

This repository contains peering information for publicly accessible nodes on
the Yggdrasil network. 

Note that not all peers in this repository are guaranteed to be online - check
the [Public Peers](https://publicpeers.neilalexander.dev/) page instead to find
peers that are online now.

In most cases, public peers should be accessible by adding the string provided
for each peer to the `Peers: []` section of your `yggdrasil.conf` configuration
file.

Example in `yggdrasil.conf`:
```
Peers: [
  tcp://a.b.c.d:e
  tls://d.c.b.a:e
  tcp://[a:b:c::d]:e
  tls://[d:c:b::a]:e
]
```

### How do I pick peers?

If you are new to the network then take a look at the [Public Peers](https://publicpeers.neilalexander.dev/)
page to find public peers that are online.

Always try to pick peers that are as close to you geographically as possible, as
this will keep the latency of the network down.

If you are using a home connection, then you should avoid peering with any nodes
that are far away, as you may end up carrying traffic for the rest of the
network.

For normal usage, you probably only need 2 or 3 peers.

### Peering reference
URI format: `[protocol]://[host]:[port]?[options]`

**Available protocols:**
- Cleartext TCP: `tcp://`
- TLS: `tls://`
- TCP over SOCKS5: `socks://`
- UNIX sockets: `unix://`
- QUIC (v0.5.0+): `quic://`
- TLS over SOCKS5 (v0.5.2+): `sockstls://`

Yggdrasil supports basic authentication for SOCKS5 using credentials in the URI like this: `socks://user:password@host`

**Query options:**
- Public-key authentication: `?key=[publickey]` (can have multiple values)
- Custom SNI (for TLS/QUIC): `?sni=[domain]` (default is host if it's domain)
- Same-peer link priority: `?priority=[integer]` (default is 0, maximum 254 for lowest priority)
- Password authentication (v0.5.0+): `?password=[string]` (length up to 64 characters)
- Maximum back-off time (v0.5.5+): `?maxbackoff=[seconds]` (supports duration values like 5m, 1h etc)
