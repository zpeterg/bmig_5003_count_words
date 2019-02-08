
def dealArgs(args):
    rtn = {
        # 'file': '',
        'start': '',
        'stop': '',
        'finish': '',
        'format': False,
        'output': '',
        'stats': False,
    }

    for a in args:
        a = a.split('=')
        if a[0] == '--input':
            rtn['file'] = a[1]
        elif a[0] == '--start':
            rtn['start'] = a[1]
        elif a[0] == '--stop':
            rtn['stop'] = a[1]
        elif a[0] == '--finish':
            rtn['finish'] = a[1]
        elif a[0] == '--output':
            rtn['output'] = a[1]

    # throw error if no input file supplied
    if 'file' not in rtn:
        raise ValueError('You must supply a file with --input')

    if '-s' in args:
        rtn['stats'] = True
    elif '-f' in args:
        rtn['format'] = True

    return rtn


def cleanWord(word):
    word = word.lower()
    word = word.replace('\n', '')
    return word.strip("~`!@#$%^&*()_-+={[}]|\\:;\"' <,>.?/")
