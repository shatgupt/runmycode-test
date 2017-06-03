import sys
print('Hello World from python3!')
print(str(len(sys.argv[1:])) + ' Args: [' + ', '.join(sys.argv[1:]) + ']')
