import array as arr # in this approach we have to use arr.array() to create an array.

#  Batter approach is  ---->
from array import *

my_array = array('i',[1,2,3,4,5,6,7,8])  

#| Code | Meaning | Minimum bytes |
# |---|---|---:|
# | `b` | Signed char (integer) | 1 |
# | `B` | Unsigned char (integer) | 1 |
# | `u` | Unicode character | 2 |
# | `w` | Unicode character (Python 3.13+) | 4 |
# | `h` | Signed short | 2 |
# | `H` | Unsigned short | 2 |
# | `i` | Signed int | 2 |
# | `I` | Unsigned int | 2 |
# | `l` | Signed long | 4 |
# | `L` | Unsigned long | 4 |
# | `q` | Signed long long | 8 |
# | `Q` | Unsigned long long | 8 |
# | `f` | Float | 4 |
# | `d` | Double | 8 |

for i in range(len(my_array)):
    print(my_array[i],end=" ") # end = " " is used to print the elements in the same line

print("\n")
for i in my_array:
    print(i,end=" , ")


my_array.insert(0,0) # insert(index,value) is used to insert a value at a specific index

# and append() is used to add a value at the end of the array.
my_array.append(9)

my_array[0] = 10 # update the value at index 0

copy_array = array(my_array.typecode, (element for element in my_array))

copy_array.pop() # remove the last element of the array
copy_array.remove(10) # remove the value 10 from the array


slice_array = my_array[2:-3]


 
# User input in an array 

user_array = array('i',[])

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    user_array.append(int(input("Enter the element: ")))

print("This is the user array: ",user_array)