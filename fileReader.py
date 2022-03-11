def fileReader(fileName):
    with open(fileName) as fileObject:
        lines = fileObject.readlines()
    return lines
