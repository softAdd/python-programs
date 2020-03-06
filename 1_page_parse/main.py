import requests
import re

siteContent = requests.get('http://lib.stat.cmu.edu/datasets/boston').content
siteData = re.split(r'\n\n', siteContent)[2]
dataLines = re.split(r'\n', siteData)
linesCount = len(dataLines) - 1

parsedData = []
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

print(parsedData[0])
print(parsedData[1])
print(parsedData[2])
print(parsedData[3])