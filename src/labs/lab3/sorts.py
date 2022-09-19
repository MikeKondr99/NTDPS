from typing import TypeVar

TNum = TypeVar("TNum", int, float, str)


def bubble(input: list[TNum]) -> list[TNum]:
    res = input[:]
    for i in range(0, len(res)):
        for j in range(0, len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


def selection(input: list[TNum]) -> list[TNum]:
    res = input[:]
    for i in range(0, len(res)):
        min = i
        for j in range(i, len(res)):
            if res[j] < res[min]:
                min = j
        res[min], res[i] = res[i], res[min]
    return res


def quick(input: list[TNum]) -> list[TNum]:
    def sort(start: int, end: int) -> None:
        if start < end:
            p = partition(start, end)
            sort(start, p - 1)
            sort(p + 1, end)

    def partition(start: int, end: int) -> int:
        pivot = res[end]
        i = start
        for j in range(start, end):
            if res[j] <= pivot:
                res[i], res[j] = res[j], res[i]
                i += 1
        res[i], res[end] = res[end], res[i]
        print(i)
        print(res)
        return i

    res = input[:]
    sort(0, len(res) - 1)
    return res
