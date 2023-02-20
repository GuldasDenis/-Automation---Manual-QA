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
odd_list = []
even_list = []
for index in range(len(elements)):
    if index % 2 == 0:
        odd_list.append((index, elements[index]))
    else:
        even_list.append((index, elements[index]))
print("Список кортежей с нечетными индексами:", odd_list)
print("Список кортежей с четными индексами:", even_list)