print('Введите количество страниц:')
pageCount = input()
print('Введите номер страницы:')
pageNumber = input()

def create_page_list(pageCount, pageNumber):
    pageCount = int(pageCount)
    pageNumber = int(pageNumber)

    pageList = []
    for page in range(pageCount + 1):
        actualPage = page + 1
        if ((actualPage in range(pageNumber - 1, pageNumber + 2) or actualPage == 1) and actualPage < pageCount):
            pageList.append(actualPage)

    pageList.append(pageCount)
    pageList.sort(reverse = True)

    return pageList

def find_point_positions(pageList):
    pointPositions = []

    for i in range(len(pageList) - 1):
        if (pageList[i] - 1 != pageList[i + 1]):
            pointPositions.append(i)

    return pointPositions

def create_result_list(pageList, pointPositions):
    resultList = pageList
    incrementer =  1
    for i in pointPositions:
        resultList.insert(i + incrementer, '...')
        incrementer += 1

    commaPositions = []
    for i in range(len(resultList) - 1):
        commaPositions.append(i + 1)

    incrementer =  0
    for i in commaPositions:
        resultList.insert(i + incrementer, ',')
        incrementer += 1

    return resultList


def print_string_to_file(text):
    fs = open('output.txt', 'w')
    fs.write(text)
    fs.close()

pageList = create_page_list(pageCount, pageNumber)
pointPositions = find_point_positions(pageList)
resultList = create_result_list(pageList, pointPositions)
text = ''.join(map(str, resultList))
print_string_to_file(text)