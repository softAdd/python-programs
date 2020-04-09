def create_page_list(pageCount, pageNumber):
    pageCount = int(pageCount)
    pageNumber = int(pageNumber)

    pageList = []
    for page in range(pageCount + 1):
        actualPage = page + 1
        if ((actualPage in range(pageNumber - 1, pageNumber + 2) or actualPage == 1) and actualPage < pageCount):
            pageList.append(actualPage)

    pageList.append(pageCount)

    print(pageList)
    return pageList

def find_point_positions(pageList):
    pointPositions = []

    for i in range(len(pageList) - 1):
        if (pageList[i] - 1 != pageList[i + 1]):
            pointPositions.append(i)

    print(pointPositions)
    return pointPositions
print('Point positions:')
# []
pointPositions = find_point_positions([])
# []
pointPositions = find_point_positions([1])
# []
pointPositions = find_point_positions([2, 1])
# []
pointPositions = find_point_positions([3, 2, 1])
# []
pointPositions = find_point_positions([4, 3, 2, 1])
# [0]
pointPositions = find_point_positions([5, 3, 2, 1])
# [0, 3]
pointPositions = find_point_positions([15, 10, 9, 8, 1])
print('Page list:')
# []
pageList = create_page_list(0, -1)
# [1]
pageList = create_page_list(1, 1)
# [1, 2]
pageList = create_page_list(2, 1)
# [1, 2, 3]
pageList = create_page_list(3, 2)
# [1, 2, 3, 4]
pageList = create_page_list(4, 2)
# [1, 6, 7, 8, 12]
pageList = create_page_list(12, 7)
