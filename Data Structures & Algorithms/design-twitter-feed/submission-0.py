class Twitter:

    def __init__(self):
        self.time=0
        self.tweet_map = collections.defaultdict(list)
        self.follow_map = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time,tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ans=[]
        minHeap=[]

        self.follow_map[userId].add(userId)

        for user in self.follow_map[userId]:
            if user in self.tweet_map:
                index = len(self.tweet_map[user])-1
                time, tweetId = self.tweet_map[user][index]
                heapq.heappush(minHeap,[time, tweetId, user, index])

        while minHeap and len(ans) <10:
            time, tweetId, user, index = heapq.heappop(minHeap)
            ans.append(tweetId)

            index-=1

            if index>=0:
                time, tweetId = self.tweet_map[user][index]
                heapq.heappush(minHeap, [time, tweetId, user, index])


        return ans            



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map.get(followerId).remove(followeeId)

        
