'''
P.S:
You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.

Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.

Note:Uppercase letters come before lowercase letters in lexicographical order.
"Alice" and "alice" are distinct.
'''

#Solution:
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        msg = []
        for x in messages:
            msg.append(len(x.split()))       
        di = {}
        for x in range(len(senders)):
            if senders[x] in di:
                di[senders[x]]+=msg[x]
            else:
                di[senders[x]]=msg[x]
        # res = max(di, key=di.get)
        # print(res)
        res=[]
        for x in di:
            if di[x]==max(di.values()):
                res.append(x)
        res.sort()        
        return res[-1]
