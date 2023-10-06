import os
import random


def createMatrix(row, col, abc, doubleMax):
    matrix, doubleLetters = [[[] for _ in range(col)] for _ in range(row)], 0
    for i in range(row):
        j = 0
        while j < col:
            index = random.randint(0, len(abc) - 1)
            matrix[i][j].append(abc[index])
            abc.pop(index)
            if doubleLetters < doubleMax and len(matrix[i][j]) < 2 and random.randint(1, 2) == 2: doubleLetters += 1
            elif doubleLetters < doubleMax and i == row - 1 and j > col - doubleMax and len(matrix[i][j]) < 2: continue
            else: j += 1
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
        if rule == 1: variable = matrix[reshuffle[0][0]][0 if reshuffle[i][1] == len(matrix[0]) - 1 else reshuffle[i][1] + 1]
        if rule == 2: variable = matrix[0 if reshuffle[i][0] == len(matrix) - 1 else reshuffle[i][0] + 1][reshuffle[1][1]]
        line += variable[random.randint(0, len(variable) - 1)]
    return line


def PlayferCipher(line, matrix):
    i, j, cipheredLine = 0, 1, ""
    while i < len(line) - 1 and j < len(line):
        first, second = findSymbol(line[i].lower(), matrix), findSymbol(line[j].lower(), matrix)
        if first[0] != second[0] and first[1] != second[1]: cipheredLine += PlayferRules([first, second], matrix, 0)
        if first[0] == second[0]: cipheredLine += PlayferRules([first, second], matrix, 1)
        if first[1] == second[1] and first[0] != second[0]: cipheredLine += PlayferRules([first, second], matrix, 2)
        i, j = i + 2, j + 2
    return cipheredLine


def writeFile(line, fileName):
    with open(fileName, "w") as file: file.write(line)
    file.close()


def printMessage(line, cipheredLine, matrix):
    print("\nВідкритий текст:\n" + line + "\n")
    print("Зашифрований текст:\n" + cipheredLine + "\n\nТаблиця-ключ:")
    for row in matrix:
        for element in row:
            if len(element) == 1: print("\t" + str(element), end="\t")
            else: print("\t" + str(element), end="")
        print(end="\n")


alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р",
            "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
text = "ЛьвівЦеМістоЯкеРозташованеНаЗаходіУкраїниСлавитьсяСвоєюВеликоюІсторієюЧарівноюАрхітектуроюВеликимКультурнимСпадкомТаНеймовірноюГостинністюСвоїхМешканців"
row, col = 5, 6

writeFile(text, "openText.txt")
cipherMatrix = createMatrix(row, col, alphabet.copy(), len(alphabet) - row * col)
cipheredText = PlayferCipher(text, cipherMatrix)
writeFile(cipheredText, "cipheredText.txt")
printMessage(text, cipheredText, cipherMatrix)

# Lab 6
completePath = os.path.join("F:\Бакалаврат\\7 семестр\Захист даних\Лаби\Lab5\lab5", "..", "..", "Lab6/lab6/")
writeFile(text, completePath + "openTextLab5.txt")
writeFile(cipheredText, completePath + "cipheredTextLab5.txt")

writeFile("", completePath + "matrixLab5.txt")
for i in range(len(cipherMatrix)):
    for j in range(len(cipherMatrix[i])):
        for k in range(len(cipherMatrix[i][j])):
            if len(cipherMatrix[i][j]) == 2 and k != len(cipherMatrix[i][j]) - 1:
                with open(completePath + "matrixLab5.txt", "a") as file: file.write(f"{cipherMatrix[i][j][k]},")
            elif j == len(cipherMatrix[i]) - 1:
                with open(completePath + "matrixLab5.txt", "a") as file:file.write(f"{cipherMatrix[i][j][k]}")
            else:
                with open(completePath + "matrixLab5.txt", "a") as file: file.write(f"{cipherMatrix[i][j][k]} ")
    if i == len(cipherMatrix) - 1: break
    else:
        with open(completePath + "matrixLab5.txt", "a") as file: file.write(f"\n")
file.close()
