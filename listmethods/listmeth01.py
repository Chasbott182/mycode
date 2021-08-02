#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
protoa = ["ssh", "http", "https"]


print(proto[1])

proto.extend("dns") #this line will add d,n, and s

print(proto)

proto.append("dns") #add 'dns' to the end of the list
protoa.append("dns") #add 'dns' to the end of the list

print(proto)

proto2 = [22, 80, 443, 53] # a list of numbers

proto.extend(proto2) # add iterate through proto2 and add it to proto

print(proto)

protoa.append(proto2) # add proto2 list to the end of protoa

print(protoa)

protoa.pop()

print(protoa)
