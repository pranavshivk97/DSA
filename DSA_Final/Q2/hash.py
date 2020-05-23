# Name: Pranav Shivkumar (ps1029)
# Hash Table


# function to compute the hash value for each key in the table based on the hash function
def hash_table(vals):
    A = list(range(2, 31))  # range of values for A, from 2 to 30
    M = list(range(1, 27))  # range of values for M, from 1 ot 26 (set to the number of letters in the alphabet

    a = []
    m = []
    result = []

    # iterate over M, A and length of values
    for k in range(len(M)):
        for j in range(len(A)):
            for i in range(len(vals)):
                func = (A[j] * vals[i]) % M[k]  # compute the hash values
                result.append(func)  # append to a list, along with
                a.append(A[j])  # the corresponding values for A and
                m.append(M[k])  # M

    n = len(vals)

    # split the list into a list of lists
    fin = [result[i * n:(i + 1) * n] for i in range((len(result) + n - 1 // n))]

    return fin, a, m


# function to check if the hashed values are distinct
def is_distinct(fin, vals, a, m):
    n = len(vals)

    for i in range(len(fin)):
        for j in range(len(fin[i])):
            for k in range(n):
                if len(fin[i]) == len(set(fin[i])):     # if distinct return to main and print
                    return fin[i], a[i * n], m[i * n]


def main():
    # original values for keys
    keys = {'S': 18, 'E': 4, 'A': 0, 'R': 17, 'C': 2, 'H': 7, 'X': 23, 'M': 12, 'P': 15, 'L': 11}
    vals = list(keys.values())          # extract the values from the dictionary
    print("Original values are: {}\n".format(vals))
    print("Results")

    res, a, m = hash_table(vals)
    fin, a, m = is_distinct(res, vals, a, m)

    print("A = {}, M = {}, Hash table values = {}".format(a, m, fin))


if __name__ == '__main__':
    main()
