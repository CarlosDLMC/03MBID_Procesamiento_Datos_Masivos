#!/usr/bin/python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_word, current_count = word, count
print('%s\t%s' % (current_word, current_count))
# print(f"{current_word}\t{current_count}")