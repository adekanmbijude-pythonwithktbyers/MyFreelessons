#!/usr/bin/env python
f = open("show_version.txt")
data = f.readline()
f.close()
print(data)
print(type(data))

with open("show_version.txt", "r") as f:
	data = f.readline()
	print(data)
	print(type(data))
