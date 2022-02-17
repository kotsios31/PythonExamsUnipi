import re
from collections import Counter


def removeNonChars():
    with open('two_cities_ascii.txt', 'r+') as file:
        file = file.read()

        new_string = re.sub('[^a-zA-Z]+', ' ', file)

    return new_string


def sumOfWord(word):
    return sum((ord(char) - 64) for char in word)


def wordLengthFreq(array):
    tmp = f'Οι χαρακτήρες των λέξεων βρίσκονται στα αριστερά και μετά το (:) το πόσες φορές υπάρχουν.\n {Counter(map(len, array))}'
    print(tmp)


def main():
    onlyAlpha_txt = removeNonChars().split(" ")
    filtered_txt = list(filter(None, onlyAlpha_txt))

    listWithSumNon20 = []
    for word in filtered_txt:
        if sumOfWord(word) != 20:
            listWithSumNon20.append(word)

    wordLengthFreq(listWithSumNon20)


if __name__ == "__main__":
    main()
