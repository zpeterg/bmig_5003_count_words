
def cleanWords(arr):
    rtn = []
    for item in arr:
        new_item = item.strip("~`!@#$%^&*()_-+={[}]|\\:;\"' <,>.?/")
        if new_item != '':
            rtn.append(new_item)
    return rtn
