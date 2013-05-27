# given this array of 1000 integers, find and remove the duplicates.

a = [ 7, 11, 21, 27, 91, 87, 29, 49, 66, 35, 34, 79, 69, 39, 18, 65, 27, 60, 66, 68, 23, 79, 15, 96,
      25, 63, 63, 53, 32, 88, 32, 78, 41, 71, 10, 75, 40, 32, 97, 50, 97, 79, 54, 89, 21, 30, 77, 39,
      81, 58, 93, 30, 72, 22, 34, 52, 50, 20, 85, 77, 27, 16, 20, 44, 52, 20, 49, 65, 24, 43, 33, 95,
      29, 40, 97, 46, 55, 56, 68, 89, 91, 47, 7, 16, 20, 87, 56, 58, 73, 29, 92, 9, 87, 57, 59, 77,
      17, 3, 44, 67, 31, 93, 27, 50, 66, 79, 53, 76, 76, 24, 1, 78, 18, 53, 100, 74, 22, 53, 50, 51,
      47, 89, 82, 7, 32, 64, 38, 59, 83, 27, 41, 92, 13, 36, 59, 62, 11, 45, 53, 67, 48, 7, 35, 5, 81,
      32, 13, 35, 98, 69, 75, 57, 55, 20, 91, 65, 38, 17, 48, 69, 95, 83, 4, 77, 70, 14, 33, 9, 60, 48,
      10, 57, 6, 75, 70, 17, 76, 75, 91, 98, 3, 13, 4, 16, 88, 24, 54, 60, 19, 62, 58, 58, 22, 95, 26,
      74, 78, 50, 32, 49, 43, 3, 98, 25, 46, 71, 4, 33, 83, 14, 40, 76, 65, 72, 57, 59, 93, 33, 56, 6,
      98, 61, 1, 97, 31, 14, 14, 57, 41, 53, 74, 23, 68, 2, 66, 6, 42, 5, 88, 40, 78, 49, 81, 73, 73,
      45, 68, 93, 78, 63, 32, 54, 42, 24, 14, 92, 37, 81, 42, 52, 20, 73, 56, 52, 21, 90, 54, 100, 34,
      68, 79, 9, 98, 9, 9, 11, 86, 55, 2, 40, 26, 26, 83, 64, 9, 38, 1, 99, 84, 39, 12, 20, 9, 11, 3,
      86, 13, 48, 10, 64, 88, 33, 100, 62, 12, 36, 97, 31, 33, 17, 64, 74, 6, 57, 15, 81, 9, 93, 10,
      84, 9, 76, 67, 46, 51, 30, 85, 63, 18, 81, 29, 66, 48, 2, 39, 77, 79, 31, 18, 53, 11, 95, 40,
      83, 87, 39, 90, 59, 51, 52, 98, 75, 68, 16, 19, 5, 82, 91, 31, 5, 59, 23, 29, 2, 3, 92, 97, 66,
      99, 8, 39, 75, 6, 63, 52, 67, 28, 94, 84, 5, 44, 30, 69, 22, 13, 61, 34, 18, 52, 20, 27, 11, 52,
      99, 47, 43, 73, 50, 90, 59, 2, 75, 31, 50, 79, 69, 87, 3, 94, 4, 28, 17, 67, 9, 71, 79, 26, 53,
      44, 81, 58, 50, 99, 80, 24, 46, 49, 85, 43, 41, 36, 85, 66, 23, 27, 39, 19, 67, 33, 14, 25, 6,
      62, 49, 100, 54, 74, 33, 61, 17, 2, 1, 93, 6, 86, 42, 41, 8, 1, 18, 27, 60, 100, 39, 93, 59, 52,
      83, 17, 75, 21, 19, 56, 47, 43, 89, 93, 95, 56, 45, 78, 41, 50, 46, 8, 62, 94, 42, 72, 32, 90,
      40, 3, 60, 1, 16, 26, 50, 43, 2, 96, 90, 95, 36, 72, 98, 47, 91, 4, 97, 70, 24, 43, 34, 65, 14,
      81, 97, 49, 7, 71, 94, 41, 78, 88, 1, 73, 13, 86, 25, 75, 93, 79, 37, 14, 92, 96, 22, 2, 56, 62,
      39, 43, 41, 35, 18, 78, 18, 6, 52, 6, 61, 75, 16, 7, 75, 20, 99, 16, 90, 47, 28, 99, 93, 88, 66,
      14, 40, 21, 86, 30, 77, 72, 53, 37, 15, 1, 13, 78, 11, 24, 47, 40, 10, 85, 42, 7, 91, 49, 21, 39,
      68, 50, 39, 75, 12, 92, 41, 76, 62, 40, 68, 56, 5, 92, 91, 100, 45, 40, 86, 85, 71, 73, 92, 64,
      10, 52, 51, 88, 46, 55, 37, 52, 38, 22, 4, 9, 93, 26, 37, 27, 42, 85, 68, 22, 28, 50, 59, 57, 90,
      8, 46, 84, 18, 57, 89, 36, 30, 29, 69, 20, 98, 19, 79, 9, 34, 89, 32, 32, 81, 90, 81, 8, 66, 59,
      56, 79, 58, 12, 60, 73, 66, 11, 50, 39, 3, 14, 21, 75, 97, 51, 88, 38, 33, 45, 91, 66, 6, 15, 94,
      87, 57, 9, 45, 43, 89, 83, 46, 94, 3, 41, 46, 78, 27, 83, 73, 41, 20, 64, 60, 39, 51, 10, 67, 56,
      71, 66, 59, 20, 47, 86, 29, 57, 88, 88, 8, 69, 99, 9, 22, 7, 82, 46, 41, 5, 53, 71, 27, 87, 7, 5,
      20, 23, 46, 16, 4, 91, 64, 53, 17, 51, 73, 30, 80, 51, 53, 99, 46, 90, 49, 97, 56, 38, 33, 48, 17,
      70, 47, 29, 10, 38, 26, 95, 53, 14, 23, 48, 76, 34, 16, 27, 89, 28, 88, 82, 3, 5, 23, 20, 1, 54,
      28, 60, 39, 5, 42, 59, 36, 53, 60, 21, 50, 96, 70, 94, 91, 52, 72, 62, 79, 99, 82, 37, 15, 34, 9,
      52, 82, 92, 8, 42, 48, 9, 97, 54, 28, 91, 92, 49, 21, 33, 26, 45, 30, 46, 67, 80, 74, 21, 62, 10,
      83, 43, 35, 48, 2, 64, 27, 84, 34, 26, 45, 18, 7, 50, 42, 80, 99, 8, 99, 59, 74, 69, 7, 93, 94,
      93, 25, 71, 58, 54, 9, 31, 36, 64, 87, 93, 24, 58, 21, 5, 89, 76, 34, 29, 16, 32, 33, 94, 55, 5,
      94, 60, 43, 74, 48, 12, 45, 57, 65, 71, 44, 42, 51, 10, 96, 57, 29, 61, 52, 77, 87, 55, 92, 28, 86,
      8, 22, 36, 23, 60, 19, 94, 16, 8, 96, 74, 36, 76, 25, 73, 2, 75, 67, 63, 62, 33, 92, 52, 97, 14,
      97, 92, 47, 83, 78, 44, 86, 16, 4, 14, 88, 69, 75, 97, 48, 20, 64, 70, 84, 49, 19, 83, 81, 73, 96,
      61, 99, 77, 51, 85, 2, 44, 22, 43, 7, 72, 82, 48, 29, 68, 65, 63, 44, 13, 87, 95, 28, 84, 36, 78,
      44, 97, 34, 86, 7, 3, 26, 32, 6 ]

def method1(a):
    # this method modifies (sort) the array
    # complexity is about n.logn, because of the sorting
    a.sort()
    old = None
    
    for n in a:
        if old == n:
            continue
        old = n
        print n, ', ',

def method2(a):
    # this method needs about 2n of memory...
    b = []
    for n in a:
        if n not in b:
            b.append(n)
    print b

def method3(a):
    # similar to 2, but uses a python set
    # it alsos modifies the order, because the set is always unordered.
    b = set(a)
    print list(b)

method2(a)
method3(a)
method1(a)
