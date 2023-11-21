'''
Problem
You are given an array A consisting of N integers. 

Task

Print the sum of the elements in the array. 

Note: Some of the integers may be quite large.

Input Format

The first line contains a single integer N denoting the size of the array.  
The next line contains space-separated integers denoting the elements of the array.
Output format

Print a single value representing the sum of the elements in the array.


Constraints:

1<=N<=10

0<=a[i]<=10^10
'''



n = int(input())  # Read the size of the array
array_elements = input().split()  # Read the space-separated integers into an array

result = sum(int(x) for x in array_elements)  # Sum the integers

print(result)  # Print the result