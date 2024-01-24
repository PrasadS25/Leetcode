class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        self.followMap[userId].add(userId)
        res = []
        minheap = []
        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                index = len(self.tweetMap[followee])-1
                count, tweetId = self.tweetMap[followee][index]
                minheap.append([count,tweetId,followee,index-1])

        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index>=0:
                count , tweetId = self.tweetMap[followee][index]
                heapq.heappush(minheap,[count,tweetId,followee,index-1])        

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)