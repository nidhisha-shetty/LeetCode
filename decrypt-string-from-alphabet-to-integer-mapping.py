#Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.

#Solution
**using-dictionary**
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''   
        x=0                         
        di={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',
            8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',
            17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        while x<len(s):
            if (x+2)<len(s) and s[x+2]=='#':
                res+=(di[int(s[x:x+2])])
                x+=3
            else: 
                res+=di[int(s[x])]
                x+=1            
        return res
        
**using-ascii**
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''   
        x=0                                 
        while x<len(s):
            if (x+2)<len(s) and s[x+2]=='#':
                res+=chr(int(s[x:x+2])+96)
                x+=3
            else: 
                res+=chr(int(s[x])+96)    
                x+=1
        return res
