class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for x in range(len(word)):
            res=''
            if word[x]==ch:
                print(x)
                res=word[x::-1]+word[x+1:]
                return res
                break
