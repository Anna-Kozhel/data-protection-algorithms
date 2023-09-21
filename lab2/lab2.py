import random


def createProportionalReplacement(abc):
    table, data = [[] for _ in range(len(abc[0]))], []
    for i in range(len(abc[0])):
        for k in range(abc[1][i]):
            while True:
                cipheredSymbol = random.randint(100, 999)
                if cipheredSymbol not in data:
                    table[i].append(cipheredSymbol)
                    data.append(cipheredSymbol)
                    break
    return table


def findSymbol(symbol, abc):
    if symbol in abc[0]: return abc[0].index(symbol)


def replaceSymbolWithNumber(abc, table, line):
    cipheredLine = ""
    for symbol in line:
        i = findSymbol(symbol.lower(), abc)
        cipheredLine += f"{random.choice(table[i])}"
    return cipheredLine


def writeFile(line, fileName):
    with open(fileName, "w") as file:
        file.write(line)
        file.close()


def printMessage(line, cipheredLine, table, abc):
    print("\nВідкритий текст:\n" + line + "\n")
    print("Зашифрований текст:\n" + cipheredLine + "\n\nТаблиця пропорційної заміни:")
    for row in table:
        print("\n"+abc[0][table.index(row)], end="\t")
        for element in row: print(element, end="\t")


alphabet = [
    ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
     "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я", " "],
    [6, 2, 4, 2, 1, 3, 4, 1, 1, 2, 5, 4, 1, 1, 4, 3, 3, 7, 9, 3, 4, 4, 4, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2, 14]]
text = "Львів це місто яке розташоване на заході України славиться своєю великою історією чарівною архітектурою великим культурним спадком та неймовірною гостинністю своїх мешканців"

writeFile(text, "openText.txt")
replacementTable = createProportionalReplacement(alphabet)
cipheredText = replaceSymbolWithNumber(alphabet, replacementTable, text)
writeFile(cipheredText, "cipheredText.txt")
printMessage(text, cipheredText, replacementTable, alphabet)
