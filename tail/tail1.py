# Tail, quick and dirty

import sys

lines = sys.stdin.readlines()

numlines = int(sys.argv[1])

print ''.join(lines[-numlines:])
