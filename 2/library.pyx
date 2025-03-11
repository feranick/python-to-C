# library.pyx
def add(int a, int b) -> long:
    cdef int result
    result = long(a + b)
    return result

def add_matrix(int a) -> long:
    cdef long i, j
    cdef long b
    b = 0
    for i in range(a):
        for j in range(a):
            b += long(i + j)
    return b
