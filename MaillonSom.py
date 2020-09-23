# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 07:28:25 2020

@author: cuna
"""
 

class Maillon :
    
    def __init__(self, valeur) :
        self.val=valeur
        self.suiv = None

class LinkedList : 
    
    def __init__(self):
        self.head = None
        
    def appendLast(self, data ):
        newCel = Maillon(data)
        
        if( self.head == None): 
            self.head = newCel
            return
        p = self.head
         
        while p.suiv :
           p = p.suiv
          
        p.suiv = newCel
        
    def printList(self): 
       cur_node = self.head
       while cur_node:
            print(cur_node.val)
            cur_node = cur_node.suiv
    

    def lenList(self): 
       cur_node = self.head
       cpt = 0
       while cur_node:
            cpt+=1
            cur_node = cur_node.suiv
       return cpt
   
    def isEmpty(self):
        return self.head == None
        
    def delLast(self, key):

        cur_node = self.head

        if cur_node and cur_node.val == key:
            self.head = cur_node.suiv
            cur_node = None
            return

        prev = None 
        while cur_node :
            prev = cur_node
            cur_node = cur_node.suiv

        if cur_node is None:
            return 

        prev.suiv = cur_node.suiv
        cur_node = None
    


 
#        
linkedList = LinkedList()
print('----isEmpty-----')
print(linkedList.isEmpty())

linkedList.appendLast(1)
linkedList.appendLast(2)
linkedList.appendLast(3)
linkedList.appendLast(4)
linkedList.appendLast(3)
print('------List-----')
linkedList.printList() 
