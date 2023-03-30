import time
import random


def generateNumbers(numberList, numberDictionary):
    for i in range(1000):
        numberRandom = random.randrange(1, 10001)
        numberList.append(numberRandom)
        numberDictionary.update({i: numberRandom})


def test1(numberList, numberDictionary):
    startTime = checkTime()
    print(numberList)
    listTime = checkTime() - startTime

    startTime = checkTime()
    print(numberDictionary)
    dictionaryTime = checkTime() - startTime

    print("The list took " + str(listTime) + " seconds to print and the dictionary took " +
          str(dictionaryTime) + "seconds.")


def test2(numberList, numberDictionary):
    numberRandom = random.choice(numberList)
    startTime = checkTime()
    numberList.index(numberRandom)
    listTime = checkTime() - startTime

    startTime = checkTime()
    for k, v in numberDictionary.items():
        if v == numberRandom:
            break
    dictionaryTime = checkTime() - startTime

    print("The list took " + str(listTime) + " seconds to retrieve the number and the dictionary took "
          + str(dictionaryTime) + " seconds to retrieve the number.")


def test3(numberList, numberDictionary):
    numberRandom = random.randrange(1, 10001)
    startTime = checkTime()
    numberList.insert(len(numberList), numberRandom)
    print(numberList)
    listTime = checkTime() - startTime

    startTime = checkTime()
    numberDictionary[len(numberDictionary)] = numberRandom
    print(numberDictionary)
    dictionaryTime = checkTime() - startTime

    print("The list took " + str(listTime) + " seconds to insert and the dictionary took "
          + str(dictionaryTime) + " seconds to insert.")


def test4(numberList, numberDictionary):
    numberRandom = random.choice(numberList)
    dictionaryKey = 0
    startTime = checkTime()
    numberList.remove(numberRandom)
    listTime = checkTime() - startTime

    startTime = checkTime()
    for k, v in numberDictionary.items():
        if numberRandom == v:
            dictionaryKey = k
            break
    del numberDictionary[dictionaryKey]
    dictionaryTime = checkTime() - startTime

    print("The list took " + str(listTime) + " seconds to remove the value and "
          + "the dictionary took " + str(dictionaryTime) + " seconds")


def checkTime():
    return time.perf_counter()


numberList = []
numberDictionary = {}

generateNumbers(numberList, numberDictionary)

test1(numberList, numberDictionary)
test2(numberList, numberDictionary)
test3(numberList, numberDictionary)
test4(numberList, numberDictionary)
