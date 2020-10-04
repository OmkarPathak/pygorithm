"""
Given two strings, A and B. Find minimum number of edits required to convert 
A to B. Following are the allowed operations(edits) :

1. Insert(Insert a new character before or after any index i of A)
2. Remove(Remove the charater at the ith index of A)
3. Replace(Replace the character at ith indedx of A to any other character
            (possibly same))

Cost of all the operations are equal.

Time Complexity : O(M X N)
Space Complexity : O(M X N), where M and N are the lengths of A and B
                    respectively.
"""
 
def edit_distance(str1, str2): 
    """
    :param str1: string
    :param str2: string
    :return: int
    """
    m = len(str1)
    n = len(str2)

	# Create a table to store results of subproblems 
    dp = [ [0 for x in range(n + 1)] for x in range(m + 1) ]
	
    """
    dp[i][j] : contains minimum number of edits to convert str1[0...i] to str2[0...j]
    """

	# Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 

            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j # Min. operations = j 

            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i # Min. operations = i 

            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 

            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],	 # Insert 
                                    dp[i-1][j],	 # Remove 
                                    dp[i-1][j-1]) # Replace 


    return dp[m][n] 