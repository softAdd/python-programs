# task 1
print('Введите число от 1 до 9:')
x = int(input())

def betweenOneAndThree():
  print('Введите строку:')
  s = input()
  print('Введите число повторов строки:')
  n = int(input())
  s *= n
  print(s)

def betweenFourAndSix(x):
  print('Введите степень:')
  m = float(input())
  x **= m
  print(x)

def betweenSevenAndNine(x):
  for i in range(10):
    x += 1
    print(x)

if x in range(1, 4):
  betweenOneAndThree()
elif x in range(4, 7):
  betweenFourAndSix(x)
elif x in range(7, 10):
  betweenSevenAndNine(x)
else:
  print('Ошибка ввода')

# task 2
def printProgramName():
  print('Общество в начале XXI века')

def askForAge():
  print('Введите ваш возраст:')
  age = int(input())

  if age in range(0, 7):
    print('Вам в детский сад')
  elif age in range(7, 18):
    print('Вам в школу')
  elif age in range(18, 25):
    print('Вам в профессиональное учебное заведение')
  elif age in range(25, 60):
    print('Вам на работу')
  elif age in range(60, 121):
    print('Вам предоставляется выбор')
  else:
    print('Ошибка, это программа для людей!')

printProgramName()
askForAge()
