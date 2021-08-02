#!/usr/bin/env python3

# create a list
my_list = ["192.168.0.5",4567, "UP"]

# Print the first element in the list
print("The first item in the list (IP): " + my_list[0])

# Print the second element in the list
print("The second item in the list (port): " + str(my_list[1]) )

# Print the last element in the list
print("The last item in the list (state): " + my_list[2] )

#CHALLENGE

iplist = iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("IP addresses:", iplist[3] +",", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

