import library
import time, sys

a = int(sys.argv[1]) # Suggested: 10000
def add_matrix(a):
    b = 0
    for i in range(a):
        for j in range (a):
            #b += library.mult(i,j)
            b += i+j
    return b

start_time = time.perf_counter()
print("\n Result direct:",add_matrix(a),"\n")
total_time = time.perf_counter() - start_time
print(" Total time: {0:.1f}s or {1:.1f}m or {2:.1f}h".format(total_time,
        total_time/60, total_time/3600),"\n")

start_time = time.perf_counter()
print("\n Result C library:",library.add_matrix(a),"\n")
total_time = time.perf_counter() - start_time
print(" Total time: {0:.1f}s or {1:.1f}m or {2:.1f}h".format(total_time,
        total_time/60, total_time/3600),"\n")
