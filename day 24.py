

    def removeDuplicates(self,head):
        #Write your code here
        cur = head
        li=[]
        while cur.next:
            last = cur
            li.append(cur.data)
            li = list(set(li))
            cur = cur.next
            #print(li)
            if cur.data in li:
                last.next = cur.next
                cur = None
                
                self.removeDuplicates(head)
                return head
        return head
             




