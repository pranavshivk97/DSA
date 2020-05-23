# Kendall Tau distance using merge sort

def ktd_merge(arr, low, mid, high):
# Calculate no of inversion pairs using merge sort, which has a complexity of O(NlogN)
    pairs = 0

    n1 = mid - low + 1
    n2 = high - mid

    l_arr = []
    r_arr = []

    for i in range(0, n1):
        l_arr.append(arr[low + i])

    for j in range(0, n2):
        r_arr.append(arr[mid + 1 + j])

    i = j = 0
    k = low

    while i < n1 and j < n2:
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            pairs += mid - (low + i) + 1
            j += 1
        k += 1

    while i < n1:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r_arr[j]
        j += 1
        k += 1

    return pairs

# Recursive merge sort functtion
def ktd_ms(arr, low, high):
    pairs = 0

    if high > low:
        mid = (low + high) // 2
        pairs += ktd_ms(arr, low, mid)
        pairs += ktd_ms(arr, mid + 1, high)
        pairs += ktd_merge(arr, low, mid, high)

    return pairs


def main():

    arr = []

    txt = input("Enter the file to open: ")

    txt1 = open(txt, 'r')

    for l in txt1:
        arr.append(int(l))

    print("Input data: ", arr)

    print("The Kendall Tau distance for the given data is: ", ktd_ms(arr, 0, len(arr) - 1))


if __name__ == '__main__':
    main()


