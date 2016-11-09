'''
    Given an array of integers, a, find the maximum difference between
    two elements, a[i] and a[j], given the following conditions below:
    
    1. i < j
    2. a[j] - a[i] > 0

    Return -1 if there is no such maximum difference.
'''

def maxDifference(a):
    length = len(a)
    lastInd = length - 1
    minInd, minVal = -1, 10**6 + 1
    maxInd, maxVal = -1, -1 * minVal
    maxIndPtr, prevMaxInd = maxInd, maxInd
    maxDiff = -1
    while maxIndPtr < lastInd:
        startMaxInd = maxInd + 1
        newMaxInd, newMaxVal = getMaxRight(a, startMaxInd)
        if newMaxVal > maxVal:
            maxInd, maxVal = newMaxInd, newMaxVal
        
        startMinInd = prevMaxInd + 1
        newMinInd, newMinVal = getMinLeft(a, startMinInd, maxInd)
        if newMinVal < minVal:
            minInd, minVal = newMinInd, newMinVal
            
        if maxInd > minInd:
            maxDiff = max(maxDiff, maxVal - minVal)

        print("Index:\t%d\tValue:\t%d" % (minInd, minVal))
        print("Index:\t%d\tValue:\t%d" % (maxInd, maxVal))
        
        maxIndPtr = max(maxIndPtr, maxInd) + 1
        print("Index:\t%d" % (maxIndPtr))
        prevMaxInd = maxInd
        
    return maxDiff

def getMinLeft(xs, startInd, endInd):
    i = startInd
    minInd, minVal = -1, 10**6 + 1
    while i <= endInd:
        if xs[i] < minVal:
            minInd, minVal = i, xs[i]
        i += 1
    return (minInd, minVal)
            
def getMaxRight(xs, startInd):
    i = startInd
    maxInd, maxVal = -1, -1 * (10**6 + 1)
    for elem in xs:
        if elem >= maxVal:
            maxInd,maxVal = i, elem
        i += 1
    return (maxInd, maxVal)

a = [7, 2, 3, 10, 2, 4, 8, 1]
b = [6, 7, 9, 5, 6, 3, 2]
print("Answer:\t%d" % maxDifference(a))
print()
print("Answer:\t%d" % maxDifference(b))

'''
maxInd, maxVal = getMaxRight(a, 0)
print("Index: %d, Value: %d" % (maxInd, maxVal))
minInd, minVal = getMinLeft(a, 0, maxInd-1)
print("Index: %d, Value: %d" % (minInd, minVal))
print()
maxInd, maxVal = getMaxRight(b, 0)
print("Index: %d, Value: %d" % (maxInd, maxVal))
minInd, minVal = getMinLeft(b, 0, maxInd-1)
print("Index: %d, Value: %d" % (minInd, minVal))
'''
