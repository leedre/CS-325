'''
Jon-Eric Cook
CS-325
Homework #1
This program demonstrates the insert sort algorithm. It does this by opening
a file named data.txt, reading in data, sorting said data via the insert sort
algorithm and then outputing the results to a file named insert.out.
'''

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

# open the input file
input_file = open('data.txt','r')

# create the output file
output_file = open('insert.out','w')

# convert the string to a array of characters
line = input_file.readline().split(' ')
while line != ['']:
    # convert to an array of integers
    line = map(int, line)

    # discard the first number
    line = line[1:]

    # call insertsort
    s = insertsort(line)

    # output the sorted array to the output file
    output_file.write(' '.join(map(str,s)))
    output_file.write('\n')

    # get another line
    line = input_file.readline().split(' ')

# close the files
input_file.close()
output_file.close()

# RESOURCES
# The code from page 18 from Introduction to Algorithms, INSERTION-SORT (A)
# helped me solve this problem.
