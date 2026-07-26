import time

class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = [] # (timestamp, tweetId)
        self.following = [] # user1, user2, etc
    
    def tweet(self, tweetId):
        self.tweets.append((-time.time(), tweetId))
    
    def follow(self, user):
        if user not in self.following:
            self.following.append(user)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)

    def getNewsFeed(self):
        bigHeap = []
        bigHeap.extend(self.tweets)
        for user in self.following:
            bigHeap.extend(user.tweets)
        heapq.heapify(bigHeap)
        num_loops = min(10, len(bigHeap))
        feed = []
        for i in range(num_loops):
            time, tweet = heapq.heappop(bigHeap)
            feed.append(tweet)
        return feed

class Twitter:

    def __init__(self):
        self.d = {} #user id, User

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.d:
            user = self.d[userId]
            user.tweet(tweetId)
        else:
            user = User(userId)
            user.tweet(tweetId)
            self.d[userId] = user

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.d:
            user = self.d[userId]
            return user.getNewsFeed()
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = None
        followee = None
        if followerId != followeeId:
            if followerId in self.d:
                follower = self.d[followerId]
            else:
                follower = User(followerId)
                self.d[followerId] = follower

            if followeeId in self.d:
                followee = self.d[followeeId]
            else:
                followee = User(followeeId)
                self.d[followeeId] = followee
            
            follower.follow(followee)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.d:
            follower = self.d[followerId]
        else:
            return
        if followeeId in self.d:
            followee = self.d[followeeId]
        else:
            return

        follower.unfollow(followee)
