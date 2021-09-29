class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for x in operations:
            if "-" in x:
                res-=1
            else:
                res+=1
        return res
