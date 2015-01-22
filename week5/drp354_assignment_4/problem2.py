################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################


# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
  biggerNumber = []
  for token in L:
    if token > v:
      biggerNumber.append(token)
    else:pass
  return len(biggerNumber)


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
  for idx,token in enumerate(L):
    if token > v:
      return len(L[idx:])
    else:
	  n = 0
  return n 
  

# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
  L_length =len(L)
  lo = 0
  hi = L_length
  if v >= L[hi-1]:
    return 0
  elif v < L[0]:
    return L_length
  else:
  #binary search algorithm
    while lo <= hi:
      mid = lo + (hi-lo)/2
      if L[mid] == v:
        break
      elif L[mid] < v: 
        lo = mid+1
      else:
        hi = mid-1
    #Checking repeated numbers
    if mid < (L_length-1):
      while (L[mid+1] == L[mid]):
        mid+=1
        if mid == (L_length-1):
          return 0
    else:
      return 0
  return len(L[(mid+1):])


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  n = searchGreaterBinSearch(L,v1) - searchGreaterBinSearch(L,v2)
  return n

