from random import randint


# создаем массив размера size и заполняем случайными целыми числами из диапазона [-100; 100)
size = 10
array = [randint(-100, 100) for x in range(size)]

# выводим исходный массив
print('Initial array:')
print(array)
# print('*' * 30)
# print('Bubble sort')
# n = 1
# while n < len(array):
#     for i in range(len(array) - n):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
#     print(array)
# print(array)


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# print(heapSort(array))
# Driver code to test above
# arr = [ 12, 11, 13, 5, 6, 7]
heapSort(array)
n = len(array)
print ("Sorted array is")
for i in range(n):
    print ("%d" %array[i]),
# This code is contributed by Mohit Kumra