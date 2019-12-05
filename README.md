# napalm-opengear

NAPALM driver for Opengear Linux

Your Jinja2 might look like:
```jinja2
config.system.name {{ inventory_hostname }}
```

This is turned into
```
sudo config -s config.system.name=...
```

Anything without a value (just a key like `config.delayed`) will be deleted via `config -d $key`.

We use `cp` to store a state between "running" and "startup". Diffs are created by moving `config.xml` around and seeing what changed.

Do not edit `config.xml` outside of NAPALM or you will be missing changes.

Editing the XML or diffing the XML is not supported, this may limit the amount of configuration we can provide in a 2-dimensional "set" like structure.

### Implemented APIs

* close
* get_arp_table
* get_config
* is_alive
* open
* get_facts
* get_interfaces
* get_interfaces_ip
* commit_config
* compare_config
* discard_config
* rollback
* load_merge_candidate
* get_users
* cli


### Missing APIs.

* compliance_report
* connection_tests
* get_bgp_config
* get_bgp_neighbors
* get_firewall_policies
* get_ipv6_neighbors_table
* get_network_instances
* get_optics
* get_probes_config
* get_probes_results
* get_route_to
* load_replace_candidate
* load_template
* post_connection_tests
* pre_connection_tests
* ping
* traceroute
* get_bgp_neighbors_detail
* get_environment
* get_interfaces_counters
* get_lldp_neighbors
* get_lldp_neighbors_detail
* get_mac_address_table
* get_ntp_peers
* get_ntp_servers
* get_ntp_stats
* get_snmp_information
* [...]
