#  File: ExpressionTree.py
#  Description: Creates an expression tree
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:11/29/2016
#  Date Last Modified:12/2/2016

import operator

class BinaryTree:    

    def __init__(self,initVal = "debug"):
        self.data = initVal
        self.left = None
        self.right = None

    def insertLeft(self,newNode = None):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode = None):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data

    def createTree (self, expr): #Creates Tree using recursion

        operators = ["+","-","*","/"]
        if len(expr)>0:
            item = expr.pop(0)
            if item == "(":
                self.insertLeft()
                self.getLeftChild().createTree(expr)
                item = expr.pop(0)
                if item == ")":
                    item = expr.pop(0)
                self.setRootVal(item)
                self.insertRight()
                self.getRightChild().createTree(expr)                
            elif item not in operators and item != ")":
                self.setRootVal(float(item))                

    def evaluate(self,root): #Evaluates Tree
        operators = {"+":operator.add,
                     "-":operator.sub,
                     "*":operator.mul,
                     "/":operator.truediv}
        Left = root.getLeftChild()
        Right = root.getRightChild()
        if Left and Right:
            fn = operators[root.getRootVal()]
            return fn(self.evaluate(Left),self.evaluate(Right))
        else:
            return root.getRootVal()                  
                     
        
    def preorder(self,root):
        if root != None:
            print(root.getRootVal(), end=" ")
            self.preorder(root.getLeftChild())
            self.preorder(root.getRightChild())
     

    def postorder(self,root):
        if root != None:
            self.postorder(root.getLeftChild())
            self.postorder(root.getRightChild())
            print(root.getRootVal(), end=" ")

def main():

    f = open("treedata.txt")
    for line in f:   
        print("Infix Expression:",line)
        expr = line.split()
        Tree = BinaryTree()
        Tree.createTree(expr)
        print("Value:             ",Tree.evaluate(Tree))
        print("Prefix Expression: ", end= " ")
        Tree.preorder(Tree)
        print("")
        print("Postfix Expression:", end= " ")
        Tree.postorder(Tree)
        print("\n")
    

main()

