from josephus_algorithms.josephus import Josephus
from triple_sum.triple_sum import TripleSum
from insertion_sort.insertion_sort_comparable import InsertionSort
from merge_sort_with_insertion.merge_sort_w_insertion import MergeSortWithInsertion


def __main__():
    josephus_sample = Josephus([3, 6, 2, 7, 5, 1, 4])
    josephus_sample_result = josephus_sample.josephus_algorithm_survivor_output(7, 3)
    print(
        "1. Josephus algorithm with Queue with two Stacks\n1-1. Josephus sample result for [3, 6, 2, 7, 5, 1, "
        "4] is returned as {}".format(josephus_sample_result)
    )
    ts = TripleSum()
    ts.set_nums([-1, 0, 1, 2, -1, -4])
    print(
        "2. TripleSum algorithm with comparable elements inside of it\n2-1. "
        "TripleSum result for {} is {}".format(str(ts.get_nums()), ts.triple_sum())
    )

    sorter = InsertionSort([3, 4, 1, 2, 5, 6])
    sorter.sort()
    print(
        "3. Insertion sort for the comparable elements involving list\n3-1. Insertion Sort result "
        "for the input X [3, 4, 1, 2, 5, 6] is {}".format(sorter.data)
    )

    sorter.data = [3, 7, 1, 2, 5, 6]
    sorter.sort()
    print(
        "3-2. Insertion Sort result for the input X [3, 7, 1, 2, 5, 6] is {}".format(
            sorter.data
        )
    )

    sorter = MergeSortWithInsertion(cutoff=7)  # Set cutoff to 7
    arr = [2, 22, 41, 12, 7, 9, 51, 23, 60]
    sorter.sort(arr)
    print(
        "4. Merge sort with insertion\n4-1. Merge Sort with Insertion result for the input array "
        "[2, 22, 41, 12, 7, 9, 51, 23, 60] is {}".format(arr)
    )


if __name__ == "__main__":
    __main__()
