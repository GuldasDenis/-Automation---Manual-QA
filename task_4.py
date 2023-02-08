# 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace("Fast", "Gigabit"))
#4.2
mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))
#4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()[4]
result = result.split(',')
print(result)