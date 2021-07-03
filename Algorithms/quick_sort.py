import time
from colors import *

def partition(data, drawData, start, end, timeTick):
    i = start + 1
    pivot = data[start]
    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[start], data[i-1] = data[i-1], data[start]
    return i-1


def quick_sort(data, drawData, timeTick, start, end):
    if start < end:
        pivot_position = partition(data, drawData, start, end, timeTick)
        quick_sort(data, drawData, timeTick, start, pivot_position - 1)
        quick_sort(data, drawData, timeTick, pivot_position + 1, end)

        drawData(data, [DARK_BLUE if x >= start and x < pivot_position else YELLOW if x == pivot_position
        else PURPLE if x > pivot_position and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])