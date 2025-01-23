
#1 Import numpy as np and see the version
#Q. Import numpy as np and print the version number.
import numpy as np
print(np.__version__)

#2 How to create a 1D array?
#Q. Create a 1D array of numbers from 0 to 9

a = np.arange(0,10)
print(a)


#3 How to create a boolean array?
#Q. Create a 3×3 numpy array of all True’s

b=np.arange(1,10).reshape(3,3)
print(b)
print(b<10)


#4 How to extract items that satisfy a given condition from 1D array?
#Q. Extract all odd numbers from arr

arr =np.array([0,1,2,3,4,5,6,7,8,9])

arr_odd =arr %2!=0
print(arr[arr_odd])


#5 How to replace items that satisfy a condition with another value in numpy array?
#Q. Replace all odd numbers in arr with -1

arr =np.array([0,1,2,3,4,5,6,7,8,9])
arr_odd =arr %2!=0
arr[arr_odd] =-1
print(arr)

#6 How to replace items that satisfy a condition without affecting the original array?
#Q. Replace all odd numbers in arr with -1 without changing arr

arr =np.array([0,1,2,3,4,5,6,7,8,9])
arr2 =arr.copy()
arr_odd =arr2 %2!=0
arr2[arr_odd] =-1
print(arr)
print(arr2)

#7 How to reshape an array?
#Q. Convert a 1D array to a 2D array with 2 rows

a=np.arange(10)
print(a)
a=a.reshape(2,5)
print(a)

#8 How to stack two arrays vertically?
#Q. Stack arrays a and b vertically

a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
print(a)
print(b)
c = np.concatenate((a,b),axis=0)
print(c)

#9 How to stack two arrays horizontally?
#Q. Stack the arrays a and b horizontally.

a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
print(a)
print(b)
c = np.concatenate((a,b),axis=1)
print(c)

#10 How to generate custom sequences in numpy without hardcoding?
#Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

a = np.array([1,2,3])
print(a)
b= np.r_[np.repeat(a,3), np.tile(a,3)]

print(b)

#11 How to get the common items between two python numpy arrays?
#Q. Get the common items between a and b


a= np.array([1,2,3,2,3,4,3,4,5,6])
b= np.array([7,2,10,2,7,4,9,4,9,8])

print(np.sort(a))
print(np.sort(b))

common = np.intersect1d(a,b)
print(common)


#12 How to remove from one array those items that exist in another? 
#Q. From array a remove all items present in array b

