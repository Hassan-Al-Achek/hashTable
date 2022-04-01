from hashfunctions import hassan_alachek_efficientHash
from fileReader import fileReader, fileLen
import sys


def createTAD(M):
    X = [[] for _ in range(M)]
    return X


def printTable(X):
    for i in range(len(X)):
        print(f"[+] Element Number [{i}] = {X[i]}")


def htInsert(hashTable, element, length):
    index = hassan_alachek_efficientHash(element, length)
    hashTable[index].append(element)


def htSearch(hashTable, key, length):
    index = hassan_alachek_efficientHash(key, length)
    if len(hashTable[index]) > 1:
        searchElementIndex = hashTable[index].index(key)
        return hashTable[index][searchElementIndex]

    if len(hashTable[index]) == 1:
        return hashTable[index][0]

    return []


def htPrint(hashTable, length):
    for i in range(length):
        if len(hashTable[i]) == 0:
            continue
        else:
            print("[", end='')
            for j in range(len(hashTable[i]) - 1):
                print(f"{hashTable[i][j]} ->", end='')
            print(hashTable[i][len(hashTable[i]) - 1], end='')
            print("]")


def usage():
    print(f"python {sys.argv[0]} <fileName1> <fileName2>")
    print(f"Example:")
    print(f"python {sys.argv[0]} file1.txt file2.txt")


def main():
    filesName = sys.argv[:3]
    M = int((10 / 3) * fileLen(filesName[1]))
    X = createTAD(M)
    lines = fileReader(filesName[1])

    for line in lines:
        htInsert(X, line.strip(), M)

    lines2 = fileReader(filesName[2])
    for line2 in lines2:
        htElement = htSearch(X, line2.strip(), M)
        if len(htElement) != 0:
            print(htElement)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
        exit(1)
    elif len(sys.argv) > 3:
        print("[!] Too Many Argument")
        exit(1)
    elif len(sys.argv) == 3:
        main()
    else:
        usage()
        exit(1)
