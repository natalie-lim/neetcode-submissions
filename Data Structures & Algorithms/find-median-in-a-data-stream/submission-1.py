class MedianFinder:

    def __init__(self):
        self.pq = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.pq, num)

    def findMedian(self) -> float:
        print("heap curr: ", self.pq)
        l = len(self.pq) - 1
        num = l / 2
        ceil = math.ceil(num)
        floor = math.floor(num)
        if ceil == floor:
            toPush = []
            popped = 0
            for i in range(ceil + 1):
                popped = heapq.heappop(self.pq)
                toPush.append(popped)
            while toPush:
                val = toPush.pop()
                heapq.heappush(self.pq, val)
            return popped

        else:
            print("is not normal")
            first = self.pq[ceil]
            second = self.pq[floor]
            toPush = []
            popped1 = 0
            popped2 = 0
            for i in range(ceil + 1):
                popped1 = popped2
                popped2 = heapq.heappop(self.pq)
                toPush.append(popped2)
            while toPush:
                val = toPush.pop()
                heapq.heappush(self.pq, val)
            return (popped1 + popped2) / 2