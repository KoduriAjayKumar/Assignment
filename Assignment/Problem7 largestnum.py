#To find the largest number in a list without using built-in functions.
list = [int(i) for i in input('enter the numbers in list separating with space').split() ]
list.sort()
largest = list[-1]
print('The largest number is :',largest)