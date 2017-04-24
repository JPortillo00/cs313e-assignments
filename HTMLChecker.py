#  File: HTMLChecker.py
#  Description: Checks HTML files
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:10/5/2016
#  Date Last Modified:10/7/2016

class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

def getTag(file):   #Implementation of recommended getTag function was not used but was basis to complete createTagList
   txt = file.read(1)
   tag = ""
   while txt is not '>':
      if txt is '<':
         txt = file.read(1)
         while txt is not '>' and txt is not '' and txt is not " ":
            tag += txt
            txt = file.read(1)            
      else:
         txt = file.read(1)
   return tag
            
def createTagList(): #creates a list of all HTML tags in a file
   f = open("html.txt") 
   txt = f.read(1)
   taglist = []
   tag = ""
   while txt is not "": #This conditions was used on the basis that f.read() after reaching the end was ""
      tag = ""
      if txt is '>':
         txt = f.read(1)
         if txt == "": # breaks loop when f.read() reaches the end
            break
      while txt is not '>': #Variation of the getTag function modified to break loop and append tags      
         if txt is '<':
            txt = f.read(1)
            while txt is not '>' and txt is not '' and txt is not " ":
               tag += txt
               txt = f.read(1)               
            if txt is '>':
               taglist.append(tag)               
         else:
            txt = f.read(1)
            if txt == "": # breaks loop when f.read() reaches the end
               break #end of variation
   f.close()
   return taglist

def main():
   file = open("html.txt")
   ValidTags = []
   Exceptions = ["br", "hr", "meta"]
   taglist = createTagList()
   print("TagList = ", taglist)

   html = Stack()

   for tag in taglist:
      if tag[0] != "/" and tag in Exceptions:
         print("Tag is: ",tag," does not need to match. Stack is still: ",html.items)
      elif tag[0] != "/" :
         if tag not in ValidTags:
            print("Tag ",tag," not recognized, but accepted")
            ValidTags.append(tag)
         html.push(tag)
         print("Tag is: ",tag," pushed. Stack is now: ",html.items)
      elif tag[1:] == html.peek():
         html.pop()
         print("Tag is: ",tag," matches. Stack is now: ",html.items)
      else:
         print("Error: Tag is ",tag," but top of stack is ",html.peek())
         break
         
   if html.isEmpty():
      print("Processing complete.  No mismatches found.")
   else:
      print("Processing complete.  Unmatched tags remain on stack: ",html.items)      
  
   
main()
