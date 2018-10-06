"""
  This program won't run properly without an input.
  Try with: abc
"""
import sys
print('Hello World from Python 3!')
for line in sys.stdin:
    print(line.rstrip())
