# Important Notes:
# A. Union-find disjoint set for verifying connectivity
# B. Sets are numbered 1 to n
# C. Every union operation will increase the edge count
# D. There is "grandparent" path compression for every non-root set in find

def find(s1, s2):
    return getRoot(s1) == getRoot(s2)
        
def getRoot(s):
    global parent
    currSet = s
    while parent[currSet] != currSet:
        parent[currSet] = parent[parent[currSet]]
        currSet = parent[currSet]
    parent[s] = currSet
    return currSet
        
def union(s1, s2):
    global components
    global edges
    global parent
    global rank
    edges += 1
    if find(s1, s2):
        return
    rootS1, rootS2 = getRoot(s1), getRoot(s2)
    if rank[rootS1] > rank[rootS2]:
        parent[rootS2] = rootS1
        rank[rootS1] += rank[rootS2]
    else:
        parent[rootS1] = rootS2
        rank[rootS2] += rank[rootS1]
    components -= 1

n = 1

components, edges = n, 0
parent = [i for i in xrange(n+1)]
rank = [1 for i in xrange(n+1)]
