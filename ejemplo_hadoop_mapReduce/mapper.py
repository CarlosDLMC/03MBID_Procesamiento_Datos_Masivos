#!/usr/bin/python

import sys

for linea in sys.stdin:
    linea = linea.strip()
    words = linea.split()
    for word in words:
        print(f"{word}\t1")
