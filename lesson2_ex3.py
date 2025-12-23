#!/usr/bin/env python
ip_addresses = ["192.168.10.0","192.168.10.1","192.168.10.2","192.168.10.3","192.168.10.4"]
print(ip_addresses)
ip_addresses.append("192.168.10.5")
print(ip_addresses)
ip_addresses.extend(["192.168.10.6","192.168.10.7"])
print(ip_addresses)
new_ip = ip_addresses + ["192.168.10.8", "192.168.10.9"]
print(new_ip)
print(new_ip[0])
print(new_ip[-1])
new_ip.pop()
print(new_ip)
new_ip.pop(0)
print(new_ip)
new_ip.insert(0,"2.2.2.2")
print(new_ip)
