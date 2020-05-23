import matplotlib.pyplot as plt
import numpy as np


def main():
    print("TRIE TREE")
    import Trie_2
    comp_trie, time_trie_ins, time_trie_search, count_trie_node = Trie_2.trie_result()
    print("Insertion: ", time_trie_ins)
    print("Search: ", time_trie_search)

    print("RADIX TREE")
    import radix_2
    comp_radix, time_radix_ins, time_radix_search, count_radix_node = radix_2.radix_result()
    print("Insertion: ", time_radix_ins)
    print("Search: ", time_radix_search)

    time = np.array([1, 2, 3, 4, 5, 6])
    time1 = np.array([10, 20, 30, 40, 50, 60])

    y1 = np.row_stack((count_trie_node, count_radix_node))

    fig1, ax1 = plt.subplots()
    fig1.canvas.set_window_title("Insertion Analysis")

    ax1.plot(time1, y1[0], label="Trie Tree", color="c", marker="o")
    ax1.plot(time1, y1[1], label="Radix Tree", color="g", marker="o")

    plt.xticks(time1)
    plt.xlabel("Number of Words Inserted")
    plt.ylabel("Number of Nodes Created")
    plt.title("Insertion Analysis")

    handles, labels = ax1.get_legend_handles_labels()
    legend = ax1.legend(handles, labels, loc="upper center")

    ax1.grid('on')

    plt.savefig("insertion_analysis.png")

    y4 = np.row_stack((time_trie_ins, time_radix_ins))

    fig1, ax3 = plt.subplots()
    fig1.canvas.set_window_title("Insertion Analysis")

    ax3.plot(time1, y4[0], label="Trie Tree", color="c", marker="o")
    ax3.plot(time1, y4[1], label="Radix Tree", color="g", marker="o")

    plt.xticks(time1)
    plt.xlabel("Number of Words Inserted")
    plt.ylabel("Time (ns)")
    plt.title("Insertion Time Analysis")

    handles, labels = ax3.get_legend_handles_labels()
    legend = ax3.legend(handles, labels, loc="upper right")

    ax3.grid('on')

    plt.savefig("insertion_time_analysis.png")

    y3 = np.row_stack((time_trie_search, time_radix_search))

    fig1, ax3 = plt.subplots()
    fig1.canvas.set_window_title("Search Analysis")

    ax3.plot(time, y3[0], label="Trie Tree", color="c", marker="o")
    ax3.plot(time, y3[1], label="Radix Tree", color="g", marker="o")

    plt.xticks(time)
    plt.xlabel("Number of Words with Common Prefix")
    plt.ylabel("Time (ns)")
    plt.title("Search Analysis")

    handles, labels = ax3.get_legend_handles_labels()
    legend = ax3.legend(handles, labels, loc="upper right")

    ax3.grid('on')

    plt.savefig("search_analysis.png")

    y2 = np.row_stack((comp_trie, comp_radix))

    fig2, ax2 = plt.subplots()
    fig2.canvas.set_window_title("Comparison Analysis")

    ax2.plot(time, y2[0], label="Trie Tree", color="c", marker="o")
    ax2.plot(time, y2[1], label="Radix Tree", color="g", marker="o")

    plt.xticks(time)
    plt.xlabel("Number of Words with Common Prefix")
    plt.ylabel("Number of Comparisons")
    plt.title("Comparison Search Analysis")

    handles, labels = ax2.get_legend_handles_labels()
    legend = ax2.legend(handles, labels, loc="upper center")
    ax2.grid('on')

    plt.savefig("comparison_analysis.png")

    plt.show()


if __name__ == '__main__':
    main()
