# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getArea(i1, i2):
            return (i2-i1) * min(height[i1], height[i2])
        v, i1, i2 = 0, 0, len(height) - 1
        while i2 > i1:
            v = max(getArea(i1, i2), v)
            if height[i1] < height[i2]:
                i1 += 1
            elif height[i1] > height[i2]:
                i2 -= 1
            else:
                i1 += 1
                i2 -= 1
        return v

# 17. Letter Combinations of a Phone Number
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        comb = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        return list(map(lambda c: ''.join(c), itertools.product(*list(map(lambda d: comb.get(d), digits)))))

# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            if c in m:
                stack.append(m[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack

# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p = []
        def permute(a, b, s):
            if not b:
                p.append(s)
                return
            if not a:
                p.append(s + b * ')')
                return
            if a < b:
                permute(a, b - 1, s + ')')
            permute(a - 1, b, s + '(')
        permute(n, n, '')
        return p
