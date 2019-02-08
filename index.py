import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile
from getStats import getStats


def getAndFilter(options):
    f = Filter(options)
    these_words = getFile(options['file'], f.filter)
    return these_words


if __name__ == '__main__':
    args = sys.argv
    options = dealArgs(args)
    words = getAndFilter(options)
    stats = None

    # if stats being requested
    if options['stats']:
        stats = getStats(words)
    # format (incompatible with stats)
    elif options['format']:
        words = formatToLines(words)

    forPrint = '\n'

    # if outputting, just print JSON for one
    if options['output']:
        if stats:
            forPrint = json.dumps(stats, indent=4)
        else:
            forPrint = json.dumps(words, indent=4)
        writeFile(forPrint, options['output'])
        print(f"\nThe requested data has been written to file {options['output']}.")
    # if printing to screen
    else:
        if stats:
            if len(stats) <= 1:
                forPrint += 'No stats to print.'
            else:
                forPrint += 'STATS:\n'
                for stat in stats:
                    forPrint += f'\n{stat}: {stats[stat]}'
        else:
            if len(words) <= 1:
                forPrint += 'No words to print.'
            else:
                forPrint += 'WORDS:\n'
                for word in words:
                    forPrint += f'\n{word}'
        print(forPrint)
