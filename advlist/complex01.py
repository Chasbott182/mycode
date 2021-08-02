#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

# print second element in the list
print(list1[1])

# Second list
list2 = ["juniper"]

# extend list1 with list2
list1.extend(list2)

print(list1)

# create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

# use the append operation to append list1 by list3
list1.append(list3)

# display the new complex list1
print(list1)

print(list1[4])

print(list1[4][0])
