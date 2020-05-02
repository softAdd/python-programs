#  task 1
list1 = ['Привет', 'из', 'массива строк.', 'Как дела?']

for i in list1:
  print(i)

# task 2
for i in list1:
  for j in i:
    print(j, end='.')
  print()

# task 3
list2 = [56, 78, 45, 23]
i = 0

for a in list2:
  list2[i] = float(a)
  i += 1

print(list2)