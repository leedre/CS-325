'''
Jon-Eric Cook
CS-325
Homework #2
This program demonstrates the stooge sort algorithm. It does this by first
checking if the first element is larger that the element at the end. If this is
true then it swaps them. If there are 3 or more elements in the array, it
proceeds to sort the first 2/3s of the array. It then sorts the final 2/3 of
the array. It the goes back and sorts the first first 2/3 of the array again.
This program will be reading in the data to be sorted from a file names data.txt.
'''

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

# open the input file
input_file = open('data.txt','r')

# create the output file
output_file = open('stooge.out','w')

# convert the string to a array of characters
line = input_file.readline().split(' ')
while line != ['']:
    # convert to an array of integers
    line = map(int, line)

    # discard the first number
    line = line[1:]

    # call stoogeSort
    s = stoogeSort(line,0,len(line)-1)

    # output the sorted array to the output file
    output_file.write(' '.join(map(str,s)))
    output_file.write('\n')

    # get another line
    line = input_file.readline().split(' ')

# close the files
input_file.close()
output_file.close()
