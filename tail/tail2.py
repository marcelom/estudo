# Tail, um pouco melhor, linha por linha...

import sys

numlines = int(sys.argv[1])
stack = []
i = 1

for line in sys.stdin:
   stack.append(line)
   if i>numlines:
       stack.pop(0)
   i += 1

print "".join(stack)
