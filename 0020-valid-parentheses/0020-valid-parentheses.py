class Solution:
    def isValid(self, s: str) -> bool:
        openi =[  "(" , "{" ,"["  ]
        close=[")" ,"}" ,"]" ]
        stack=[]
        for i in range(len(s)):
            if(s[i] in openi):
                stack.append(s[i])
            elif(s[i] in close):
                pos=close.index(s[i])
                if(len(stack)>0 and (openi[pos]==stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
        
                