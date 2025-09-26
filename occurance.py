#!/usr/bin/python3.11
import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python script.py <input_string>")
    sys.exit(1)

input_string = sys.argv[1]
char_counts = Counter(input_string)

for char, count in char_counts.items():
    print(f"{char}: {count}")
