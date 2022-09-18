class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        su = numBottles
        while numBottles >= numExchange:
            su += numBottles // numExchange
            numBottles = numBottles //numExchange + numBottles % numExchange
            # print(su,numBottles)
        return su
        