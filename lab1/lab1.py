def findSymbol(symbol, alphabet):
    for i in range(len(alphabet)):
        if symbol in alphabet[i]: return i, alphabet[i].index(symbol)


def cipherDecoder(symbol, alphabet, shift):
    i, index = findSymbol(symbol, alphabet)
    index += shift
    if index > len(alphabet[i]) - 1:
        return alphabet[i][index - len(alphabet[i])]
    else:
        return alphabet[i][index]


def writeFile(text, fileName, type):
    with open(fileName, type) as file:
        file.write(text)
        file.close()


def readFile(fileName):
    with open(fileName, 'r') as file: return file.read()


def cipherShift(text, alphabet, shift, fileName):
    writeFile(text, fileName, 'w')
    text, textShift, textDecode = readFile(fileName), "", ""
    for symbol in text:
        textShift += cipherDecoder(symbol, alphabet, shift)

    writeFile("\n\n" + textShift, fileName, 'a')

    for symbol in textShift:
        textDecode += cipherDecoder(symbol, alphabet, -shift)

    return printMessage(textShift, textDecode, fileName)


def printMessage(textShift, textDecode, fileName):
    print("\nПрочитаний шифр зі зсувом з файлу " + fileName + ":\n" + textShift + "\n")
    print("Декодований шифр у текст:\n" + textDecode + "\n\n")


alphabetUA = [
    ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
     "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"],
    ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
     "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я"]]
alphabetEN = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z"],
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
     "X", "Y", "Z"], [" ", ",", ".", ";", ":", "!", "?", "(", ")", "[", "]", "\'", "\"", "-"]]

textUA = "ЛьвівцемістоякерозташованеназаходіУкраїниславитьсясвоєювеликоюісторієючарівноюархітектуроювеликимкультурнимспадкомтанеймовірноюгостинністюсвоїхмешканців"
textEN = "Lviv, often referred to as the 'City of Lions,' is a picturesque and historic city located in western Ukraine."
SHIFT = 12

cipherShift(textUA, alphabetUA, SHIFT, "cipheredFileUA.txt")
cipherShift(textEN, alphabetEN, SHIFT, "cipheredFileEN.txt")
