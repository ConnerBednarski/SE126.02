# Conner Bednarski
# SE126.02
# Lab5A
#
# Variables:
# ipAddress         Holds all the IPs
# subnetMask        Holds the subnet mask for class B ips
# ip_split          Holds the split value from the original ip
# octect1           Holds the number from the first octet
#
#
#====Variable Declaration=============================================
ipAddress = []
subnetMask = '255.255.0.0'

#====Functions========================================================
def ipSplit(ip):
    '''Splits the IP and prints the ip if it's a class B'''
    ip_split = ip.split(".")
    ipAddress.append(ip)

    octet1 = (int) (ip_split[0])

    if ((octet1 >= 128) and (octet1 <= 191)):
        print("IP: {}SUBNET MASK: {}\n".format(ip, subnetMask))
    


    
#====Main Code=======================================================
with open("C:\\Users\\cbedn\\Downloads\\lab5a.txt") as file:
    lines = file.readlines()
    for row in lines:
        ipSplit(row)


