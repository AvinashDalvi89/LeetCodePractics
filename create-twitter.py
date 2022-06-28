from collections import defaultdict
class Twitter(object):

    def __init__(self):
        self.tweet = collections.defaultdict(list)
        self.followers = collections.defaultdict(list)
        self.tweet_counter = collections.defaultdict(int)
        self.counter = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.counter += 1 
        self.tweet[userId].append((self.counter, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        #print(self.followers)
        #print(self.tweet[userId][::])
        tweetlist = self.tweet[userId][::]
        #print(tweetlist)
        for follower in self.followers[userId]:
            tweetlist.extend(self.tweet[follower])
        
        tweetlist.sort(reverse=True)
        #print(tweetlist)
        return [tweetId for counter, tweetId in tweetlist[:10]]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        #print(self.followers)
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
