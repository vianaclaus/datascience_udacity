import numpy as np

if True:
    array = np.array([1, 4, 5, 8, 7, 0, 54, 56], float)
    print array
    print ""
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print array
	
	
if True:
    array = np.array([1, 4, 5, 8, 52, 89, 1], float)
    print array
    print ""
    print array[5]
    print ""
    print array[:1]
    print ""
    array[1] = 9.0
    print array[1]	
	
	
if True:
    two_D_array = np.array([[9,7,5], [6, 5, 4]], float)
    print two_D_array
    print ""
    print two_D_array[2][2]
    print ""
    print two_D_array[1, :]
    print ""
    print two_D_array[:, 2]	
	
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2


if True:
    array_1 = np.array([[56, 22], [31, 46]], float)
    array_2 = np.array([[50, 65], [71, 89]], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2


if True:
    array_1 = np.array([18, 22, 32], float)
    array_2 = np.array([[62], [72], [82]], float)
    print np.mean(array_1)
    print np.mean(array_2)
    print ""
    print np.dot(array_1, array_2)
	
	
