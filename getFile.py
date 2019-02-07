
def getFile(filename):
    rtn = []
    with open(filename, 'r') as file:
        # append each line with a space
        for line in file:
            for word in line.split(' '):
                rtn.append(word)
    return rtn
