#This code is contributed by Sakshi-Mallick

import math 
  
def jumpSearch( a , x , n ): 
      
    # Finding block size to be jumped 
    step = math.sqrt(n) 
      
    # Finding the block where element is 
    # present (if it is present) 
    pre = 0
    while ar[int(min(step, n)-1)] < x: 
        pre = step 
        step += math.sqrt(n) 
        if pre >= n: 
            return -1
      
    # Doing a linear search for x in  
    # block beginning with prev. 
    while a[int(prev)] < x: 
        pre += 1
          
        # If we reached next block or end  
        # of array, element is not present. 
        if pre == min(step, n): 
            return -1
      
    # If element is found 
    if a[int(pre)] == x: 
        return pre
      
    return -1
  
# Driver code to test function 
a = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 55
n = len(a) 
  
# Find the index of 'x' using Jump Search 
index = jumpSearch(arr, x, n) 
  
# Print the index where 'x' is located 
print("Number" , x, "is at index" ,"%.0f"%index) 
