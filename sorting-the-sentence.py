'''
P.S: Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"sentence4 a3 is2 This1" -> "This is a sentence"
'''

#Solution:
class Solution:
    def sortSentence(self, s: str) -> str:
        li=s.split()
        li_copy=['a']*len(li)
        for x in li:
            li_copy[int(x[-1])-1]=x[:-1]
        return ' '.join(li_copy)
            

