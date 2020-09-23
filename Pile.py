import Sommet
 

class Maillon :
    
    def __init__(self, som :Sommet) :
        self.som  = som
        self.suiv = None

class Pile : 
    
    def __init__(self):
        self.head = None
        
    def empiler(self, data : Sommet):
        newCel = Maillon(data)
        
        if( self.head == None): 
            self.head = newCel
            return
      
        newCel.suiv  = self.head
        self.head = newCel
        

    def printList(self): 
       cur_node = self.head
       while cur_node:
            print(cur_node.som.num)
            cur_node = cur_node.suiv
    

 
    def isEmpty(self):
        return self.head == None
        
    def depiler(self):

        cur_node = self.head

        if cur_node is None:
            return 
        
        self.head = self.head.suiv
        del cur_node.suiv
        return cur_node

  
 
#        
linkedList = Pile()
print('----isEmpty-----')
print(linkedList.isEmpty())

linkedList.empiler(Sommet.Sommet(1,0,[]))
linkedList.empiler(Sommet.Sommet(2,0,[]))
linkedList.empiler(Sommet.Sommet(3,0,[]))
linkedList.empiler(Sommet.Sommet(4,0,[]))
 
linkedList.printList()
linkedList.depiler()
print('-------------')
linkedList.printList()