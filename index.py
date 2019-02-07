import sys
from getFile import getFile
from walkArray import WalkArray
from format import formatToLines

def dealArgs(args):
    rtn = {
        'file': '',
        'start': '',
        'stop': '',
        'finish': '',
    }
    for a in args:
        a = a.split('=')
        if a[0] == '-file':
            rtn['file'] = a[1]
        elif a[0] == '-start':
            rtn['start'] = a[1]
        elif a[0] == '-stop':
            rtn['stop'] = a[1]
        elif a[0] == '-finish':
            rtn['finish'] = a[1]
    return rtn


def getAndFilter(args):
    options = dealArgs(args)
    words = getFile(options['file'])
    arr = WalkArray(words, options)
    arr.filter()
    return arr.words


if __name__ == '__main__':
    args = sys.argv
    words = getAndFilter(args)
    if '-f' in args:
        words = formatToLines(words)
    for word in words:
        print(word)

