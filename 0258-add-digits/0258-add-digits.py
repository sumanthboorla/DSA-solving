class Solution:
    def addDigits(self, num: int) -> int:
        sum1=0
        if(num<10):
            return num
        else:
            while(num>=10):
                sum1=0
                while(num>0):
                    x=num%10
                    sum1+=x
                    num=num//10
                num=sum1
            return sum1
        