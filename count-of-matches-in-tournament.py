#You are given an integer n, the number of teams in a tournament that has strange rules:
If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and ((n - 1) / 2) + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

#Solution:
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        matches=0
        team_move_to_next_level=0
        while n>1:
            if n%2==0:
                matches=n/2
                team_move_to_next_level=n/2
                n=team_move_to_next_level
                res+=matches
            else:
                matches=(n-1)/2
                team_move_to_next_level=((n-1)/2)+1
                n=team_move_to_next_level
                res+=matches
        return res
