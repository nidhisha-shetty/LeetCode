# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
#You are also given a rule represented by two strings, ruleKey and ruleValue.

#Solution:
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        for subarray in items:
            if ruleKey=="type":
                if  subarray[0]==ruleValue:
                    count+=1
            elif ruleKey=="color":
                if subarray[1]==ruleValue:
                    count+=1
            else:
                if subarray[2]==ruleValue:
                    count+=1
        return count
