'''def pair(arrray,target):
   left,right = 0,len(a)-1
   while left < right:
     cursum = array[left] + array[right]
     if cursum == target:
       return 'true'
     elif cursum > target:
       right-=1
     else:
       left+=1
   return 'false'

a=int(input())
array = list(map(int,input().split()))
target = int(input("Enter target sum : "))
print(pair(array,target))'''


'''def check(s):
    new = ''
    for i in s:
        if i.isalnum():
            new += i.lower()
    left,right = 0, len(new)-1
    while left<right:
        if new[left]!=new[right]:
            return 'false'
        left+=1
        right-=1
    return 'true'

s = input("Enter a string: ")
print(check(s))'''


'''def merge(arr1,arr2):
    new=[]
    l1,l2=len(arr1),len(arr2)
    i,j=0,0
    while 1<11 and j<12:
        if arr1[i]<arr2[j]:
            new.append(arr1[i])
            i+=1
        else:
            new.append(arr2[j])
            j+=1
    while i<11:
        new.append(arr1[i])
        i+=1
    while j<12:
        new.append(arr2[j])
        j+=1
    return new
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(merge(a,b))'''


'''def quicksort(array):
    if len(array):
        return array
    pivot = array[len(array)//2]
    left = [i for i in array if i<pivot]
    middle = [i for i in array if i<pivot]
    right = [i for i in array if i<pivot]
    return quicksort(left)+middle+quicksort(right)
a=list(map(int,input().split()))
print(quicksort(a))'''


'''def rearrange_string(word, ch):
    index = word.find(ch)
    if index == -1:
        return word 

    before_ch = word[:index][::-1]
    after_ch = word[index + len(ch):]

    return ch + before_ch + after_ch

word = input("Word: ")
ch = input("Ch: ")
output = rearrange_string(word, ch)
print(output)'''


'''def find(s):
    left,right=0,len(s)-1
    while(left+right):
        if s[left].isalpha() and s[right].isalpha():
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        elif s[left].isalpha():
            right-=1
        elif s[right].isalpha():
            left+=1
    return ''.jon(s)
s=input()
print(find([*s]))'''


























