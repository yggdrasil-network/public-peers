# Public Peers

This repository contains peering information for publicly accessible nodes on
the Yggdrasil network. If you are new to the network then this is a good place
to start in order to get connected.

In most cases, public peers should be accessible by adding the string provided
for each peer to the `Peers: []` section of your `yggdrasil.conf` configuration
file.

Example in `yggdrasil.conf`:
```
Peers:
[
  tcp://a.b.c.d:e
  tcp://d.c.b.a:e
  tcp://[a:b:c::d]:e
  tcp://[d:c:b::a]:e
]
```

### How do I pick peers?

Always try to pick peers that are as close to you geographically as possible, as
this will keep the latency of the network down.

If you are using a home connection then you should avoid peering with any nodes
that are far away, as you may end up carrying traffic for the rest of the
network.

For normal usage, you probably only need 2 or 3 peers.
