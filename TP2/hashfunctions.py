import numpy as np


# Why this hash function is useless
# because simply: we can have multiple
# strings where the sum of the ascii value
# result on the same value like "ha" and "ah" strings
# So we have a hard chance to meet collision
def hassan_alachek_simpleModuloHash(string, length):
    hashValue = 0
    if len(string) == 0:
        return 0
    for character in string:
        hashValue += ord(character)

    return hashValue % length


def hassan_alachek_efficientHash(string, length):
    hashValue = 5381
    for character in string:
        hashValue = ((hashValue << 5) + hashValue) + ord(character)
    return hashValue % length


def hassan_alachek_sdbm(string, length):
    hashValue = 0
    for character in string:
        hashValue = ord(character) + (hashValue << 6) + (hashValue << 16) - hashValue
    return hashValue % length


def hassan_alachek_cyclicShift(string, length):
    hashValue = 0

    for character in string:
        hashValue = np.uintc(np.uintc(hashValue << 5) | np.uintc(hashValue >> 27))
        hashValue += np.uintc(ord(character))
    return hashValue % length
