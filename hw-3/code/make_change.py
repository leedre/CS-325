'''
Jon-Eric Cook
CS-325
Homework #3
This program demonstrates the DP make_change algorithm.
'''

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

# open the input file
input_file = open('amount.txt','r')

# create the output file
output_file = open('change.txt','w')

# convert the string to a array of characters
V = input_file.readline().split(' ')
# get the next line
A = input_file.readline()
while V != [''] and A != ['']:
    # convert to an array of integers
    V = map(int, V)
    # convert the string to an int
    A = int(A)

    # call make_change
    change = make_change(V,A)
    # total number of coins
    total_coins = sum(change)

    # output the results to the output file
    output_file.write(' '.join(map(str,V)))
    output_file.write('\n')
    output_file.write(str(A))
    output_file.write('\n')
    output_file.write(' '.join(map(str,change)))
    output_file.write('\n')
    output_file.write(str(total_coins))
    output_file.write('\n')

    # convert the string to a array of characters
    V = input_file.readline().split(' ')
    # get the next line
    A = input_file.readline()

# close the files
input_file.close()
output_file.close()

# Reference:  The below link was used to help understand and complete part of this assignment.
# https://www.youtube.com/watch?v=NJuKJ8sasGk
