from urllib.request import Request, urlopen
from binascii import unhexlify, hexlify
import json


def maxConsecutive(binaryRandomness):
    maxOnes = max(map(len, binaryRandomness.split('0')))
    maxZeros = max(map(len, binaryRandomness.split('1')))

    return maxOnes, maxZeros


def hexToBinaryConversion(hexRandomness):

    result = bin(int(hexRandomness, 16))

    return result[2:]


def mergeRandomness(randomnessArray):

    mergedRandomness = bytes()
    for randomness in randomnessArray:
        randomness = unhexlify(randomness)
        mergedRandomness += randomness

    return hexlify(mergedRandomness)


def findLatest():

    req = Request(' https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; '
                                                                                        'WOW64; rv:31.0) '
                                                                                        'Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read().decode())
    latestRound = int(str(data["round"]))

    return latestRound


def findRangeOfRounds(latestRound):
    firstRound = latestRound - 99
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
    binaryRandomness = hexToBinaryConversion(mergedRandomness)

    maxOnes, maxZeros = maxConsecutive(binaryRandomness)
    print("Length of biggest sequence of 1s: ", maxOnes)
    print("Length of biggest sequence of 0s: ", maxZeros)


if __name__ == "__main__":
    main()
