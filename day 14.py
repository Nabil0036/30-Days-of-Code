
        self.maximumDifference = 0
	# Add your code here
    def computeDifference(self):
        dif=[]
        for i in self.__elements:
            j=0
            while j< len(self.__elements):
                q=abs(i-self.__elements[j])
                dif.append(q)
                j+=1
        self.maximumDifference= max(dif)
