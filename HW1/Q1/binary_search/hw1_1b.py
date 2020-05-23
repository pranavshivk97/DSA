def bin_search(lst, e):
    low = 0
    high = len(lst)

    mid = (low + high) / 2

    for i in range(0, len(lst), 1):
        for j in range(i + 1, len(lst), 1):
            if e == mid:
                return mid
            elif e > mid:
                low = mid + 1
            elif e < mid:
                high = mid - 1
            else:
                print("Element not found")


def three_sum_n2logn(lst):
    count = 0
    cnt = 0
    x = 0
    length = len(lst)

    for i in range(0, length, 1):
        cnt += 1
        for j in range(i + 1, length, 1):
            cnt += 1
            x = -(lst[i] + lst[j])
            if bin_search(lst, x):
                count += 1

    print("Time taken: ", cnt)


def main():
    data = []

    txt1 = open("8int.txt", "r")
    for l in txt1:
        data.append(int(l))

    # print("Input data (8): ", data)
    data = sorted(data)

    print("Triplets with the sum (8) is: ", three_sum_n2logn(data))
    print("\n")

    txt2 = open("32int.txt", "r")
    for l in txt2:
        data.append(int(l))

    # print("Input data (32): ", data)
    print("Triplets with the sum (32) is: ", three_sum_n2logn(data))
    print("\n")

    txt3 = open("128int.txt", "r")
    for l in txt3:
        data.append(int(l))

    # print("Input data (128): ", data)
    print("Triplets with the sum (128) is: ", three_sum_n2logn(data))
    print("\n")

    txt4 = open("512int.txt", "r")
    for l in txt4:
        data.append(int(l))

    # print("Input data (512): ", data)
    print("Triplets with the sum is (512): ", three_sum_n2logn(data))
    print("\n")

    txt5 = open("1024int.txt", "r")
    for l in txt5:
        data.append(int(l))

    # print("Input data (1024): ", data)
    print("Triplets with the sum (1024) is: ", three_sum_n2logn(data))
    print("\n")

    txt6 = open("4096int.txt", "r")
    for l in txt6:
        data.append(int(l))

    # print("Input data (4096): ", data)
    print("Triplets with the sum (4096) is: ", three_sum_n2logn(data))
    print("\n")

    txt7 = open("4192int.txt", "r")
    for l in txt7:
        data.append(int(l))

    # print("Input data (4192): ", data)
    print("Triplets with the sum (4192) is: ", three_sum_n2logn(data))
    print("\n")

    txt8 = open("8192int.txt", "r")
    for l in txt8:
        data.append(int(l))

    # print("Input data (8192): ", data)
    print("Triplets with the sum (8192) is: ", three_sum_n2logn(data))
    print("\n")


if __name__ == '__main__':
    main()
