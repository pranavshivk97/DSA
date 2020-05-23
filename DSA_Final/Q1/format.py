def main():
    file1 = open("1000EWD.txt", "r")
    file2 = open("file3.txt", 'w')

    # read the file for number of vertces and edges (first 2 lines in the txt)
    v = file1.readline()
    file2.write(v)
    e = file1.readline()
    file2.write(e)

    # add a single space and concatenate each value in the text file with it
    for line in file1:
        file2.write(" ".join(line.split()))
        file2.write("\n")

    file1.close()
    file2.close()


if __name__ == '__main__':
    main()