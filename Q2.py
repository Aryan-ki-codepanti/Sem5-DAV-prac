import numpy as np

# Write programs in Python using NumPy library to do the following:
# a. Compute the mean, standard deviation, and variance of a two dimensional random integer array
# along the second axis.

twoD_array = np.random.randint(1, 100, (5, 5))
print("2D random Array")
print(twoD_array)
print("Mean about 2nd axis")
print(np.mean(twoD_array, axis=1))
print("Standard Deviation about 2nd axis")
print(np.std(twoD_array, axis=1))
print("Variance about 2nd axis")
print(np.var(twoD_array, axis=1))

# b. Get the indices of the sorted elements of a given array.
# a. B = [56, 48, 22, 41, 78, 91, 24, 46, 8, 33]

B = [56, 48, 22, 41, 78, 91, 24, 46, 8, 33]
sorted_B = sorted(B)
indices = list(map(lambda x: sorted_B.index(x), B))

print(f"Orignal B : {B}")
print(f"Sorted : {sorted_B}")
print(f"Indexes in sorted array : {indices}")


# c. Create a 2-dimensional array of size m x n integer elements, also print the shape, type and datatype of the array and then reshape it into nx m array, n and m are user inputs given at the run time.
'''
m = int(input("Enter number of rows : "))
n = int(input("Enter number of columns : "))
mn_arr = np.random.randint(1, 100, (m, n))
nm_arr = np.reshape(mn_arr, (n, m))
print(f"Orignal {m}x{n}\n{mn_arr}")
print(f"Shape : {mn_arr.shape}")
print(f"Dtype : {mn_arr.dtype}")
print(f"Reshaped {n}x{m}\n{nm_arr}")
'''

# d. Test whether the elements of a given array are zero, non-zero and NaN. Record the indices of
# these elements in three separate arrays.


def test_array(arr):
    print(f"Given Array\n{arr}\n")
    print(f"Zero test\n{arr == 0}\n")
    print(f"Non-Zero test\n{arr != 0}\n")
    print(f"NaN Test\n{np.isnan(arr)}\n")


sample_arr = np.random.randn(3, 4)
test_array(sample_arr)
