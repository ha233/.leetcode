#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    MIN_INT = 0 - 2 ** 31
    MAX_INT = 2 ** 31 - 1

    def trimPrefix(self, s: str, length: int) -> int:
        idx = 0
        while idx < length:
            if ('0' <= s[idx] <= '9') or (s[idx] in ['+', '-']):
                break
            idx += 1

        return idx

    def convertStrToInt(self, s: str) -> int:
        num = 0
        length = len(s)
        
        for i in range(length):
            num += (int(s[length-1-i]) - int('0')) * (10 ** i)
        
        return num

    def myAtoi(self, s: str) -> int:
        length = len(s)
        startIdx = self.trimPrefix(s, length)
        if (startIdx >= length):
            return 0

        bNegative = False
        if s[startIdx] == '-':
            bNegative = True
            startIdx += 1
        elif s[startIdx] == '+':
            startIdx += 1

        numString = ""
        for idx in range(startIdx, length):
            if '0' <= s[idx] <= '9':
                numString += s[idx]
        
        number = self.convertStrToInt(numString)

        if bNegative:
            number = 0 - number

        number = max(number, self.MIN_INT)
        number = min(number, self.MAX_INT)

        return number
        
def main():
    print (Solution().myAtoi("-ab00887"))

if __name__ == "__main__":
    main()

# @lc code=end

