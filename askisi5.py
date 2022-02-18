import re
from collections import Counter

def remove_Non_Chars():
    with open('two_cities_ascii.txt', 'r+') as file:
        file = file.read()

        new_string = re.sub('[^a-zA-Z]+', ' ', file)

    return new_string.lower()

def main():
    # ΒΗΜΑ 1
    arr = remove_Non_Chars().split()
    counter = Counter(arr)
    print(" Oι δέκα δημοφιλέστερες λέξεις είναι:", counter.most_common(10))

    # ΒΗΜΑ 2
    # print(counter)
    counter = counter.most_common(40)
    combination2 = []
    combination3= []
    for word in counter:
        word = word[0]
        if len(word) > 1:
            for word2 in counter:
                word2 = word2[0]
                if len(word2) > 1:
                    if word[:2] == word2[:2] and word is not word2 and word not in combination2 and word2 not in combination2:
                        combination2.append([word, word2])
                    if word[:3] == word2[:3] and word is not word2 and word not in combination3 and word2 not in combination3:
                        combination3.append([word, word2])

    print("οι δύο πρώτοι συνδυασμοί δύο πρώτων γραμμάτων είναι: ", combination2)
    print("οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων είναι: ", combination3)

if __name__ == "__main__":
    main()
