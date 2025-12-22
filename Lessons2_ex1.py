#!/usr/bin/env python
#base_address = "192.168.254."
#subnet_prefix = int(input("Enter subnet prefix length (25-30): "))
#Total_number_of_host_in_prefix = int(2**(32-subnet_prefix))
#Usable_num_hosts = Total_number_of_host_in_prefix - 2
#network_block_size = Total_number_of_host_in_prefix//256
#num_hosts = network_block_size - 2
#first_subnet_network = base_address + "0"
#second_subnet_network = base_address + str(network_block_size)
#first_host = base_address + "1"
#last_host_number = Total_number_of_host_in_prefix//256 - 1
#last_host = base_address + str(last_host_number)
#print("Number of usable hosts in subnet:", num_hosts)
#print("First subnet: ", first_subnet_network)
#print("Second subnet:", second_subnet_network)
#print("Host addresses in first subnet:")
#print("First host:", first_host)
#print("Last host: ", last_host)
#print()

base_address = "192.168.254."
subnet_prefix = int(input("Enter subnet prefix length (25-30): "))
subnet_size = int(2**(32-subnet_prefix))
num_hosts = subnet_size - 2
first_subnet_network = base_address + "0"
second_subnet_network = base_address + str(subnet_size)
first_host = base_address + "1"
last_host_number = subnet_size - 2
last_host = base_address + str(last_host_number)
print("1. Number of hosts in subnet:", num_hosts)
print("2. Network numbers:")
print("   First subnet: ", first_subnet_network)
print("   Second subnet:", second_subnet_network)
print("3. Host addresses in first subnet:")
print("   First host:", first_host)
print("   Last host: ", last_host)
print()
