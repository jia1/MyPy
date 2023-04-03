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

# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        def bs(xs, t):
            i1, i2 = 0, len(xs)-1
            while i1 <= i2:
                i = (i1+i2) // 2
                if xs[i] == t:
                    return i
                if xs[i] < t:
                    i1 = i+1
                else:
                    i2 = i-1
            return -1

        is_rotated = nums[0] > nums[-1]
        if not is_rotated:
            return bs(nums, target)

        # Peak-finding where the peak is defined as: xs[x-1] < xs[x] (i.e. peak) > xs[x+1]
        def peak(xs, j1, j2):
            i1, i2 = j1, j2
            while i1 <= i2:
                i = (i1+i2) // 2
                if (0 <= i < last and xs[i] > xs[i+1]):
                    return i+1
                elif (0 < i <= last and xs[i-1] > xs[i]):
                    return i
                else:
                    return max(peak(xs, j1, i-1), peak(xs, i+1, j2))
            return -1

        last = len(nums)-1
        i1, i2 = peak(nums, 0, last), last
        j = bs(nums[i1:i2+1], target)
        if j > -1:
            return i1 + j
        return bs(nums[:i1+1], target)

# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1: return matrix[0]
        m, n = len(matrix), len(matrix[0])
        l = m*n
        minRow, maxRow, minCol, maxCol = 0, m, 0, n
        output = []
        direction = 1
        while len(output) < l and (minRow < maxRow or minCol < maxCol):
            print(minRow, maxRow, minCol, maxCol)
            match direction:
                case 1:
                    output.extend(matrix[minRow][minCol:maxCol])
                    minRow += 1
                case 2:
                    column = [row[maxCol-1] for row in matrix[minRow:maxRow]]
                    output.extend(column)
                    maxCol -= 1
                case 3:
                    output.extend(matrix[maxRow-1][minCol:maxCol][::-1])
                    maxRow -= 1
                case 4:
                    column = [row[minCol] for row in matrix[minRow:maxRow]][::-1]
                    output.extend(column)
                    minCol += 1
            direction = 1 + direction % 4
        return output

# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def climb(x):
            if x <= 2:
                return x
            if x in m:
                return m[x]
            m[x-2] = climb(x - 2)
            m[x-1] = climb(x - 1)
            m[x] = m[x-1] + m[x-2]
            return m[x]
        return climb(n)

# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i1, i2 = 0, m-1
        j = n // 2
        while (i2-i1) > 1:
            i = (i1+i2) // 2
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i2 = i
            else:
                i1 = i
        c11, c12, c21, c22 = 0, n-1, 0, n-1
        while c11 <= c12:
            c = (c11+c12) // 2
            if matrix[i1][c] == target:
                return True
            if matrix[i1][c] > target:
                c12 = c-1
            else:
                c11 = c+1
        while c21 <= c22:
            c = (c21+c22) // 2
            if matrix[i2][c] == target:
                return True
            if matrix[i2][c] > target:
                c22 = c-1
            else:
                c21 = c+1
        return False

# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            for i in range(n):
                nums1[i] = nums2[i]
        i1 = m-1
        i2 = n-1
        i3 = m+n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i3] = nums1[i1]
                i1 -= 1
                i3 -= 1
            else:
                nums1[i3] = nums2[i2]
                i2 -= 1
                i3 -= 1
        for j in range(i2, -1, -1):
            nums1[j] = nums2[j]

# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def visit(val):
            traversal.append(val)
        def traverse(root):
            if root:
                left_subtree = traverse(root.left)
                visit(root.val)
                right_subtree = traverse(root.right)  
        traverse(root)
        return traversal

# 100. Same Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None:
                return True
            return False
        if q is None:
            if p is None:
                return True
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 107. Binary Tree Level Order Traversal II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        level = []
        if root is not None:
            level.append(root)
        while level:
            traversal.append(list(map(lambda node: node.val, level)))
            nextLevel = []
            for currNode in level:
                if currNode.left is not None:
                    nextLevel.append(currNode.left)
                if currNode.right is not None:
                    nextLevel.append(currNode.right)
            level = nextLevel
        traversal.reverse()
        return traversal

# 110. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        m = {}
        def height(tree):
            if tree in m:
                return m[tree]
            if tree is None:
                return 0
            if tree.left is None and tree.right is None:
                return 1
            m[tree] = 1 + max(height(tree.left), height(tree.right))
            return m[tree]
        def balanced(tree):
            if tree is None:
                return True
            if abs(height(tree.left) - height(tree.right)) > 1:
                return False
            return balanced(tree.left) and balanced(tree.right)
        return balanced(root)

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [c.lower() for c in s if c.isalnum()]
        h = len(x) // 2
        for i in range(h):
            if x[i] != x[-1-i]:
                return False
        return True

# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                return [l+1,r+1]

# 171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((26**i * (ord(c) - 64)) for i, c in enumerate(s[::-1]))

# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return nums
        l = len(nums)
        if l == 1:
            return nums
        r = k % l
        if not r:
            return nums
        h = l // 2
        rotateRight = True
        if r > h:
            rotateRight = False
            r = l - r
        if rotateRight:
            toMove = nums[l-r:]
            for i in range(l-r-1, -1, -1):
                nums[r+i] = nums[i]
            for j in range(r):
                nums[j] = toMove[j]
        else:
            toMove = nums[:r]
            for i in range(l-r):
                nums[i] = nums[r+i]
            for j in range(r):
                nums[l-r+j] = toMove[j]

# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        l = len(nums)
        def r(i):
            if i >= l:
                return 0
            if l - i == 1:
                return nums[i]
            if i in m:
                return m[i]
            do = nums[i] + r(i+2)
            dont = r(i+1)
            m[i] = max(do, dont)
            return m[i]
        return r(0)

# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(xs):
            ds = list(str(xs))
            sqs = map(lambda d: int(d)**2, ds)
            return sum(sqs)
        x, history = n, [n]
        while True:
            x = calc(x)
            if x == 1:
                break
            if x in history:
                ix = history.index(x)
                cycleLength = len(history) - ix
                expectedCycle = history[ix:]
                potentialCycle = [x]
                y = x
                for _ in range(cycleLength - 1):
                    y = calc(y)
                    potentialCycle.append(y)
                if potentialCycle == expectedCycle:
                    break
            history.append(x)
        return x == 1

# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        p = {}
        l = len(nums)
        def r(i, robFirst):
            if i >= l:
                return 0
            if l - i == 1:
                return 0 if robFirst else nums[i]
            if robFirst:
                c = m
            else:
                c = p
            if i in c:
                return c[i]
            do = nums[i] + r(i+2, robFirst)
            dont = r(i+1, robFirst)
            c[i] = max(do, dont)
            return c[i]
        if not nums:
            return 0
        return max(r(1, False), nums[0] + r(2, True))

# 226. Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None or node.left is None and node.right is None:
                return node
            node.left, node.right = invert(node.right), invert(node.left)
            return node
        return invert(root)

# 274. H-Index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for i, c in enumerate(sorted(citations, reverse=True), 1):
            if c < i:
                break
            h += 1
        return h


# 278. First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        n1 = 1
        n2 = n
        lastGood = n1
        firstBad = n2
        while (firstBad - lastGood) > 1:
            i = (n1 + n2) // 2
            if isBadVersion(i):
                firstBad = i
                n2 = i - 1
            else:
                lastGood = i
                n1 = i + 1
        return lastGood if isBadVersion(lastGood) else firstBad

# 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        h2, h3 = None, None
        p1, p2 = head, None
        isEven = True
        while p1 is not None:
            if isEven:
                h2 = p1
            isEven = not isEven
            p1 = p1.next
        p1 = head
        isEven = True
        while p1 is not None and p1 != (h2 if h2.next is None else h2.next):
            n2 = p1.next
            if isEven:
                p1.next = n2.next if n2 is not None else None
            else:
                if h3 is None:
                    h3 = p1
                    p2 = p1
                else:
                    p2.next = p1
                    p2 = p2.next
                p2.next = None
            isEven = not isEven
            p1 = n2
        h2.next = h3
        return head

# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [t[0] for t in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[:k]]

# 437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        numPaths = [0]
        def traverse(tree, t):
            if tree is None:
                return
            test(tree, t)
            traverse(tree.left, t)
            traverse(tree.right, t)
        def test(tree, t):
            if tree is None:
                return
            if tree.val == t:
                numPaths[0] += 1
            test(tree.left, t - tree.val)
            test(tree.right, t - tree.val)
        traverse(root, targetSum)
        return numPaths[0]

# 461. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb = bin(x)[-1:1:-1]
        yb = bin(y)[-1:1:-1]
        i = 0
        hd = 0
        if len(xb) < len(yb):
            while i < len(xb):
                if xb[i] != yb[i]:
                    hd += 1
                i += 1
            while i < len(yb):
                if yb[i] == '1':
                    hd += 1
                i += 1
        else:
            while i < len(yb):
                if xb[i] != yb[i]:
                    hd += 1
                i += 1
            while i < len(xb):
                if xb[i] == '1':
                    hd += 1
                i += 1
        return hd

# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        m = {0: 0, 1: 1}
        def f(x):
            if x <= 1:
                return m[x]
            n1, n2 = x-1, x-2
            if n2 not in m:
                m[n2] = f(n2)
            if n1 not in m:
                m[n1] = f(n1)
            m[x] = m[n1] + m[n2]
            return m[x]
        return f(n)

# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def paths(tree, d):
            if tree is None:
                return (-1, d)
            l, r = paths(tree.left, d), paths(tree.right, d)
            d = max(d, l[0] + r[0])
            return (1 + max(l[0], r[0]), d)
        return paths(root, 0)[1]

# 621. Task Scheduler
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        s = c.items()
        ls = len(s)
        last = {k: -1 for k in c}
        t = []
        for _ in range(len(tasks)):
            s = sorted(s, key=lambda x: -x[1])
            ni, p = float('inf'), 0
            for j in range(ls):
                task, count = s[j]
                if not count:
                    break
                if last[task] < 0:
                    ni, p = 0, j
                    break
                nxt, cur = last[task] + n + 1, len(t)
                _ni = max(nxt - cur, 0)
                if _ni < ni:
                    ni, p = _ni, j
                    if not ni:
                        break
            t.extend(['idle' for _ in range(ni)])
            task, count = s[p]
            last[task] = len(t)
            t.append(task)
            s[p] = (task, count - 1)
        return len(t)

# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i1, i2 = 0, len(nums) - 1
        while i1 <= i2:
            i = (i1+i2) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i1 = i+1
            else:
                i2 = i-1
        return -1


# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m, n = {}, len(cost)
        def climb(i):
            if i >= n:
                return 0
            if n-i == 1:
                return cost[i]
            if i in m:
                return m[i]
            two = climb(i+2)
            one = climb(i+1)
            m[i] = cost[i] + min(one, two)
            return m[i]
        return min(climb(1), climb(0))

# 845. Longest Mountain in Array
class Solution:
    def longestMountain(self, A):
        maxCount = 0
        up = 0
        down = 0
        for i in range(len(A) - 1):
            j = i + 1
            if A[j] > A[i]:
                if not down:
                    up += 1
                else:
                    if up and down:
                        maxCount = max(maxCount, 1 + up + down)
                    up = 1
                    down = 0
            elif A[j] < A[i]:
                if up:
                    down += 1
                else:
                    if up and down:
                        maxCount = max(maxCount, 1 + up + down)
                    up = 0
                    down = 0
            else:
                if up and down:
                    maxCount = max(maxCount, 1 + up + down)
                up = 0
                down = 0
        if up and down:
            return max(maxCount, 1 + up + down)
        else:
            return maxCount

# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getHalf(x):
            return -(x // -2)
        if head.next is None:
            return head
        curr = head
        nodes = []
        for i in range(51):
            if curr == None:
                break
            nodes.append(curr)
            curr = curr.next
        l = 0
        while curr != None:
            l += 1
            curr = curr.next
        return nodes[(len(nodes) + l) // 2]

# 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f, r = set(), set()
        for i in range(m):
            for j in range(n):
                o = grid[i][j]
                match o:
                    case 1:
                        f.add((i, j))
                    case 2:
                        r.add((i, j))
        seen = set()
        def is_valid(c):
            x, y = c
            return c not in seen and 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        t = 0
        while r:
            if not f:
                break
            fringes = []
            for coord in r:
                seen.add(coord)
                i, j = coord
                nodes = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
                fringe = list(filter(is_valid, nodes))
                fringes.extend(fringe)
            f.difference_update(fringes)
            r = set(fringes)
            t += 1
        return t if not f else -1

# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        p = sorted(enumerate(map(lambda t: t[0] - t[1], costs)), key=lambda t: t[1])
        min_cost = 0
        for c in p[:n]:
            i = c[0]
            min_cost += costs[i][0]
        for c in p[n:]:
            i = c[0]
            min_cost += costs[i][1]
        return min_cost

# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        m = {0: 0, 1: 1, 2: 1}
        def t(x):
            if x <= 2:
                return m[x]
            y1, y2, y3 = x-1, x-2, x-3
            if y3 not in m:
                m[y3] = t(y3)
            if y2 not in m:
                m[y2] = t(y2)
            if y1 not in m:
                m[y1] = t(y1)
            m[x] = m[y1] + m[y2] + m[y3]
            return m[x]
        return t(n)

# 1706. Where Will the Ball Fall
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        numRows, numCols = len(grid), len(grid[0])
        answer = []
        for i in range(numCols):
            r, c = 0, i
            while r < numRows:
                if grid[r][c] == 1:
                    if c == numCols-1 or grid[r][c+1] == -1:
                        break
                    c += 1
                else:
                    if c == 0 or grid[r][c-1] == 1:
                        break
                    c -= 1
                r += 1
            answer.append(-1 if r < numRows else c)
        return answer

# 2131. Longest Palindrome by Concatenating Two Letter Words
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        longest = 0
        counterparts = {}
        for i in range(len(words)):
            word = words[i]
            if word in counterparts and counterparts[word] > 0:
                counterparts[word] -= 1
                longest += 4
            else:
                c = word[::-1]
                if c not in counterparts:
                    counterparts[c] = 0
                counterparts[c] += 1
        for word in counterparts:
            if not counterparts[word]:
                continue
            if word[0] == word[1]:
                longest += (counterparts[word] // 2) + 2
                break
        return longest
