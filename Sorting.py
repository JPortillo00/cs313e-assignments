#  File: Sorting.py
#  Description: Measure th average time for each sorting function
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:11/15/2016
#  Date Last Modified:11/18/2016

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def SortingTime(listLength,sortType,listType,n):

    #This function does all the timing for the sorts depending on the parameters
    #listlength => lenght of list
    #sortType => Type of sort used
    #listType => how list will be manipulates i.e. reverse, random, almost sorted

    avgTime = 0

    for i in range(n):

        myList = [i for i in range(listLength)]
        #establishes list for certian case
        if listType == "Almost Sorted":            

            random.shuffle(myList)
            for i in range(listLength//10):
                rIndex1 = random.randint(0,len(myList)-1)
                rIndex2 = random.randint(0,len(myList)-1)
                while rIndex1 == rIndex2:
                    rIndex2 = random.randint(0,len(myList)-1)
                temp = myList[rIndex1]
                myList[rIndex1] = myList[rIndex2]
                myList[rIndex2] = temp
                
        elif listType == "Random":
            
            random.shuffle(myList)
            
        elif listType == "Reverse":
            
            myList.reverse()
       
        startTime = time.perf_counter()
        #finds sutible sort for parameter
        if sortType == 'bubble':            
            bubbleSort(myList)            
        elif sortType == 'select':           
            selectionSort(myList)            
        elif sortType == 'insert':            
            insertionSort(myList)            
        elif sortType == 'shell':            
            shellSort(myList)            
        elif sortType == 'merge':            
            mergeSort(myList)
        elif sortType == 'quick':
            quickSort(myList)

        endTime = time.perf_counter()           
        elapsedTime = endTime - startTime
        avgTime += elapsedTime

    return (avgTime/n)
    

def main():
    
    sampleSize = 5 # this was just used so I could increase the size on calculated the average. Currently set to 5 as assigned
    #The following data structures are used to print a table as Dr. Bulko assigned
    inputType = ["Random","Sorted","Reverse","Almost Sorted"] #Types of List or How the List would be manipulated
    Sorts = ["bubble","select","insert","shell","merge","quick"] #Sort Types
    SortFun = {'bubble': "      bubbleSort", #SortFunctions
               'select': "   selectionSort",
               'insert': "   insertionSort",
               'shell' : "       shellSort",
               'merge' : "       mergeSort",
               'quick' : "       quickSort"}

    for i in inputType: #prints table which matches specs based of table on assignment
        print("Input Type =",i)
        print("                    avg time   avg time   avg time")
        print("   Sort function     (n=10)    (n=100)    (n=1000)")
        print("-----------------------------------------------------")
        for x in Sorts:
            print(SortFun[x],
                  " ",'%.6f'%SortingTime(10,x,i,sampleSize),
                  " ",'%.6f'%SortingTime(100,x,i,sampleSize),
                  " ",'%.6f'%SortingTime(1000,x,i,sampleSize))
        print(" ")   
    

main()
