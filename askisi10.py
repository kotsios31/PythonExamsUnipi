def loadText():
    with open('two_cities_ascii.txt', 'r') as file:
        text = file.read()

    return text


def text_BinarySeven(text):
    bin7 = [format(ord(char), '07b') for char in text]

    return bin7


def getFirst_LastTwo(arr):
    string = ''
    for bin7Char in arr:
        firstBits = bin7Char[:2]
        lastBits = bin7Char[-2:]
        fourBits = firstBits + lastBits
        string += fourBits
    return string


def split_SixteenBits(string):
    arr = [string[i:i + 16] for i in range(0, len(string), 16)]

    return arr

def make_Arrays(split_Bits):
    divided_Two, divided_Three, divided_Five, divided_Seven = [], [], [], []

    for sixteenBits in split_Bits:
        num = int(sixteenBits, 2)
        if num % 2 == 0:
            divided_Two.append(num)

        if num % 3 == 0:
            divided_Three.append(num)

        if num % 5 == 0:
            divided_Five.append(num)

        if num % 7 == 0:
            divided_Seven.append(num)

    return divided_Two, divided_Three, divided_Five, divided_Seven


def main():
    text = loadText()
    sevenBitsArr = text_BinarySeven(text)
    firstAndLast = getFirst_LastTwo(sevenBitsArr)
    splitBits16 = split_SixteenBits(firstAndLast)

    divided_Two, divided_Three, divided_Five, divided_Seven = make_Arrays(splitBits16)

    length_Sixteen = len(splitBits16)

    print("From ", length_Sixteen, " ο αριθμός, ", len(divided_Two), "μπορεί να διαίρεθει ακριβώς με 2.")
    print("From ", length_Sixteen, " ο αριθμός, ", len(divided_Three), "μπορεί να διαίρεθει ακριβώς με 3.")
    print("From ", length_Sixteen, " ο αριθμός, ", len(divided_Five), "μπορεί να διαίρεθει ακριβώς με 5.")
    print("From ", length_Sixteen, " ο αριθμός, ", len(divided_Seven), "μπορεί να διαίρεθει ακριβώς με 7.")

if __name__ == "__main__":
    main()

