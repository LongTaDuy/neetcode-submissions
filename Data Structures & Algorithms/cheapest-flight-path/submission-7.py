class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0
        for i in range(k + 1):
            tmp_price = price.copy()
            for s, d, p in flights:
                if price[s] == float("inf"):
                    continue
                if price[s] + p < tmp_price[d]:
                    tmp_price[d] = price[s] + p
            price = tmp_price
        return -1 if price[dst] == float("inf") else price[dst]