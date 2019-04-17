#peak element is greater than rest of other:
#example For example, for input array {5, 10, 20, 15}, 20 is the only peak element.
#For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90.
def peakElement(a, l, r, n):
    mid= int(l + (r-l)/2)
    #find the peak element o exit from loop
    if((mid==0 or a[mid-1]<= a[mid]) and (mid == n-1 or a[mid+1]<= a[mid])):
    #return the index of peak element. Toreturn the peak element do: return a[mid]    
        return mid
    elif(mid>0 or a[mid-1]> a[mid]):
        return peakElement(a, l, mid-1, n)
    else:
        return peakElement(a, mid+1, r, n)
    
def findPeak(arr, n):

    return peakElement(arr, 0, n - 1, n)


# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
