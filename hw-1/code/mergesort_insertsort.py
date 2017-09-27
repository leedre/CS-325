'''
Jon-Eric Cook
CS-325
Homework #1
This program compares the experimental running times of both the merger sort
algorithm and insert sort algorithm. This is done timing how long each algorithm
takes to sort a randomly generated array of length n.
'''
import random
import timeit

# wrapper function
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# merge algorithm
def merge(l,r):
    # empty array to be used to hold sorted values
    s = []
    # append to s array until either l or r array is empty
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            s.append(l[0])
            l.remove(l[0])
        else:
            s.append(r[0])
            r.remove(r[0])
    # add the remaining value to the s array
    if len(l) == 0:
        s += r
    else:
        s += l
    return s

# mergesort algorithm
def mergesort(a):
    # if the array has only one element, return it
    if len(a) == 1:
        return a
    else:
        # call mergesort on half of the current input array
        mid = len(a)/2
        l = mergesort(a[:mid])
        r = mergesort(a[mid:])
        return merge(l,r)

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

# arrays to hold times from sort functions
mergesort_data = []
insertsort_data = []

# number of elements to be in random array
elements = 0

# loop 7 times, timing the run time of each sort algorithm for 7 different
# array sizes
for x in range(7):
    # number of elements in array
    elements += 2000

    # randomly generate arrays to be sorted for mergesort and insertsort
    rand_list_mergesort = [int(1000*random.random()) for i in xrange(elements)]
    rand_list_insertsort = rand_list_mergesort

    # wrap mergesort function
    wrapped = wrapper(mergesort, rand_list_mergesort)
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for mergesort
    n = "n = "
    n += str(elements)
    mergesort_data.append(n)
    sec = "sec = "
    sec += str(time_taken)
    mergesort_data.append(sec)

    # wrap insertsort function
    wrapped = wrapper(insertsort, rand_list_insertsort)
    # time insertsort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for insertsort
    n = "n = "
    n += str(elements)
    insertsort_data.append(n)
    sec = "sec = "
    sec += str(time_taken)
    insertsort_data.append(sec)

print "Merge Sort"
print mergesort_data

print "Insert Sort"
print insertsort_data


# RESOURCES:
# The below link was used to help me complete this problem.
# http://pythoncentral.io/time-a-python-function/
