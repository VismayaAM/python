import matplotlib.pyplot as plt
import numpy as np

def animate_binary_search(array, target):
    fig, ax = plt.subplots()
    ax.set_title("Binary Search Animation")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    
    left = 0
    right = len(array) - 1
    found = False
    
    while left <= right and not found:
        mid = (left + right) // 2
        
        ax.clear()
        ax.plot(range(len(array)), array, 'bo-')
        ax.plot(mid, array[mid], 'ro')
        plt.pause(1)  # Pause for 1 second
        
        if array[mid] == target:
            found = True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    ax.clear()
    ax.plot(range(len(array)), array, 'bo-')
    if found:
        ax.plot(mid, array[mid], 'go')
        ax.set_title("Binary Search Animation - Target Found")
        print("Target found at index", mid)
    else:
        ax.set_title("Binary Search Animation - Target Not Found")
        print("Target not found")

    plt.pause(2)  # Pause for 2 seconds
    plt.close()

# Example usage
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

animate_binary_search(array, target)
