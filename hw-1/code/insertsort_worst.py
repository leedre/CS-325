'''
Jon-Eric Cook
CS-325
Homework #1
This program compares the experimental running times of the insert sort
algorithm for the best and worst array inputs.
'''
import timeit

# wrapper function
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# insert sort algorithm
def insertsort(a):
    # look through each element of the array
    for j in range(1,len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

# arrays to hold times from insert sort function
insertsort_data_best = []
insertsort_data_worst = []

# number of elements to be in random array
elements = 0

# loop 7 times, timing the run time of each sort algorithm for 7 different
# array sizes
for x in range(7):
    # number of elements in array
    elements += 2000
    # generate best and worst arrays to be sorted for insertsort
    best_list = range(elements)
    worst_list = list(reversed(best_list))

    # wrap mergesort function
    wrapped = wrapper(insertsort, best_list)
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for insertsort - best array
    n = "n = "
    n += str(elements)
    insertsort_data_best.append(n)
    sec = "sec = "
    sec += str(time_taken)
    insertsort_data_best.append(sec)

    # wrap insertsort function
    wrapped = wrapper(insertsort, worst_list)
    # time insertsort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for insertsort - worst array
    n = "n = "
    n += str(elements)
    insertsort_data_worst.append(n)
    sec = "sec = "
    sec += str(time_taken)
    insertsort_data_worst.append(sec)

print "Insert Sort - best"
print insertsort_data_best

print "Insert Sort - worst"
print insertsort_data_worst


# RESOURCES:
# The below link was used to help me complete this problem.
# http://pythoncentral.io/time-a-python-function/
