

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        i=1
        int_n = int(n)
        li=[]
        while i<=int_n:
            h=int_n%i
            if h==0:
                li.append(i)
            else:
                pass
            i+=1
        return sum(li)
