# #1
# my_array = [1, 2.5, "hello", True, [3, 4, 5]]
#
# print("For loop:")
# for i in my_array:
#     print(i)
#
# print("\nWhile loop:")
# i = 0
# while i < len(my_array):
#     print(my_array[i])
#     i += 1
#
#
# #2
# var = 10
# if var == 10:
#     result = True
# else:
#     result = False
#
# print(result)
#
# #3
elements = [1, 2, 3, 4, 5, 6, 7, 8]
list1 = []
list2 = []
for index in range(len(elements)):
    if index % 2 == 0:
        list1.append((index, elements[index]))
    else:
        list2.append((index, elements[index]))
print("Список кортежей с нечетными индексами:", list1)
print("Список кортежей с четными индексами:", list2)