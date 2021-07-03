import time
from colors import *

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)- 1):
        mini = i
        for k in range(i+1, len(data)):
            if data[k]<data[mini]:
                mini = k

        data[mini], data[i] = data[i], data[mini]
        drawData(data, [YELLOW if x == mini or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])