'''
Jon-Eric Cook
CS-325
Homework #2
This program demonstrates the stooge sort algorithm. It does this by first
checking if the first element is larger that the element at the end. If this is
true then it swaps them. If there are 3 or more elements in the array, it
proceeds to sort the first 2/3s of the array. It then sorts the final 2/3 of
the array. It the goes back and sorts the first first 2/3 of the array again.
This program will be sorting arrays of length n that contain random numbers.
'''
import random
import timeit

# wrapper function
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# stoogeSort algorithm
def stoogeSort(a,low,high):
    # swaps elements
    if a[low] > a[high]:
        temp = a[low]
        a[low] = a[high]
        a[high] = temp

    # if there are more than two elements in the array
    if (high - low + 1) > 2:
        fraction = (int)((high - low + 1.0)/3)
        stoogeSort(a,low,high-fraction)
        stoogeSort(a,low+fraction,high)
        stoogeSort(a,low,high-fraction)

    return a

# arrays to hold times from sort functions
stoogesort_data = []

# number of elements to be in random array
elements = [100,200,300,500,1000,1200,1600]

# loop 7 times, timing the run time of each sort algorithm for 7 different
# array sizes
for x in range(7):
    # randomly generate arrays to be sorted for mergesort and insertsort
    rand_list_stoogesort = [int(1000*random.random()) for i in xrange(elements[x])]

    # wrap mergesort function
    wrapped = wrapper(stoogeSort, rand_list_stoogesort, 0, len(rand_list_stoogesort) - 1)
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for mergesort
    n = "n = "
    n += str(elements[x])
    stoogesort_data.append(n)
    sec = "sec = "
    sec += str(time_taken)
    stoogesort_data.append(sec)

print "Stooge Sort"
print stoogesort_data


# RESOURCES:
# The below links were used to help me complete this problem.
# https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort#Python
# https://en.wikipedia.org/wiki/Stooge_sort
# http://www.geeksforgeeks.org/stooge-sort/
