def binary_search(array, x): 
    low = 0
    high = len(array) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if array[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif array[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1


def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
  
        for j in range(0, n-i-1): 
   
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
  
# Test array 
array = []
size = int(input("List size: "))

for i in range (1,size+1):
    item = int(input(f"Enter something at index {i} : "))
    array.append(item)

print(array)

bubbleSort(array)

print(array)
    
x = int(input("Search for : "))
  
# Function call 
result = binary_search(array, x) 
  
if result != -1: 
    print(f"Index of {x} : {result+1}") 
else: 
    print(f"Index of {x} : not found") 

