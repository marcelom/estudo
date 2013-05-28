"""
Find duplicate UIDs...

Suppose you have a file like this:

foo:123:345:...
bar:456:234:...
baz:123:444:...

I want a prorgam that does this output:

Duplicate UID 123: foo, baz
"""

import sys

def method1():
    d = {}
    for line in sys.stdin:
        a = line.split(':')
        if a[1] in d:
            d[a[1]].append(a[0])
        else:
            d[a[1]] = [a[0]]
    for uid, names in d.iteritems():
        if len(names) > 1:
            print 'Duplicate UID %s: %s' % (uid, ', '.join(names))

def method2():
    # same as 1, but uses exceptions
    d = {}
    for line in sys.stdin:
        a = line.split(':')
        try:
            d[a[1]].append(a[0])
        except KeyError:
            d[a[1]] = [a[0]]
    for uid, names in d.iteritems():
        if len(names) > 1:
            print 'Duplicate UID %s: %s' % (uid, ', '.join(names))

method2()
