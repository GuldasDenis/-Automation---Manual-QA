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
# command1 = "switchport trunk allowed vlan 1,2,3,5,8"
# command2 = "switchport trunk allowed vlan 1,3,8,9"
# result1 = command1.split()[4]
# result1 = result1.split(',')
# result2 = command2.split()[4]
# result2 = result2.split(',')
# preobrazovanie = list(set(result1) & set(result2)) # преобразовал список во множество(set), (&) операция пересецения множест (list) создал обратно список
# print(preobrazovanie)
#4.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = ospf_route.replace(",", "").replace("via", "").split() # Метод split() разбивает строку на части, используя как разделитель какой-то символ (или символы) и возвращает список строк:
list2 = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]
for list1, list2, list3 in zip(list1, list2): #Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи. Функция останавливается, когда заканчиваются элементы в одном из источников. Относится к неперезапускаемым генераторам.
    print('{:20}{:20}'.format(list2, list1))

# #4.7
# a = input("mac:   ")
# mac = (a)
# r = int(a.replace(":",""))
# print(bin(r))