import requests
import re
import pymongo


def get_data_lines(siteContent):
    siteData = re.split(r'\n\n', siteContent)[2]
    dataLines = re.split(r'\n', siteData)

    return dataLines


def parse_data(dataLines):
    parsedData = []
    linesCount = len(dataLines) - 1

    for lineNumber in range(0, linesCount):
        if (lineNumber % 2 == 1):
            line = dataLines[lineNumber - 1] + dataLines[lineNumber]
            digits = re.findall(r'\d+\.?\d*', line)

            parsedData.append({
                'CRIM': digits[0],
                'ZN': digits[1],
                'INDUS': digits[2],
                'CHAS': digits[3],
                'NOX': digits[4],
                'RM': digits[5],
                'AGE': digits[6],
                'DIS': digits[7],
                'RAD': digits[8],
                'TAX': digits[9],
                'PTRATIO': digits[10],
                'B': digits[11],
                'LSTAT': digits[12],
                'MEDV': digits[13]
            })

    return parsedData


def insert_data_to_db():
    siteContent = requests.get(
        'http://lib.stat.cmu.edu/datasets/boston').content.decode('utf-8')
    dataLines = get_data_lines(siteContent)
    parsedData = parse_data(dataLines)

    mongoClient = pymongo.MongoClient(
        'mongodb://root:example@localhost:27017/')
    dataDB = mongoClient['parsedata']

    if 'data' not in dataDB.list_collection_names():
        dataCollection = dataDB['data']
        insertedData = dataCollection.insert_many(parsedData)
        print(insertedData.inserted_ids)


def print_data_from_db():
    mongoClient = pymongo.MongoClient(
        'mongodb://root:example@localhost:27017/')

    dataDB = mongoClient['parsedata']
    dataCollection = dataDB['data']

    for data in dataCollection.find():
        print(data)


print('1 - добавить данные, 2 - прочитать данные, другое - остановиться.')
selectedType = input()
isStopped = False

while not isStopped:
    if (selectedType == '1'):
        insert_data_to_db()
        print(
            '\n\n\n1 - добавить данные, 2 - прочитать данные, другое - остановиться.\n\n\n')
        selectedType = input()
    elif (selectedType == '2'):
        print_data_from_db()
        print(
            '\n\n\n1 - добавить данные, 2 - прочитать данные, другое - остановиться.\n\n\n')
        selectedType = input()
    else:
        isStopped = True
