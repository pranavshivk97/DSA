def farthest_pair(lst):
    # Initialize the max and min values of the list to the first element of the list
    min_num = lst[0]
    max_num = lst[0]

    # iterate through the array and check if each element is greater than max or less than min
    for i in range(0, len(lst), 1):
        if lst[i] < min_num:
            min_num = lst[i]
        if lst[i] > max_num:
            max_num = lst[i]

    # calculate the distance between max and min
    dist = abs(max_num - min_num)

    return min_num, max_num, dist


def main():
    arr = []

    txt = input("Enter the text file: ")
    txt1 = open(txt, "r")

    for l in txt1:
        arr.append(int(l))

    print("Input data is: ", arr)
    print("The farthest pair and the distance is {}".format(farthest_pair(arr)))


if __name__ == '__main__':
    main()
