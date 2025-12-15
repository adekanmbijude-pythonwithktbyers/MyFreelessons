#!/usr/bin/env python
Location = input("Please Enter location:")
print(Location.upper())
print(f"Before whitespace: {repr(Location)}")
Location = input("Please Enter location:"   )
print(f"After whitespace: {repr(Location)}")
print(repr(Location.upper().strip()))

