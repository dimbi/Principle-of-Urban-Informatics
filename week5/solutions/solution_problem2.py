import random

# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
  greaterThanV = 0
  for elm in L:
    if elm > v:
      greaterThanV += 1
  return greaterThanV


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
  notGreater = 0
  for elm in L:
    if elm > v:
      break
    notGreater += 1
  return len(L) - notGreater


# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
  lengthOfL = len(L)

  # Continues search while [imin,imax] is not empty.
  imin = 0
  imax = lengthOfL # imax always points to end of array (non inclusive).

  while imin < imax:
    # Computes midpoint for roughly equal partition.
    imid = int((imin + imax) / 2)

    if v == L[imid]:   # v found at index imid.
      break
    elif v < L[imid]:  # Changes imax index to search lower subarray.
      imax = imid
    else:              # Changes imin index to search upper subarray.
      imin = imid + 1
 
  if imin < imax:      # Found v
    # Handles repetitions: makes imid point to 1st greater than v.
    while imid < lengthOfL and v == L[imid]:
      imid += 1
    # Return number of elements greater than v.
    return lengthOfL - imid
  else:
    # The possible state the binary search above
    # can stop when the element is not found is L[imax] > v.
    # Since we want to return the number of greater than v,
    # v does not need to be in L.
    return lengthOfL - imax



# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  return searchGreaterBinSearch(L, v1) - searchGreaterBinSearch(L, v2)



def testBinSearch():
  repetitions = 100
  n = 10000

  for c in range(repetitions):
    L = sorted([random.randint(0,100) for i in range(n)])
    v1 = 1
    v2 = 0
    while v1 > v2:
      v1 = random.randint(0, 100)
      v2 = random.randint(0, 100)
    gNotSorted = searchGreaterNotSorted(L, v1)
    bSorted = searchGreaterBinSearch(L, v1)
    if gNotSorted != bSorted:
      print gNotSorted, bSorted, L

def testInRange():
  repetitions = 100
  n = 10000

  for c in range(repetitions):
    L = sorted([random.randint(0,100) for i in range(n)])
    v1 = 1
    v2 = 0
    while v1 > v2:
      v1 = random.randint(0, 100)
      v2 = random.randint(0, 100)

    gNotSorted = searchGreaterSorted(L, v1) - searchGreaterSorted(L, v2)
    inRangeSorted = searchInRange(L, v1, v2)
    if gNotSorted != inRangeSorted:
      print gNotSorted, inRangeSorted, v1, v2, L

  # Some examples.
  L = [0, 2, 2, 2, 3, 4, 5]
  v1  = 1
  v2 = 2
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)
  v1  = 0
  v2 = 5
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)
  v1  = 5
  v2 = 6
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)
  v1  = 4
  v2 = 6
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)

  # Examples in the assignment.
  L = [1, 3, 4, 5, 5]
  v1 = 1
  v2 = 2
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)

  L =  [-3, 0, 2, 2, 4, 5]
  v1 = -1
  v2 = 5
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)

  L = [-1, 0, 1, 1, 2, 10, 10]
  v1 = 2
  v2 = 11
  print L, '|' + str(v1) + ' < x <= ' + str(v2) + '| = ', searchInRange(L, v1, v2)

  
if __name__ == "__main__":
  #print 'testing binSearch...'
  #testBinSearch()

  print 'testing inRange...'
  testInRange()
