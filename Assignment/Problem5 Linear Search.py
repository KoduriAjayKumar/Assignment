#Program to implement linear search 
def linear_search(list, n):
    for i in range(len(list)):
         if list[i] == n:
            return i
    return False
#Taking a list1 and searching for element 'e'
list1 = [9,6,4,5,3,4,2,0]
element = 2
print('The element 2 is at index',linear_search(list1,element))