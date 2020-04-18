# 7.1
fib1 = 0
fib2 = 1
n = 18
i = 0
fib_sum = 0
modified_fib_list = []

while i < n:
  fib_sum = fib1 + fib2
  fib1 = fib2
  fib2 = fib_sum
  i = i + 1
  if (i > 2):
    modified_fib_list.append(fib_sum)

print('Фибоначчи с 5 по 20:', modified_fib_list)

# 7.2
even_list = []
odd_list = []

i = 0

while i <= 20:
  even_list.append(i)
  i = i + 2

i = -3

while i >= -21:
  odd_list.append(i)
  i = i - 3
  

print('Четные:', even_list)
print('Каждое третье:', odd_list)

# 7.3
i = 0

while True:
  i = i + 1
  if (i > 10):
    print(i)
    break