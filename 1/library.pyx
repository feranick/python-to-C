# library.pyx
def mult(float a, float b) -> float:
    cdef float result
    result = a * b
    return result
