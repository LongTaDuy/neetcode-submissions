class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hashmap = {}
        for i in range(len(hand)):
            if hand[i] not in hashmap:
                hashmap[hand[i]] = 1
            else:
                hashmap[hand[i]] += 1
        minH = list(hashmap.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i in hashmap:
                    hashmap[i] -= 1
                else:
                    return False
                if hashmap[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
                    
