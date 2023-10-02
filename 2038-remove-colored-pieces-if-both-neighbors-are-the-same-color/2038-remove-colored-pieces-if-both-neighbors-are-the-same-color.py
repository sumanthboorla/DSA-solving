class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_score=0
        b_score=0
        for i in range(1,len(colors)-1):
            cur=colors[i]
            prev=colors[i-1]
            next_=colors[i+1]
            
            if cur=="A" and prev=="A" and next_ =="A":
                a_score+=1
            elif cur=="B" and prev=="B" and next_ =="B":
                b_score+=1
        return a_score>b_score
        