# Tor hidden service peers

*It's recommended that peers use Tor's [LongLivedPorts] (21, 22, 706,
1863, 5050, 5190, 5222, 5223, 6523, 6667, 6697 and 8300 at the time of
writing) to increase node's availability.*

[LongLivedPorts]:https://2019.www.torproject.org/docs/tor-manual.html.en#LongLivedPorts

Add connection strings from the below list to the `Peers: []` section of your
Yggdrasil configuration file to peer with these nodes.

Note that the following assumes Tor is running locally and listening on the default `localhost:9050`.

* HS3 (TCP-only, Hidden Service, v3), operated by [Jeff](https://i2p.rocks/contact.txt)
  * `socks://localhost:9050/ruoqfb5l2n55x62gu4qsooqm6yamnkjnbqmr6xbxppkxbccgyvioc3ad.onion:5050`

* HS3 (TCP-only, Hidden Service, v3), operated by [cathugger](http://cathug2kyi4ilneggumrenayhuhsvrgn6qv2y47bgeet42iivkpynqad.onion/contact.html)
  * `socks://localhost:9050/yggnekkmyitzepgl5ltdl277y5wdg36n4pc45sualo3yesm3usnuwyad.onion:1863`

* HS3 (TCP-only, Hidden Service, v3), operated by [Mikaela](https://mikaela.info/) on behalf of [Pirate Party Finland](https://piraattipuolue.fi/en) ([Tor Metrics](https://metrics.torproject.org/rs.html#details/796338999A7E34CA4C0F2C6092618C82C0D335D9))
  * `socks://localhost:9050/x7dqdmjb7y5ykj4kgirwzj62wrrd3t5dv57oy7oyidnf7cpthd4k7ryd.onion:5222`

* HS3 (TCP-only, Hidden Service, v3), operated by [opal hart](http://opalwxdqzyuwo2vbipp3facjuuztfjwauai7fghh2ggbcl7enuvfg6yd.onion/contact.xht)
  * `socks://localhost:9050/nxuwjikhsirri2rbrdlphstsn3jr2qzjrsylwkt65rh2miycr5n24tid.onion:706`
  * `socks://localhost:9050/fllrj72kxnenalmmi3uz22ljqnmuex4h2jlhwnapxlzrnn7lknadxuqd.onion:706`

* HS3 (TCP-only, Hidden Service, v3)
  * `socks://localhost:9050/k47rozbvcwzou5rk4t2b6nqiyuzcoxxhk4kaewgbx4ngthnxmaukpqqd.onion:6667`
