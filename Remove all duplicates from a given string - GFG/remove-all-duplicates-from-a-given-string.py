#User function Template for python3
class Solution:

	
	def removeDuplicates(self,str):
	    
	    x=set(str)
	    p=''
	    for i in str:
	        if(i in x):
	            p+=i
	            x.remove(i)
	        else:
	            pass
	    return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends