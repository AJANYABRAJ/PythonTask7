# 1. Sort even-placed elements in increasing and odd-placed in decreasing order

input = [5,8,6,2,9,11,28,34,16]
print("Input: "+str(input))
evenPlacedElements = []
oddPlacedElements = []
output = []
for x,value in zip(range(len(input)),input):
    if x == 0 or x % 2 == 0:
        evenPlacedElements.append(value)
    else:
        oddPlacedElements.append(value)
print("Even Placed Elements in Increasing Order: "+ str(sorted(evenPlacedElements)))
print("Odd Placed Elements in Decreasing Order: "+str(sorted(oddPlacedElements,reverse=True)))

#############################################################################

# 2. Reverse a string without affecting special characters

#def reverseString(text):
#    index = -1
#    for i in range(len(text) - 1, int(len(text) / 2), -1):
#        if text[i].isalpha():
#            temp = text[i]
#            while True:
#                index += 1
#                if text[index].isalpha():
#                    text[i] = text[index]
#                    text[index] = temp
#                    break
#    return text

#string = "a!!!j.a.n,y'fa,xyz"
#print("Input string: ", string)
#string = reverseString(list(string))
#print("Output string: ", "".join(string))

#############################################################################

# 3. Find Second Largest Number in Array

#list1 = [10, 20, 20, 4, 57, 55, 45, 99, 99]
#list2 = list(set(list1))
#list2.sort()
#print("Second largest element is:", list2[-2])

#############################################################################
# 4. Program to copy all elements of one array into another array

#from numpy import *
#arr1 = array([2, 6, 9, 4])
#arr2 = arr1.copy()
#print("Array1=",(arr1))
#print("Array2=",(arr2))

#############################################################################

# 5. Program to print the duplicate elements of an array

#arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];
#print("Duplicate elements in given array: ");
#for i in range(0, len(arr)):
#    for j in range(i + 1, len(arr)):
#        if (arr[i] == arr[j]):
#            print(arr[j]);

#############################################################################

# 6. Reverse a String  Word by Word

#string = "hello friends good morning"
#s = string.split()[::-1]
#l = []
#for i in s:
#    l.append(i)
#print(" ".join(l))