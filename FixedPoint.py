#fixed point is if array value is same as index value
#Input: arr[] = {-10, -5, 0, 3, 7}
 # Output: 3  // arr[3] == 3
  #
  # Input: arr[] = {0, 2, 5, 8, 17}
  # Output: 0  // arr[0] == 0
  #
  #
  # Input: arr[] = {-10, -5, 3, 4, 7, 9}
  # Output: -1  // No Fixed Point
def fixedPoint(a, low, high):
      if low<=high:
          mid = int(low + (high-low)/2)
          if a[mid]==mid:
              return mid
          elif a[mid]<mid:
              return fixedPoint(a, mid+1,high)
          else:
              return fixedPoint(a, low, mid-1)
          return -1

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(fixedPoint(arr, 0, n-1)))
