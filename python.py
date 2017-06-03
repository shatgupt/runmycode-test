import sys
print 'Hello World from python!'
print str(len(sys.argv[1:])) + ' Args: [' + ', '.join(sys.argv[1:]) + ']'
