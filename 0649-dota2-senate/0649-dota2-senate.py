class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        length=len(senate)
        R_array=[i for i in range(length) if senate[i]=="R"]
        D_array=[j for j in range(length) if senate[j]=="D"]
        
        while(R_array and D_array):
            i=R_array.pop(0)
            j=D_array.pop(0)
            if(i<j):
                R_array.append(length+i)
            else:
                D_array.append(length+j)
        return 'Radiant' if R_array else "Dire"
    
        

            
        
            
                
        