first_list = [1, 2, 3, 4, 5, 6, 7, 8]
second_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print('Второй элемент первого списка:', first_list[1])
second_list[len(second_list) - 1] = 0
print('Измененный второй список:', second_list)
common_list = first_list + second_list
print('Два списка в одном:', common_list)
part_common_list = common_list[::3]
print('Список-срез:', part_common_list)
part_common_list.append('FIRST')
part_common_list.append('SECOND')
print('Список-срез с двумя новыми элементами:', part_common_list)