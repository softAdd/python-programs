print('Введите количество страниц:')
pageCount = input()
print('Введите номер страницы:')
pageNumber = input()

def convert_pages_to_tuple(pageCount, pageNumber):
    pageCount = int(pageCount)
    pageNumber = int(pageNumber)

    pageList = []
    for page in range(pageCount + 1):
        actualPage = page + 1
        if ((actualPage in range(pageNumber - 1, pageNumber + 2) or actualPage == 1) and actualPage < pageCount):
            pageList.append(actualPage)

    pageList.append(pageCount)

    return tuple(pageList)

def convert_tuple_to_string(convertibleTuple):
    pageList = list(convertibleTuple)
    pageList.sort(reverse = True)
    
    if (len(pageList) <= 1):
        result = ','.join(map(str, pageList))
        return result
    elif (len(pageList) < 3):
        result = '...'.join(map(str, pageList))
        return result
    else:
        resultStart = str(pageList[0])
        del pageList[0]
        resultEnd = str(pageList[len(pageList) - 1])
        del pageList[len(pageList) - 1]
        resultMiddle = ','.join(map(str, pageList))
        result = f'{resultStart}...{resultMiddle}...{resultEnd}'
        return result

    return None

def print_string_to_file(text):
    fs = open('output.txt', 'w')
    fs.write(text)
    fs.close()

resultTuple = convert_pages_to_tuple(pageCount, pageNumber)
resultString = convert_tuple_to_string(resultTuple)
print_string_to_file(resultString)