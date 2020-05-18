

    def levelOrder(self,root):
        #Write your code here
        h= height(root)
        for i in range(1,h+1):
            printGivenLevel(root,i)
    
    


def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print (root.data,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1)           

