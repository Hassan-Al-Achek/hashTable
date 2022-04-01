def fileReader(fileName):
    with open(fileName) as fileObject:
        lines = fileObject.readlines()
    return lines


def fileLen(fileName):
    lines = fileReader(fileName)
    return len(lines)
