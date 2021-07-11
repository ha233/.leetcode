#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        right = 0
        length = len(s)
        charLoc = {}
        while (right < length):
            character = s[right]
            if character in charLoc:
                left = max(left, charLoc[character] + 1)
            charLoc[character] = right
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
                
def main():
    s = "aabebcazxcba"
    print(Solution().lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()
        
# @lc code=end

