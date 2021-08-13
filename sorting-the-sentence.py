#solution
class Solution:
    def sortSentence(self, s: str) -> str:
        li=s.split(' ')
        res=['elem']*len(li)
        for x in range(len(li)):
            print(x)
            res[x]=li[x]
        return res
        print(li)
        print(res)
