#  File: LinkedList.py
#  Description: ER Simulation
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:10/19/2016
#  Date Last Modified:10/21/2016

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

class LinkedList():

    def __init__(self):
      self.head = None
    
    def __str__ (self):
        current = self.head
        count = 1
        string = ""
        
        while current != None:
            if count % 10 != 0 :                
                count += 1
                string += current.getData() + " "
            else:                
                count += 1
                string += current.getData() + "\n"
            current = current.getNext()
        return string
        
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements
  
    def addFirst (self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
     # Add an item to the beginning of the list

    def addLast (self, item):
        current = self.head
        previous = None
        
        while current != None:
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        
     # Add an item to the end of a list

    def addInOrder (self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.

    def getLength (self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count
     # Return the number of items in the list 
     
    def findUnordered (self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.

    def findOrdered (self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list.

    def delete (self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                if current.getNext() == None and item != None:
                    found = False
                    break
                else:
                    current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext() )

        return found
    
     # Delete an item from an unordered list
     #    if found, return True; otherwise, return False

    def copyList (self):
        current = self.head
        ListCopy = LinkedList()

        while current != None:            
            ListCopy.addLast(current.getData())
            current = current.getNext()

        return ListCopy
        
        
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements

    def reverseList (self):
        current = self.head
        RevList = LinkedList()

        while current != None:            
            RevList.addFirst(current.getData())
            current = current.getNext()

        return RevList
        
        
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.

    def orderList (self):
        orderList = LinkedList()
        current = self.head     

        while current != None:
            orderList.addInOrder(current.getData())
            current = current.getNext()
            
        return orderList
        
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.

    def isOrdered (self):
        ordered = True
        current = self.head
        previous = None

        if current == None:
            return ordered
        else:
            previous = current
            current = current.getNext()
                
        while ordered and current != None:
            if previous.getData() > current.getData():
                ordered = False
            else:
                previous = current
                if current.getNext() == None:
                    break
                else:
                    current = current.getNext()
                
                
            

        return ordered 
        
     # Return True if a list is ordered in ascending (alphabetical)
     #    order, or False otherwise

    def isEmpty (self):
        return self.head == None
     # Return True if a list is empty, or False otherwise

    def mergeList (self, b):
        Merger = LinkedList()
        currenta = self.head
        currentb = b.head

        if currenta == None:
            Merger = orderList(b)
        elif currentb == None:
            Merger = orderList(self)
        else:
            Merger.addFirst(currenta.getData())
            Merger.addInOrder(currentb.getData())
            currenta = currenta.getNext()
            currentb = currentb.getNext()
        
        while currenta != None or currentb != None:
            if currenta == None:
                Merger.addInOrder(currentb.getData())
            elif currentb == None:
                Merger.addInOrder(currenta.getData())
            else:
                Merger.addInOrder(currenta.getData())
                Merger.addInOrder(currentb.getData())
                currenta = currenta.getNext()
                currentb = currentb.getNext()
            

        return Merger
        
        
     # Return an ordered list whose elements consist of the 
     #    elements of two ordered lists combined.

    def isEqual (self, b):
        currenta = self.head
        currentb = b.head
        equal = True

        while equal:
            if currenta == None and currentb == None:
                break
            elif (currenta != None and currentb == None) or (currenta == None and currentb != None):
                equal = False
            else:
                if currenta.getData() == currentb.getData():
                    currenta = currenta.getNext()
                    currentb = currentb.getNext()
                else:
                    equal = False                 
            
        return equal 
     # Test if two lists are equal, item by item, and return True.

    def removeDuplicates (self):
        Copy = self.copyList()
        pointer = Copy.head        
        previous = None

        while pointer != None:
            current = pointer
            while current != None:
                previous = current
                current = current.getNext()
                if current == None:
                    break
                if current.getData() == pointer.getData():
                    temp = current.getNext()
                    previous.setNext(temp)
            pointer = pointer.getNext()

        return Copy
    
     # Remove all duplicates from a list, returning a new list.
     #    Do not change the order of the remaining elements.


# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
