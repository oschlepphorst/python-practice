# You are given n people represented as an integer from 0 to n - 1, 
# and a list of friends tuples, where person friends[i][0] and person 
# friends[i][1] are friends.
#Return whether everyone has at least one friend.

class Solution:
    def solve(self, n, friends):
        allfriends = []
        for i in range(len(friends)):
            for j in range(len(friends[i])):
                allfriends.append(friends[i][j])
        out = True
        for x in range(n):
            if(x not in allfriends):
                out = False
        return out