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
Peers:
[
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

If you are using a home connection then you should avoid peering with any nodes
that are far away, as you may end up carrying traffic for the rest of the
network.

For normal usage, you probably only need 2 or 3 peers.

### Protocols

Currently Yggdrasil only operates as overlay network, so it requires underlaying networking.
As for 0.4.5, following protocols supoorted for peering:

- Plain TCP (`tcp://host:port`)
- TLS (`tls://host:port`)
- TCP over SOCKS5 (`socks://user:pass@proxy/host:port`)
- UNIX sockets (`unix:///path/to/socket.sock`)

### URI options

Some peers may use additional options as query string.

All supported options from 0.4.7:

* `key=PUBLICKEY` for public key pinning, allowing peering only when peer provides specified public key, you can pass multiple keys with same option name.

* `priority=N` for prioritising multiple peerings to the same peer, priority must be integer between 0 and 254.

* *(TLS only)* `sni=DOMAIN` sets optional Server Name Indication (SNI) of session, you can use that to hide the peering inside a "regular" TLS session.
