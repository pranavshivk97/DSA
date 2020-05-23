import time

count = 0
count1 = 0
time_trie_ins = []
time_trie_search = []
count_trie_node = []
comp_trie = []
comp_trie1 = []


class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


def insertWord(root, word):
    '''
    Loop through characters in a word and keep adding them at a new node, linking them together
    If char already in node, pass
    Increment the current to the child with the character
    After the characters in word are over, mark current as EOW
    '''
    global count1
    current = root
    for char in word:
        if char in current.children.keys():
            pass
        else:
            count1+=1
            current.children[char] = Node()
        current = current.children[char]
    current.endOfWord = True


def allWords(prefix, node, results,i):
    '''
    Recursively call the loop
    Prefix will be prefix + current character
    Node will be position of char's child
    results are passed by reference to keep storing result

    Eventually, when we reach EOW, the prefix will have all the chars from starting and will be the word that we need. We add this word to the result
    '''
    global count
    if node.endOfWord:
        results.append(prefix)
    for char in node.children.keys():
        if i==0:
            count += 1
        # print char, node, node.children
        allWords(prefix + char, node.children[char], results,i)


def searchWord(root, word):
    '''
    Loop through chars of the word in the trie
      If char in word is not in trie.children(), return
      If char found, keep iterating
    After iteration for word is done, we should be at the end of word. If not, then word doesn't exist and we return false.
    '''
    current = root
    search_result = True
    for char in word:
        if char in current.children.keys():
            pass
        else:
            search_result = False
            break
        current = current.children[char]

    return search_result


def getWordsWithPrefix(prefix, node, prefix_result,i):
    '''
    We loop through charcters in the prefix along with trie
    If mismatch, return
    If no mismatch during iteration, we have reached the end of prefix. Now we need to get words from current to end with the previx that we passed. So call allWords with prefix
    '''

    global count
    current = node

    for char in prefix:
        if char in current.children.keys():
            if i==0:
                count += 1
            pass
        else:
            return

        current = current.children[char]
    allWords(prefix, current, prefix_result,i)


def trie_result():
    # Input keys (use only 'a' through 'z' and lower case)
    # keys = ["the", "a", "there", "anaswe", "any","by", "their"]

    files = ["no_prefix.txt", "2common_prefix.txt", "3common_prefix.txt", "4common_prefix.txt", "5common_prefix.txt", "6common_prefix.txt"]
    words = [[] for i in range(len(files))]

    for file in range(len(files)):
        print("Importing data from file {}".format(files[file]))
        f = open("words/" + files[file], "r")
        lines = f.readlines()
        for line in lines:
            words[file].append(line.strip())


        time_ins=0
        root = Node()
        for i in range(1000):

            start_ins = time.time_ns()

            for i in range(len(words)):
                for key in words[i]:
                    insertWord(root, key)

            stop_ins = time.time_ns()
            time_ins += (stop_ins - start_ins)
        print("Time taken for inserting words into the trie tree is: ", time_ins/1000, "ns.")
        print("Number of nodes in the trie tree = ", count1)

        string = input("Enter the Prefix you want: ")
        time_search=0



        for i in range(1000):
            start_search = time.time_ns()

            if searchWord(root, string):
                prefix_result = []
                getWordsWithPrefix(string, root, prefix_result,i)
                if i==0:
                    print('\nWords starting with', string)
                    for word in prefix_result:
                        print(word)
                stop_search = time.time_ns()
                time_search += (stop_search - start_search)

                if i==0:
                    print("Number of comparisons: ", count)



            else:
                if i==0:
                    print("The key or prefix doesn't exist")
                    str1 = input('Enter the whole word you want to add')
                    insertWord(root, str1)

        comp_trie.append(count)
        time_trie_ins.append(time_ins/1000)
        time_trie_search.append(time_search / 1000)
        count_trie_node.append(count1)

    print("Comparisons: ", comp_trie)
    print("Insertion times: ", time_trie_ins)
    print("Search times: ", time_trie_search)
    print("Number of nodes: ", count_trie_node)
    print("\n")

    with open("trie_results.txt", "w") as file:
        for item in comp_trie:
            file.write(str(item))
            file.write(" ")
        file.write("\n")
        for item in time_trie_ins:
            file.write(str(item))
            file.write(" ")
        file.write("\n")
        for item in time_trie_search:
            file.write(str(item))
            file.write(" ")
        file.write("\n")
        for item in count_trie_node:
            file.write(str(item))
            file.write(" ")
        file.write("\n")

    file.close()

    return comp_trie, time_trie_ins, time_trie_search, count_trie_node


# def common_word():
#     file = open("common_prefix.txt", "r")
#     words = []
#
#     lines = file.readlines()
#     for line in lines:
#         words.append(line.strip())
#
#     # start_ins = time.time_ns()
#
#     root = Node()
#
#     for i in range(len(words)):
#         for key in words[i]:
#             insertWord(root, key)
#
#     string = ["kl", "he", "an", "ne", "mi", "ab", "lo", "ta", "bo", "fl"]
#
#     for j in range(len(string)):
#         if searchWord(root, string[j]):
#             prefix_result = []
#             getWordsWithPrefix(string[j], root, prefix_result)
#             print('\nWords starting with', string[j])
#             for word in prefix_result:
#                 print(word)
#             print("Number of comparisons: ", count)
#         # else:
#         #     print("The key or prefix doesn't exist")
#         #     str1 = input('Enter the whole word you want to add')
#         #     insertWord(root, str1)
#
#         comp_trie1.append(count)
#
#     print("Comparisons: ", comp_trie1)
#
#     with open("common_trie_results.txt", "w") as file:
#         for item in comp_trie1:
#             file.write(str(item))
#             file.write(" ")
#         file.write("\n")
#
#     file.close()
#
#     return comp_trie1





