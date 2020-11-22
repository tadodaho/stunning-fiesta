import numpy as np


def partition(collection, n):
    length = len(collection)
    if n > length:
        raise ValueError
    new_list = [[] for i in range(n)]
    idx = 0
    for e in collection:
        part = length // n + length % n
        if len(new_list[idx]) == part:
            idx += 1
            n -= 1
            length -= part
        new_list[idx].append(e)
    return new_list


def TestCase():
    assert(len(partition(lst_1, 4)) == 4)
    assert(len(partition(lst_2, 2)) == 2)
    assert(len(partition(np_arr, 4)) == 4)
    assert(isinstance(np_arr, np.ndarray) is True)
    assert(isinstance(partition(lst_2, 2)[1][0][0], int) is isinstance(lst_2[2][0], int))
    assert(isinstance(partition(np_arr, 4)[1][0], np.int64) is isinstance(np_arr[3], np.int64))
    print("Test: OK")


if __name__ == "__main__":
    lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    np_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    lst_2 = [[1, 'a', 'b'], [2, 'c', 'd'], [3, 'e', 'f']]

    # TestCase()

    N = 4
    print(type(lst_1), partition(lst_1, N))
    print(type(np_arr), partition(np_arr, N))

    N = 2
    print(type(lst_2), partition(lst_2, N))
