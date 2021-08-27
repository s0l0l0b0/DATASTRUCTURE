array = []
size = int(input("List size: "))

for i in range (1,size+1):
    item = input(f"Enter something at index {i} : ")
    array.append(item)

element = input("Search for: ")

def binary_search_recursive(array, element, start, end):
    if start > end:
        return "not found"

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

print("Index of {}: {}".format(element, binary_search_recursive(array, element, 0, len(array))))