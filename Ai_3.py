def selectionSort(A):
    # Copy original array for displaying unsorted array
    U = A.copy()
    for i in range(len(A)):

        # Assume current index has minimum value
        min_idx = i

        # Find actual minimum element in remaining array
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:

                # Update minimum index
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
    print(f'Selection Sort:\nUnsorted array: {U}\nSorted array: {A}')


if __name__ == '__main__':

    A = [64, 25, 12, 22, 11]
    selectionSort(A)