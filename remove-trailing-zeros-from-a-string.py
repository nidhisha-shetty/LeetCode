'''
P.S: Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.
'''

#Solution:
class Solution(object):
  def removeTrailingZeros(self, num):
      """
      :type num: str
      :rtype: str
      """
      num = int(num)
      while num%10 == 0:
          num = num // 10
      return str(num)
