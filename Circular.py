#  File: Circular.py
#  Description: Hot potato cirular list
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:10/25/2016
#  Date Last Modified:10/28/2016

class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER


class CircularList(object):

   def __init__ (self):
      self.head = Node(None)
      self.head.setNext(self.head)
      # the circular list constructor method.

   def add (self,item):
      temp = Node(item)
      first = self.head
      current = first

      while current.getNext() != first:
         current = current.getNext()

      temp.setNext(first)
      current.setNext(temp)
      # Insert an element in the list.  You will need this to build your
      # circular list from the data strings in the input file.  Hint:  figure
      # out which of the "add" methods we've discussed in class to use is
      # useful here and use it as a template for this method.

   def isEmpty (self):
      return (self.head.getNext() == self.head)
      # Return True if the cicrcular list is empty.
  
   def onlyOneNode (self):
      first = self.head
      current = first.getNext()
      if current.getNext() == first:
         return True
      else:
         return False
      
      # Return True if there is only one node left in the circular list.
      # This would be the "survivor".

   def remove (self,current,previous):
      pointer = current
      if self.onlyOneNode():
         return pointer
      #elif previous == self.head:
         
      
      else:
         pointer = current.getNext()
         previous.setNext(current.getNext())
         return pointer
      # Delete the node pointed to by "current" from the circular list.
      # Pass the "previous" pointer along for convenience.  This method
      # would only be called if there are at least 2 nodes in the list.
      # Return a pointer to the node immediately following the deleted
      # one.  Hint:  be sure to correctly handle the case where you delete
      # the first node in the circular list.

   def __str__ (self):
      first = self.head
      current = first.getNext()
      count = 1
      string = ""
        
      while current != first:
         if count % 10 != 0 :
            count += 1
            string += current.getData() + " "
         else:
            count += 1
            string += current.getData() + "\n"
         current = current.getNext()

      return string
      # Return a string representation of the circular list.  It should
      # include line breaks after every ten elements in the list.

def HotPotato(List,num):

   count = 0
   first = List.head
   previous = first
   current = first.getNext()
   print("In this Game n =",num)
   print("The Current List:",List)
   pause = input("pausing. . .")
   while not List.onlyOneNode():
      print("\n")
      count += 1
      if List.isEmpty():
         print("List is Empty!")
         break
      
      for i in range(num-1):  #goes through list to remove a name      
         if current.getNext() != first:
            previous = current
            current = current.getNext()            
         else:
            previous = current.getNext()
            current = previous.getNext()
      if current == first:
         previous = current
         current = current.getNext()
         
      print("Iteration Number:",str(count))
      print("Deleting:",current.getData())
      current = List.remove(current,previous)
      print("Updated List:",List)
      #pause = input("pausing. . .") #paused added to debug/test
      


   print("The sole survivor is:",List)
     
     
   

def main():
   f = open("HotPotatoData.txt")
   line = f.readline()
   while line != "":      
      List = CircularList()
      text = line.split()
      for x in range(0,int(text[0])):
         name = f.readline()
         List.add(name.rstrip())
      HotPotato(List,int(text[1]))
      line = f.readline()
      



main()
