#To find the average of 10 numbers using while loop.
i = 0
sum = 0
count = 0
while i<10:
    num = int(input('please enter the number '))
    sum = sum + num
    i = i + 1
    count = count + 1
print(sum/count)    