nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace("Fast", "Gigabit"))

mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))