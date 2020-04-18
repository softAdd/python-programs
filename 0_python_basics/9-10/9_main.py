import math

# 9.1
text = '123/#a;ls492a'
print('Первый символ:', text[0])
print('Последний символ:', text[-1])
print('Третий символ с начала:', text[2])
print('Третий символ с конца:', text[len(text) - 3])
print('Букв в строке:', (len(text) - 1))

# 9.2
text = 'randomstring1234'
print('Первые восемь символов:', text[0:8])
str_center = math.floor(len(text) / 2)
str_left = str_center - 2
str_right = str_center + 2
print('Четыре символа из центра строки:', text[str_left:str_right])

result = ''

for i in range(0, len(text)):
  if (i % 3 == 0):
    result = result + text[i]

print('С индексами, кратными трем:', result)