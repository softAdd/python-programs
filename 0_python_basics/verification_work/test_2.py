import math

# task 3
PAGES = 194
DAYS_COUNT = 3
A_VARIANTS = [28, 3, 25]
B_VARIANTS = [30, 3, 16]

def read_book(variant, title):
  A = variant[0]
  B = variant[1]
  C = variant[2]
  read_pages = A + (A * B) + (A * B - C)
  result = False if read_pages < PAGES else True

  if (not result):
    rest = PAGES - read_pages
    print(rest, 'не прочитано:', title)
  else:
    print('Все прочитано:', title)

  return result

first_question = read_book(A_VARIANTS, 'a')
second_question = read_book(B_VARIANTS, 'b')

# task 4
print('a:')
A = float(input())
print('b:')
B = float(input())
print('x:')
X = float(input())

result = None

if (A > 5 and B < -3):
  result = A + 2 * (B ** 2) + 3
elif (X < 0):
  result = X
elif (X == 0):
  result = 5
else:
  result = X + 1

print('y =', result)

# task 5
WEEK_DAYS = {
  '0': 'Понедельник',
  '1': 'Вторник',
  '2': 'Среда',
  '3': 'Четверг',
  '4': 'Пятница',
  '5': 'Суббота',
  '6': 'Воскресенье',
}

print('a:')
A = float(input())
print('b:')
B = float(input())
print('x:')
X = float(input())

Z = math.log((X ** 2) + (A * B))
rest = math.floor(Z) % 7

print(WEEK_DAYS[str(rest)])