# # 4.1
# nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# print(nat.replace("Fast", "Gigabit"))
# #4.2
# mac = "AAAA:BBBB:CCCC"
# print(mac.replace(":", "."))
# #4.3
# config = "switchport trunk allowed vlan 1,3,10,20,30,100"
# result = config.split()[4]
# result = result.split(',')
# print(result)
#4.4
# vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# vlans = set(vlans)
# print(sorted(vlans))
#4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
result1 = command1.split()[4]
result1 = result1.split(',')
result2 = command2.split()[4]
result2 = result2.split(',')
preobrazovanie = list(set(result1) & set(result2))
print(preobrazovanie)