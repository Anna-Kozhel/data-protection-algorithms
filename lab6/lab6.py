def convertToMatrix(text):
    matrix = text.split("\n")
    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(" ")
        for j in range(len(matrix[i])):
            if len(matrix[i][j]) > 1: matrix[i][j] = matrix[i][j].split(",")
    return matrix


def findSymbol(symbol, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                if symbol == matrix[i][j][k]: return [i, j]


def PlayferRules(reshuffle, matrix, rule):
    line, variable = "", []
    for i in range(2):
        if rule == 0: variable = matrix[reshuffle[i - 1][0]][reshuffle[i][1]]
        if rule == 1: variable = matrix[reshuffle[0][0]][len(matrix[0]) - 1 if reshuffle[i][1] == 0 else reshuffle[i][1] - 1]
        if rule == 2: variable = matrix[len(matrix) - 1 if reshuffle[i][0] == 0 else reshuffle[i][0] - 1][reshuffle[1][1]]
        line += variable[0] if len(variable) == 1 else "(" + str(variable[0]) + "," + str(variable[1]) + ")"
    return line


def PlayferCipherDecoder(line, matrix):
    i, j, cipheredLine = 0, 1, ""
    while i < len(line) - 1 and j < len(line):
        first, second = findSymbol(line[i].lower(), matrix), findSymbol(line[j].lower(), matrix)
        if first[0] != second[0] and first[1] != second[1]: cipheredLine += PlayferRules([first, second], matrix, 0)
        if first[0] == second[0]: cipheredLine += PlayferRules([first, second], matrix, 1)
        if first[1] == second[1] and first[0] != second[0]: cipheredLine += PlayferRules([first, second], matrix, 2)
        i, j = i + 2, j + 2
    return cipheredLine


def readFile(fileName):
    with open(fileName, 'r') as file: return file.read()


def writeFile(line, fileName):
    with open(fileName, "w") as file: file.write(line)
    file.close()


def printMessage(line, encryptedLine, cipheredLine, matrix):
    print("\nЗакодований текст:\n" + cipheredLine)
    print("\nВідкритий текст:\n" + line)
    print("\nДекодований текст:\n" + encryptedLine + "\n\nТаблиця-ключ:")
    for row in matrix:
        for element in row:
            if len(element) == 1: print("\t['" + str(element), end="']\t")
            else: print("\t" + str(element), end="")
        print(end="\n")


openText, cipheredText = readFile("openTextLab5.txt"), readFile("cipheredTextLab5.txt")
cipherMatrixText = readFile("matrixLab5.txt")
cipherMatrix = convertToMatrix(cipherMatrixText)
encryptedText = PlayferCipherDecoder(cipheredText, cipherMatrix)
writeFile(encryptedText, "encryptedText.txt")
printMessage(openText, encryptedText, cipheredText, cipherMatrix)
