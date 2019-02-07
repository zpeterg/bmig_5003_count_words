
class WalkArray:
    def __init__(self, words, options):
        self.words = words
        self.start = options['start']
        self.stop = options['stop']
        self.finish = options['finish']

    def filter(self):
        rtn = []
        recording = False
        for word in self.words:
            if word == self.start:
                recording = True
            elif word == self.stop:
                recording = False
            elif word == self.finish:
                break
            elif recording:
                rtn.append(word)
        self.words = rtn

