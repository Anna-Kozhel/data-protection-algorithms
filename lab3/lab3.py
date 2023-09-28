from itertools import chain


def writeProportionalReplacement(line):
    table = line.split('\n')
    table.pop()
    for i in range(len(table)):
        table[i] = table[i].split()
    return table


def findNumber(num, table):
    for i in range(len(table)):
        if num in table[i]: return i


def replaceNumberWithSymbol(abc, table, cipheredLine):
    line = ""
    for i in range(int(len(cipheredLine) / 3)): line += abc[findNumber(cipheredLine[3 * i:3 * (i + 1)], table)]
    return line


def writeFile(line, fileName):
    with open(fileName, "w") as file: file.write(line)
    file.close()


def readFile(fileName):
    with open(fileName, 'r') as file: return file.read()


def openFrequency(line, abc):
    frequency = [0 for _ in range(len(abc))]
    for symbol in line: frequency[abc.index(symbol)] += 1
    return frequency


def cipheredFrequency(line, dataReplacement):
    frequency = [0 for _ in range(len(dataReplacement))]
    for i in range(int(len(line) / 3)): frequency[dataReplacement.index(line[3 * i:3 * (i + 1)])] += 1
    return frequency


def printMessage(line, cipheredLine, encryptedLine, abc, openFrequency, table, cipheredFrequency):
    print("\nЗашифрований текст:\n" + cipheredLine + "\n\nДешифрований текст:\n" + encryptedLine + "\n\nВідкритий текст:\n" + line + "\n")
    print("Частота літер у відкритому тексті:\n\nлітера\tчастота")
    for i in range(len(openFrequency)): print("  " + abc[i] + "\t\t  " + f"{openFrequency[i]}", end="\n")
    print("\nЧастота символів у криптограмі:\n\nсимвол\tчастота")
    for i in range(len(cipheredFrequency)): print(" " + table[i] + "\t   " + f"{cipheredFrequency[i]}", end="\n")


alphabet = [
    ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
     "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я", " "],
    [6, 2, 4, 2, 1, 3, 4, 1, 1, 2, 5, 4, 1, 1, 4, 3, 3, 7, 9, 3, 4, 4, 4, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2, 14]]
text = "Львів це місто яке розташоване на заході України славиться своєю великою історією чарівною архітектурою великим культурним спадком та неймовірною гостинністю своїх мешканців"

cipheredText = readFile("cipheredTextLab2.txt")
dataReplacementTableText = readFile("replacementTableTextLab2.txt")
replacementTable = writeProportionalReplacement(dataReplacementTableText)
openText = replaceNumberWithSymbol(alphabet[0], replacementTable, cipheredText)
writeFile(openText, "encryptedText.txt")
openFrequencyTable = openFrequency(openText, alphabet[0])
dataReplacementTable = list(chain(*replacementTable))
dataReplacementTable.sort()
cipheredFrequencyTable = cipheredFrequency(cipheredText, dataReplacementTable)
printMessage(text, cipheredText, openText, alphabet[0], openFrequencyTable, dataReplacementTable, cipheredFrequencyTable)
