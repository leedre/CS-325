'''
Jon-Eric Cook
CS-325
Homework #3
This program demonstrates the DP make_change algorithm.
'''
import timeit

# wrapper function
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# make change DP algorithm
def make_change(V,A):
    # array to hold how many coins were needed per element
    T = [float('Inf')]*(A+1)
    # with a value of 0, 0 coins are needed
    T[0] = 0
    # array to hold the last coin used on the corresponding T element
    R = [-1]*(A+1)
    # array to hold total amount of each coin used
    C = [0]*len(V)

    # steps through the array of coins and makes change if possible
    for j in range(len(V)):
        for i in range(1,A+1):
            # if the number for change to be made for is greater than the
            # selected coin value
            if i >= V[j]:
                # if the newly selected coin value plus 1 is less than the
                # current coin value
                if (T[i-V[j]] + 1) < T[i]:
                    T[i] = 1 + T[i-V[j]]
                    R[i] = j

    # count how many coins were used per element
    while A != 0:
        C[R[A]] += 1
        A = A - V[R[A]]

    return C

V_array1_data = []

V_array1 = [range(1,1000,2),range(1,10000,2),range(1,100000,2),range(1,1000000,2),
           range(1,1200000,2),range(1,1400000,2),range(1,1600000,2)]
A_array1 = [100]

V_array2 = range(1,100,2)
A_array2 = [1000,10000,100000,1000000,1200000,1400000,1600000]

V_array3 = [range(1,1000,2),range(1,2000,2),range(1,4000,2),range(1,8000,2),
           range(1,16000,2),range(1,32000,2),range(1,64000,2)]
A_array3 = [1000,2000,4000,8000,16000,32000,64000]

# for x in range(7):
#     # wrap mergesort function
#     wrapped = wrapper(make_change, V_array1[x], A_array1[0])
#     # time mergesort function
#     time_taken = timeit.timeit(wrapped, number=1)
#
#     # log number of elements and time taken
#     sec = "sec = "
#     sec += str(time_taken)
#     V_array1_data.append(sec)

# for x in range(7):
#     # wrap mergesort function
#     wrapped = wrapper(make_change, V_array2, A_array[x])
#     # time mergesort function
#     time_taken = timeit.timeit(wrapped, number=1)
#
#     # log number of elements and time taken
#     sec = "sec = "
#     sec += str(time_taken)
#     V_array1_data.append(sec)

for x in range(7):
    # wrap mergesort function
    wrapped = wrapper(make_change, V_array3[x], A_array3[x])
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken
    sec = "sec = "
    sec += str(time_taken)
    V_array1_data.append(sec)

print "V_array1_data"
print V_array1_data
