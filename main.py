import ctypes

x = 5647
y = 6151
bits = 61

def dim(p, q):
    global x, y
    x = p
    y = q

def allocate():
    a = (ctypes.POINTER(ctypes.c_ulong) * x)()
    for i in range(x):
        a[i] = (ctypes.c_ulong * y)()
        if a[i] == 0:
            print("unable to allocate")
            return
    for i in range(x):
        for j in range(y):
            a[i][j] = 0
    print("\nAllocated and Initialized 2DBF Successfully...\n")
    return a

def _set_(a, h):
    i = h % x
    j = h % y
    pos = h % bits
    a[i][j] |= (1 << pos)

def _test_(a, h):
    i = h % x
    j = h % y
    pos = h % bits
    return (a[i][j] >> pos) & 1

def _del_(a, h):
    i = h % x
    j = h % y
    pos = h % bits
    p = 1 << pos
    if p == (a[i][j] & (1 << pos)):
        a[i][j] ^= p

def _free_(a):
    print("\nMemory freed successfully...\n")

dim(10, 10)
array = allocate()
_set_(array, 5)
print(_test_(array, 5))
_del_(array, 5)
print(_test_(array, 5))
_free_(array)
def allocate():
    a = (ctypes.POINTER(ctypes.c_ulong) * x)()
    for i in range(x):
        a[i] = (ctypes.c_ulong * y)()
        for j in range(y):
            a[i][j] = 0
    print("\nAllocated and Initialized 2DBF Successfully...\n")
    return a
