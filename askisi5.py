import re
from collections import Counter


def removeNonChars():
    with open('two_cities_ascii.txt', 'r+') as file:
        file = file.read()

        new_string = re.sub('[^a-zA-Z]+', ' ', file)

    return new_string.lower()


def main():
    # Step A
    array = removeNonChars().split()
    counter = Counter(array)
    print(" Oι δέκα δημοφιλέστερες λέξεις είναι:", counter.most_common(10))

    # Step B
    # print(counter)
    counter = counter.most_common(40)
    combinationsFor2Letters = []
    combinationsFor3Letters = []
    for word in counter:
        word = word[0]
        if len(word) > 1:
            for word_2 in counter:
                word_2 = word_2[0]
                if len(word_2) > 1:
                    if word[:2] == word_2[:2] and word is not word_2 and word not in combinationsFor2Letters and word_2 not in combinationsFor2Letters:
                        combinationsFor2Letters.append([word, word_2])
                    if word[:3] == word_2[:3] and word is not word_2 and word not in combinationsFor3Letters and word_2 not in combinationsFor3Letters:
                        combinationsFor3Letters.append([word, word_2])

    print("οι δύο πρώτοι συνδυασμοί δύο πρώτων γραμμάτων είναι: ", combinationsFor2Letters)
    print("οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων είναι: ", combinationsFor3Letters)


if __name__ == "__main__":
    main()
