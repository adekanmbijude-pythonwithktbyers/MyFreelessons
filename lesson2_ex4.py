#!/usr/bin/env python
with open("show_arp.txt", mode="r") as f:
	show_arp = f.readlines()
	print(show_arp)
	for line in show_arp:
        	print(line.strip()) #this will enable structured printout
	print(type(show_arp))
	print(len(show_arp))
	print(show_arp[0].strip()) #this will print out the first line = Header line
	print(show_arp[1].strip()) #This will print the first tabular data
	print(show_arp[-1].strip()) #This will print the last  tabular data
fields = show_arp[0].split() #this will help split the header in the show-arp into fields and saved in variable fields
print(fields)
print(type(fields))
print(len(fields))
print(fields[0]) #This will print the first field
print(fields[-1]) #This will print the last field
fields.remove('(min)')
find_hardware_index = fields.index('Hardware')
print(find_hardware_index)
fields[find_hardware_index] = "Hardware_Addr"
fields.remove("Addr")
print(fields)
