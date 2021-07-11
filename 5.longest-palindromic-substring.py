#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        length = len(s)
        for i in range(length):
            curLen = 1
            startIdx = endIdx = i
            for j in range(1, length):
                leftIdx = i - j
                rightIdx = i + j
                if leftIdx < 0 or rightIdx > (length - 1):
                    break
                if s[leftIdx] != s[rightIdx]:
                    break
                curLen += 2
                startIdx = leftIdx
                endIdx = rightIdx
            if curLen > maxLen:
                maxLen = curLen
                resStart = startIdx
                resEnd = endIdx

            curLen = 0
            startIdx = endIdx = i
            for j in range(0, length):
                leftIdx = i - j
                rightIdx = i + j + 1
                if (leftIdx < 0) or (rightIdx > length - 1):
                    break
                if s[leftIdx] != s[rightIdx]:
                    break
                curLen += 2
                startIdx = leftIdx
                endIdx = rightIdx
            if curLen > maxLen:
                maxLen = curLen
                resStart = startIdx
                resEnd = endIdx
        
        result = ""
        for idx in range(resStart, resEnd + 1):
            result+=s[idx]
        return result

def main():
    s = "abaabbaaBA"
    print(Solution().longestPalindrome(s))

if __name__ == "__main__":
    main()
        
# @lc code=end

