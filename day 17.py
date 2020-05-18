#Write your code here
class Calculator():
    def power(self,n,p):
        self.n = n
        self.p = p
        if self.n>=0 and self.p>=0:
            return self.n**self.p
        else:
            return ValueError("n and p should be non-negative")

