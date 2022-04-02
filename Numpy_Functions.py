'''
python3 -m venv env
pip3 install numpy
'''

import numpy as np

# initializing the array
a = np.array([1, 2, 3]) #Creating 1D array
# a = np.array([1, 2, 3], dtype = 'int16') will set the memory size as 16 bits instead of default 32

b = np.array([[2.4, 3.5, 4.6], [3.6, 8.9, 10.0]]) # 2D array with floating values

# You can create any dimensional array this way

# Getting Dimensions
b.ndim # Returns 2

# Shapes (Returns tuple of the dimensions of the array as (row, column))
a.shape # Returns (3,)
b.shape # Returns (2, 3)

# Get types and memory size
a.dtype # Returns int32 data type by default
a.itemsize # Returns the number of memory locations, i.e, 4 by default
a.size # Total number of elements
a.nbytes # Returns total number of bytes, same as a.size * a.itemsize
b.itemsize # returns 8 as floats are larger




'''Accessing or changinfg specific elements'''
a = np.array([1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]) # 2x7 array

# Get a specific Element
a[1, 5] # Returns 13 as It is in INDEX 1 of row and 5 of column
a[1, -2] # Returns 13 as negative indexing is also valid

# Get a specific row
a[0, :] # Returns the 0th index row using SLICING SYNTAX

# Get a column
a[:, 2] # : signifies "Get all"

# You can use anything following [startindex:endindex:stepsize]
a[0, 1:6:2] # Returns array([2, 4, 6])

# Changing Elements
a[1, 5] = 20
a[: , 2] = 5 # Changes the column with 2nd index to all 5's
a[:, 2] = [1, 2] # Changes the respective elements to 1 and 2
# If you are using more dimensions, make sure that the subsequence follows that dimension as well


'''Initializing different types of arrays'''
np.zeros(5) # Returns a VECTOR of 5 : array([0., 0., 0., 0., 0.])
np.zeros((2, 4)) # 2x4 dimensional matrix
np.ones((2, 4, 3)) # Vector Matrix with all 1's
np.ones((2, 4), dtype = 'int32')
np.full((2, 3), 99) # Populates a 2x3 matrix with the values till 99

np.full_like(a, 4) # Populates the array of dimensions same as a but with values 4
np.full(a.shape, 4) # Same as above

# Random floats matrix
np.random.rand(4, 2) # 4x2 matrix of random numbers
np.random.random_sample(a.shape) # Random matrix with same dimensions as a

# Random integers matrix
np.random.randint(7) # Default start value is 0, but can be mentions as (start, end) parameter
np.random.randint(4, 7, size = (3, 3)) # 3x3 from 4 to 6. You can even include negative numbers

# Identity Matrix 
np.identity(5) # Vector 5x5 identity matrix

# Repeating arrays
arr = np.array([[1, 2, 3]]) # Use 2D Matrix as we are working with vectors
r1 = np.repeat(arr, 3, axis = 0) # Try with axis = 1

# Printing arary problems
output = np.ones((5, 5))
z = np.zeros ((3, 3))
z[1, 1] = 9
output[1:-1, 1:-1] = z


# Be careful while copying arrays
a = np.array([1, 2, 3])
b = a # This just makes b point to the same place a does, we did not create a new array and copy its contents
b[0] = 100 # This will not only change b, but will change a as well even though b is just a copy
b = a.copy() # This will create a new array that will not affect the first array


'''Mathematics : Useful for element wise arithmetic'''
a = np.array([1, 2, 3, 4])
a + 2 # Adds 2 to each element, same for other operations like - += * ** etc
b = np.array([3, 4, 5, 9])
a + b

np.sin(a) # Same for cos tan inverse etc.


# USING LINEAR ALGEBRA
a = np.ones((2, 3))
b = np.full((3, 2), 2)
# Make sure that the dimensions match for multiplications, else you'll get VALUE ERROS
np.matmul(a, b)

c = np.identity(3)
np.linalg.det(c) # Determinant of identity matrix is one

# Try Eigen Values, inverse of matrix, Trace, SVD etc.


# USING STATISTICS 
stats = np.arary([[1, 2, 3], [4, 5, 6]])
np.min(stats) # Returns the min of the stats
np.max(stats) # Returns the max of the stats

np.min(stats, axis = 1) # Returns array([1, 4]) as they are the mins of both rows respectively. Axis can be 0
np.sum(stats, axis = 0) # Arrays added columnwise




'''Reorganizing Arrays'''
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
after = before.reshape((8, 1)) # makes it a 8x1
after = before.reshape((2, 2, 2)) # As long as it has same values, you can reshape it to anything


# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

np.vstack(v1, v2, v2, v1) # Any number of parameters

# Horizontally stacking vectors
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

np.hstack((h1, h2))



'''MISC'''
# Loading Data from files (Use pandas)
file = np.genfromtext('name.txt', delimiter = ',')
file = file.astype('int32') # Else it 


# Boolean masking and advanced indexing
file > 50 # Returns True and False in each position with same dimension as the array

file[file > 50] # Returns only the numbers which are over 50

# You can index with a list in Numpy
a[[2, 3, 4]] # Values at 3, 4, and 5



np.any(file > 50, axis = 0)
np.all(file > 50, axis = 0)
((filedata > 50) & (filedata < 100))