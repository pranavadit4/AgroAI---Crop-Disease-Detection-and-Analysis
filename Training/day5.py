#function calling itself is called recursion
#a recursion method calling solves a problem by calling a copy of itself to work on a smaller problem
#recursion is a problem where a function callsitself to find the result.The base condition acts as the breakpoint to the self calling process


#types:
    #Direct Recursion
    #inDirect Recursion
#direct: function calling itself
#indirect: function calling another function

#my code
'''def add(a,b):
    if b == 0:
        return a
    return add(a + 1,b - 1)
    
num1=10
num2=2
result = add(num1,num2)
print("Sum : ",result)'''

#board
'''def add(a,b):
    if b == 0:
        return a
    elif b>0:
        return add(a+1,b-1)
    else:
        return add(a-1,b+1)
print(add(10,-20))'''

#fibonacci series
'''def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
n = 8
for i in range(0,n):
    print(fib(i))'''
    
#binary search using recursion
'''def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid=(left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,mid + 1,right,target)
    else:
        return binary_search(arr,left,mid - 1,target)
arr = [1,3,5,7,9,11,13,15,17,19,21]
target = 19
print(binary_search(arr, 0, len(arr) - 1, target))'''




