

>>> x = reduce(operator.or_, [1<<ord(c) for c in 'abcdefg'])
>>> x
20123953278623141748760163385344L
>>> y = reduce(operator.or_, [1<<ord(c) for c in 'abcde'])
>>> y
4912146075884388930799724920832L
>>> (x or y)
20123953278623141748760163385344L
>>> (x and y)
4912146075884388930799724920832L
>>> (x and y)==y
True
