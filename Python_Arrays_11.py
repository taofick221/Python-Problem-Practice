# Create an array
import array as arr

# Create an array of integers
integer_array = arr.array('i', [1, 2, 3, 4, 5]) 
print("Integer Array:", integer_array)



# Create an array of floats
float_array = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print("Float Array:", float_array)



# Accessing array elements
print("First element of integer array:", integer_array[0])
print("Second element of float array:", float_array[1])



# Modifying array elements
integer_array[2] = 10
float_array[3] = 9.9
print("Modified Integer Array:", integer_array)
print("Modified Float Array:", float_array)
print()


# Array operations
# Appending elements
integer_array.append(6)
float_array.append(6.6)
print("Appended Integer Array:", integer_array)
print("Appended Float Array:", float_array)
