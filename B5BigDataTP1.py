from random import randint
from hashfunctions import hassan_alachek_simpleModuloHash, hassan_alachek_efficientHash, hassan_alachek_sdbm, \
    hassan_alachek_cyclicShift
from fileReader import fileReader, fileLen
import matplotlib.pyplot as plt


def createTAD(M):
    X = [0 for _ in range(M)]
    return X


def printTable(X):
    for i in range(len(X)):
        print(f"[+] Element Number [{i}] = {X[i]}")


def putInTAD(X, index):
    X[index] += 1
    return X


# M = Length
def evaluateTAD(X):
    if len(X) == 0:
        print("[-] Empty Array")
        exit(1)
    else:
        numOfNonAccededCell = 0
        numOfCollision = 0
        average = 0
        for i in range(len(X)):
            if X[i] == 0:
                numOfNonAccededCell += 1
            else:
                if X[i] > 1:
                    numOfCollision += (X[i] - 1)
                average += X[i]
        average /= (len(X) - numOfNonAccededCell)
        arrayMin = min([x for x in X if x != 0])
        arrayMax = max(X)

        return numOfNonAccededCell, arrayMin, arrayMax, average, numOfCollision


def printStatistic(X):
    numOfNonAccededCell, arrayMin, arrayMax, average, numOfCollision = evaluateTAD(X)
    print(f"""
    [+] Number Of Element Not Acceded Yet Is: {numOfNonAccededCell}
    [+] The Minimum Access To Cell Acceded Is: {arrayMin}
    [+] The Maximum Access To Cell Acceded Is: {arrayMax}
    [+] The Average Value Of Access Is: {average}
    [+] Number of Collision Is: {numOfCollision}
    """)


def randomAccessToTAD(X, R):
    arrayLength = len(X)
    for i in range(R):
        randomIndex = randint(0, arrayLength - 1)
        X = putInTAD(X, randomIndex)
    return X


# Plot a histogram to compare the
# Number of collision between hash functions
def plotCollisionNumber(X):
    numOfCollision = [evaluateTAD(X[i])[4] for i in range(4)]

    hashFunction = ["simpleModuloHash", "efficientHash", "sdbm", "cyclicShift"]
    plt.bar(hashFunction, numOfCollision)
    plt.title("Collision Comparison")
    plt.xlabel("Hash Function")
    plt.ylabel("Number Of Collisions")
    plt.show()


# def main():
#     R = 5
#     M = 10
#     X = createTAD(M)
#     print("[+] Empty Array")
#     printTable(X)
#     X = randomAccessToTAD(X, R)
#     print("[+] Non-Empty Array")
#     printTable(X)
#     printStatistic(X)

def main():
    hashFunction = ["simpleModuloHash", "efficientHash", "sdbm", "cyclicShift"]
    fileName = ['word.txt']
    M = int((10 / 3) * fileLen(fileName[0]))
    print(M)
    X = [createTAD(M) for _ in range(4)]

    lines = fileReader(fileName[0])
    for line in lines:
        X[0] = putInTAD(X[0], hassan_alachek_simpleModuloHash(line.strip(), M))
        X[1] = putInTAD(X[1], hassan_alachek_efficientHash(line.strip(), M))
        X[2] = putInTAD(X[2], hassan_alachek_sdbm(line.strip(), M))
        X[3] = putInTAD(X[3], hassan_alachek_cyclicShift(line.strip(), M))

    plotCollisionNumber(X)

    # Console Prints
    hashFunction = ["simpleModuloHash", "efficientHash", "sdbm", "cyclicShift"]
    for i in range(4):
        print(f"\tStatistic For Hash Function {hashFunction[i]}")
        printStatistic(X[i])


if __name__ == '__main__':
    main()