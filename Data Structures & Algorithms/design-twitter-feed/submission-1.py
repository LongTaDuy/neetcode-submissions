class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetpost = defaultdict(list) # [count, tweetid]
        self.tweetfollow = defaultdict(set) # userid
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetpost[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.tweetfollow[userId].add(userId)
        for followee in self.tweetfollow[userId]:
            if followee in self.tweetpost:
                index = len(self.tweetpost[followee]) - 1
                count, tweetid = self.tweetpost[followee][index]
                minheap.append([count, tweetid, followee, index - 1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetid, followee, index = heapq.heappop(minheap)
            res.append(tweetid)
            if index >= 0:
                count, tweetid = self.tweetpost[followee][index]
                heapq.heappush(minheap, [count, tweetid, followee, index - 1])
        return res
            

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.tweetfollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.tweetfollow[followerId]:
            self.tweetfollow[followerId].remove(followeeId)

