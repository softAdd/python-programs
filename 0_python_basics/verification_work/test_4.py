# task 1
print('Введите строку:')
s = input()
result = s.split(' ')
result = list(filter(lambda s: s[0].lower() == 'а', result))
print('Слова, начинающиеся с буквы а:', result)
print('Количество:', len(result))

# task 2
print('Введите текст:')
text = input()

re = __import__('re')
reg_exp = '^([0-9]*\.?[0-9]+)$'

if re.match(reg_exp, text) is not None:
  num = float(text)
  if num % 4 == 0:
    print('Число кратно 4.')
  else:
    print('Число не кратно 4.')
else:
  print('Текст не является записью десятичного числа.')

# task 3 -> you can insert also numbers greater than 100
from word2number.w2n import word_to_num
from googletrans import Translator
import re

print('Введите текст, выделяя цифровые значения, пример: <Две тысячи> собак лаяли в <трех> дворах.')
text = input()

search_pattern = r'<[^<>]+>'
matches = re.findall(search_pattern, text)

def word_to_number(matches_with_pattern):
  try:
    translator = Translator()
    number = matches_with_pattern[1:-1]
    # w2n accepts only english words
    number = translator.translate(number).text
    number = word_to_num(number)
    return number
  except:
    return '<Error>'

numbers = list(map(word_to_number, matches))

for i in range(len(matches)):
  number = str(numbers[i])
  text = text.replace(matches[i], number, 1)

print(text)