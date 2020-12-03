

def insetionsort(array):
    for i in range(1, len(array)):
        j = i # insertion
        while j > 0 and array[j] < array[j - 1]: # indices
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    array = [9,8,4,2,5,3]
    print(insetionsort(array))
