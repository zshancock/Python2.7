## A merchant has a shelf with 4 boxes - she wants to count the number of swaps to either sort her shelf in either reverse order
## order. For example, the boxes are on the shelf ordered 1,3,2,4 -- the result is 1,2,3,4 with one swap.


# count swaps for sorting for normal sorting order(i.e 1,2,3,4)

def normorder_swaps(xlist):
    xcount = 0
    for i in range(len(xlist)):
        for j in range(1, len(xlist)-i):
            if xlist[j-1] > xlist[j]:
                xcount += 1
                xlist[j-1], xlist[j] = xlist[j], xlist[j-1]
    return  xcount

# count swaps for sorting for reverse sorting order(i.e 4,3,2,1)

def revorder_swaps(ylist):
    ycount = 0
    for i in range(len(ylist)):
        for j in range(1, len(ylist)-i):
            if ylist[j-1] < ylist[j]:
                ycount += 1
                ylist[j-1], ylist[j] = ylist[j], ylist[j-1]
    return  ycount


# combine two functions for a single function that returns the minimum
# between them (i.e. the minimum swaps to obtain either order).

def lowest_swaps(zlist):

    z_copy = list(zlist)
    a = normorder_swaps(zlist)
    b = revorder_swaps(z_copy)

    if a > b:
        return('Target Order -> ' + str(sorted(zlist, reverse=True)) + ' with ' + str(b) +
               ' Steps.')
    elif a < b:
        return('Target Order -> ' + str(sorted(zlist)) + ' with ' + str(a) +
               ' Steps.')
    elif a == b:
        return('Target Order -> ' + str(sorted(zlist)) + ' with ' + str(a) +
               ' Steps.')
    else:
        return('Failed.')
    

# test on three scenarios #

# Scenario 1 - correct answer is 1 swap for this list (end order is 8,5,2,1)

print(5,8,2,1)
print(lowest_swaps([5,8,2,1]))

# Scenario 2 - correct answer is 2 swaps for this list (end order is 1,2,5,8)

print(2,1,8,5)
print(lowest_swaps([2,1,8,5]))

# Scenario 3 - correct answer is 1 swap for this list (end order is 1,2,5,8)

print(1,5,2,8)
print(lowest_swaps([1,5,2,8]))
