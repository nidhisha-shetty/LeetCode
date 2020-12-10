'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order. Given the string (command), return the Goal Parser's interpretation of (command).
'''

#Solution
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res=""
        for x in range(len(command)):
            if command[x]=="G":
                res+="G"
            elif command[x]=="(" and command[x+1]==")":
                res+="o"
            elif command[x:x+4]=="(al)":
                res+="al"
        return res
            
