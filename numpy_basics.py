import numpy as np

#21-01-25
# reference - https://numpy.org/doc/stable/user/absolute_beginners.html

#1 Array fundamentals
''''                                       #note - use given command in terminal to activate virtual environment - source myenv/bin/activate
a = ([1,2,3])                               then use command to open jupyter- jupyter notebook 
print(a)                                    after usage to deactivate the virtual environment use - deactivate
print(a.all())
print(a.argmax())
print(a.argmin())
print(a.argpartition(1))
print(a.argsort())
print(a.byteswap())
print(a.clip(max=2))
'''

#2 Array attributes
'''
arr = ([1,2,3],
       [4,5,6],
       [7,8,9])

a = np.array(arr)
print(a.dtype) # 
print(a.ndim)
print(a.shape)
print(a.size)
'''

#3 How to create a basic array
'''
my1 = np.zeros(2)
print(my1)

my2 = np.ones(2)
print(my2)

my3 = np.empty(2)
print(my3)

my4 = np.arange(5)
print(my4)

my5 = np.arange(2,10,1)
print(my5)

my6 = np.linspace(2,100,15)
print(my6)
'''


#4 Adding, removing, and sorting elements
'''
arr = np.array([15,2,6,7,9,64,1,3])
print(np.sort(arr))
print(np.argsort(arr))
print(arr.searchsorted(9))
print(np.partition(arr,2))


a= np.array([1,2,3])
b=np.array([4,5,6])
b2 =np.array([7,8,9])

c = np.lexsort((a,b))
d = np.lexsort((b,a))
print(c)
print(d)

e = np.concatenate((a,b))
print(e)

f= np.concatenate((e,b2), axis=0)
print(f)

'''

#5 How do you know the shape and size of an array?
'''
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]]) 

print(array_example.ndim)    #will tell you the number of axes, or dimensions, of the array.
print(array_example.shape)   #will tell you the total number of elements of the array
print(array_example.size)    #If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3)
'''

#6 Can you reshape an array?
'''
a= np.array([[1,2],
            [3,4],
            [5,6]])

print(a)
print(a.shape)

b = a.reshape(2,3)     #keep in mind if you want to reshape as per the columns, need to research
print(b)
print(b.shape)
'''

#7 How to convert a 1D array into a 2D array (how to add a new axis to an array)
'''
a= np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

print(a)
print(a.shape)

a2 = a[np.newaxis,:]    #inserting an axis along the first dimension
print(a2)
print(a2.shape)

a2 =a[:,np.newaxis]     #inserting an axis along the second dimension
print(a2)
print(a2.shape)

b = np.array([1,2,3])
print(b)
print(b.shape)

c = np.expand_dims(b, axis=0)       #add an axis at index position 0 or 1 with respect to axis= 0 or 1
print(c)
'''

#22-01-25 
#8 Indexing and slicing     (https://numpy.org/doc/stable/user/absolute_beginners.html#indexing-and-slicing)
'''
a = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])

print(a[0])
print(a[a<8])
print(a[a>=5])
print(a[a%2==0])
print(a[(a>2) & (a<8)])
five_up = (a>12) | (a==12)
print(five_up)

non_zero = np.nonzero(a<5)
print(non_zero)
b = a[non_zero]
print(b)
'''

#9 How to create an array from existing data

'''
a1 =np.array([[1,1],[2,2]])

a2 =np.array([[3,3],[4,4]])

#print(np.concatenate(a1,a2))  #works only on 0-dimensional array
print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))

x= np.arange(1,25).reshape(2,12)
print(x)

print(np.hsplit(x,4))
print(np.vsplit(x,2))

y =np.arange(1,101)
print(y)
print(y.reshape(5,20))
print(y.reshape(10,10))
print(np.hsplit(y,(2,4,6,8)))

z= y.copy()                 #make a complete copy of the array and its data (a deep copy)
z1 = y.view()               #create a new array object that looks at the same data as the original array (a shallow copy).
'''

#10 Basic array operations
'''
a= np.array([1,2])
b = np.ones(2, dtype=int)

c= a+b
print(c)

d= a-b
print(d)

e = a*b
print(e)

f= b/a
print(f)
'''
'''
a= np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c= a+b
print(c)

d= a-b
print(d)

e = a*b
print(e)

f= b/a
print(f)
'''


#11 Broadcasting
'''
NumPy understands that the multiplication should happen with each cell. 
That concept is called broadcasting. Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes.

a= np.array([1.0,2.0])
b= a*1.6
print(b)
'''

#12 More useful array operations
'''
a= np.array([[1,2,3],
              [4,5,6]])
print(a.max())
print(a.min(axis=1))
print(a.min())
print(a.mean())
print(a.sum())
'''

#13 Creating matrices
'''
a =np.random.random(10)
print(a)

b= np.random.random((3,2))
print(b)
'''

#14 Generating random numbers

'''
rng = np.random.default_rng()
print(rng)
b = rng.integers(10,size=(2,4))
print(b)
'''


#15 How to get unique items and counts
'''
a= np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_array = np.unique(a)
print(unique_array)

index = np.unique(a, return_index=True)   #To get the indices of unique values in a NumPy array 
                                          #(an array of first index positions of unique values in the array)
print(index)

counts = np.unique(a, return_counts=True) #get the frequency count of unique values in a NumPy array.
print(counts)
'''
          #for 2d array
'''
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [2, 2, 3, 4]])
unique_rows, indices, occurrence_count = np.unique(
     a_2d, return_index=True, return_counts=True)

print(a_2d)
print(unique_rows)
print(indices)
print(occurrence_count)
'''

#16 Transposing and reshaping a matrix
'''
a = np.array([[1,2,3],
               [4,5,6]])

b = np.arange(6).reshape(2,3)
print(b)

print(a.T)
print(a.transpose())
print(a.reshape(3,2))
'''

#17 How to reverse an array
'''
a = np.arange(1,10).reshape(3,3)
print(a)
print(np.flip(a))
print(np.flip(a, axis=0))
print(np.flip(a, axis=1))
'''

#18 Reshaping and flattening multidimensional arrays
'''
a = np.arange(0,100,5).reshape(4,5)
print(a)

print(a.flatten())       # It changes to your new array won’t change the parent array.


b =a.ravel()             # The new array created using ravel() is actually a reference to the parent array (i.e., a “view”).
b[0] = 69                # This means that any changes to the new array will affect the parent array as well.
print(np.ravel(a))       # Since ravel does not create a copy, it’s memory efficient.
'''

#19 How to access the docstring for more information
'''help()'''


#20 Working with mathematical formulas
'''
a= np.array([10,20,30]).reshape(3,1)
b= np.array([2,1,4]).reshape(3,1)

print(a)
print(b)
'''
     # Formula -> MeanSquareError= (1/n)*(summation of(square of(pridictions - labels)))
'''
n=3
predictions = a
labels = b

MeanSquareError= (1/n)*(np.sum(np.square(predictions - labels)))
print(MeanSquareError)
'''

#21 How to save and load NumPy objects
'''
a =np.arange(1,10).reshape(3,3)
print(a)
print(a.dtype)

np.save('my_3X3_matrix', a)

b= np.load('my_3X3_matrix.npy')
print(b)
print(b.dtype)

np.savetxt('my_3X3_matrix.csv', a)
c= np.loadtxt('my_3X3_matrix.csv')
print(c)
print(c.dtype)
'''
'''
np.save  -> If you want to store a single ndarray object, store it as a .npy file.
np.savez -> If you want to store more than one ndarray object in a single file, save it as a .npz file.
np.load -> to reconstruct your array.
np.savetext -> You can save a NumPy array as a plain text file like a .csv or .txt file.
np.loadtxt -> You can quickly and easily load your saved text file
note -> The savetxt() and loadtxt() functions accept additional optional parameters such as header, footer, and delimiter
          While text files can be easier for sharing, .npy and .npz files are smaller and faster to read.
          if you need to work with lines that contain missing values), you will want to use the genfromtxt function.
'''

#22 Importing and exporting a CSV

'''
import pandas as pd

x = pd.read_csv('/home/muhammad-iftikhar/python-files/Sowpods (Copy).csv')
print(x)

a= np.arange(0,100,5).reshape(4,5)
print(a)
df =pd.DataFrame(a)
print(df)

df.to_csv('pd_matrix.csv')

data = pd.read_csv('pd_matrix.csv')
print(data)
'''


#23 Plotting arrays with Matplotlib

import matplotlib.pyplot as plt
'''
a= np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
plt.plot(a)
plt.show()
'''
'''
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
plt.plot(x, y, 'o')      # dots
plt.show()
'''

'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()
'''

