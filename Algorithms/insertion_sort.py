import time
from colors import *

def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        mini = i

        while mini>0 and temp < data[mini-1]:
            data[mini] = data[mini-1]
            mini -= 1
        data[mini] = temp
        drawData(data, [YELLOW if x == mini or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
