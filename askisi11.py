from urllib.request import Request, urlopen
from binascii import unhexlify, hexlify
from math import log
import json


def calculateEntropy(hexString):
    """Calculates the Shannon entropy of a string"""

    # get probability of chars in string
    prob = [float(hexString.count(c)) / len(hexString) for c in dict.fromkeys(list(hexString))]

    # calculate the entropy
    entropy = - sum([p * log(p) / log(2.0) for p in prob])

    return entropy


def mergeRandomness(randomnessArray):

    mergedRandomness = bytes()
    for randomness in randomnessArray:
        randomness = unhexlify(randomness)
        mergedRandomness += randomness

    return hexlify(mergedRandomness)


def findLatest():

    req = Request(' https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read().decode())
    latestRound = int(str(data["round"]))

    return latestRound


def findRangeOfRounds(latestRound):
    firstRound = latestRound - 20
    randomness_array = []

    for roundNumber in range(firstRound, latestRound + 1):
        req = Request('https://drand.cloudflare.com/public/' + str(roundNumber), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
        data = json.loads(urlopen(req).read().decode())

        randomness_array.append(data["randomness"])

    return randomness_array


def main():
    latestRound = findLatest()
    rangeOfRoundsArray = findRangeOfRounds(latestRound)
    mergedRandomness = mergeRandomness(rangeOfRoundsArray).decode()
    entropy = calculateEntropy(mergedRandomness)
    print("Final entropy: ", entropy)


if __name__ == "__main__":
    main()
