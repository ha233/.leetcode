#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
from typing import List

# @lc code=
class Solution:
    def findCandidates(self, pos: int, n: int) -> List[int]:
        candidates = []

        if (pos == 0):
            for i in range(2**n):
                candidates.append(i)
            return candidates
        
        prevNum = self.result[pos-1]
        for i in range(n):
            newNum = prevNum ^ (1 << i)
            if self.usedNum[newNum] == 0:
                candidates.append(newNum)
        
        return candidates
        
    def backTrack(self, pos: int, n: int) -> bool:
        if pos == 2**n:
            for i in range(n):
                if (self.result[0] ^ (1 << i)) == self.result[2**n - 1]:
                    # print("found!! pos = {}, n = {}".format(pos, n))
                    return True 
            return False
        
        candidates = self.findCandidates(pos, n)
        if not candidates:
            return False

        for num in candidates:
            self.result.append(num)
            self.usedNum[num] = 1
            ret = self.backTrack(pos + 1, n)
            if (ret == True):
                return True
            else:
                self.result.pop()
                self.usedNum[num] = 0
        
        return False

    # def grayCode(self, n: int) -> List[int]:
    #     self.usedNum = [0 for i in range(2**n)]
    #     self.result = []
    #     self.backTrack(0, n)
    #     return self.result

    def grayCode(self, n: int) -> List[int]:
        self.usedNum = [0 for i in range(2**n)]
        self.result = [0]
        self.usedNum[0] = 1
        for i in range(1, 2**n):
            prevNum = self.result[i-1]
            for j in range(n):
                candidate = prevNum ^ (1 << j)
                if self.usedNum[candidate] == 0:
                    self.result.append(candidate)
                    self.usedNum[candidate] = 1
                    break
        return self.result

def main():
    import sys
    sys.setrecursionlimit(100000)
    result = Solution().grayCode(2)
    print (result)

if __name__ == "__main__":
    main()
# @lc code=end

