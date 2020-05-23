# Referred https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/ for the algorithm
def initialize(lst):
    l = len(lst)
    count = 0

    # define a and b as shown to iterate through the list. a will be te consecutive elements in the list
    for i in range(0, l - 1):
        a = i + 1
        b = l - 1
    # if the sum is 0, increment count and a and reduce b
        while a < b:
            if lst[i] + lst[a] + lst[b] == 0:
                count += 1
                a += 1
                b -= 1
            # otherwise increment a
            elif lst[i] + lst[a] + lst[b] < 0:
                a += 1
            # else decrease b
            elif lst[i] + lst[a] + lst[b] > 0:
                b -= 1
            else:
                print("Not found")

    return count


def three_sum(lst):
    count = 0
    cnt = 0
    length = len(lst)

    for i in range(0, len(lst)):
        cnt += 1
        lst.sort()
        count += initialize(lst)

    print("Time taken for computation = ", cnt)

    return count


def main():
    data = []

    # read the data and copy into a list
    txt1 = open("8int.txt", "r")
    for l in txt1:
        data.append(int(l))
    print("Number of three sums in the list is: ", three_sum(data))
    print("\n")


if __name__ == '__main__':
    main()
