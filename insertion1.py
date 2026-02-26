def insertionSort1(n, arr):
    # Write your code here
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                cur = arr[i]
                arr[i] = arr[j]
                print(' '.join([str(each) for each in arr]))
                arr[j], arr[i] = cur, arr[j]
    print(' '.join([str(each) for each in arr]))
    
