#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:44:44 2020

@author: ronaksharma
"""

#--------- Think Python----------#
#------------ Exercise 3----------#
#import turtle
#import math
#def square(exampleTurtle):
#    for i in range(4):
#        exampleTurtle.fd(100)
#        exampleTurtle.lt(90)
#
#        
#def polygon(exampleTurtle,n):
#    angle=360//n
#    for i in range(n):
#        exampleTurtle.fd(100)
#        exampleTurtle.lt(angle)
#        
#def circle(exampleTurtle,radius):
#    circumfrence=2*(math.pi)*radius
#    n=int(circumfrence/2)
#    angle=360//n
#    for i in range(n):
#        exampleTurtle.fd(2)
#        exampleTurtle.lt(angle)
#  
#n=6
#radius=100
#jop=turtle.Turtle()
#circle(jop,radius)
#turtle.mainloop()

#------------- Exercise 5-------------#
#import time
#def convertTimetoDays(time):
#    numberOfDaysPassedSinceEpoch=(time//86400)
#    currentHour=(time//3600)%24
#    currentMinute=(time//60)%60
#    print(numberOfDaysPassedSinceEpoch,currentHour,currentMinute)
#
#currentTime=time.time()
#convertTimetoDays(currentTime)

#def recurse(n, s):
#    if n == 0:
#        print(s)
#    else:
#        recurse(n-1, n+s)
#recurse(3, 0)

#--------------Exercise 6--------------#
# ADD IN RECURSIVE FUNCTIONSS
# 1. Palindrone Problem

#def first(word):
#    return word[0]
#
#def last(word):
#    return word[-1]
#
#def middle(word):
#    return word[1:-1]
#
#def is_palindrone(testString):
#    if(len(testString)<3):
#        return True
#    else:
#        if(first(testString)==last(testString)):
#            middleString=middle(testString)
#            result=is_palindrone(middleString)
#        else:
#            return False
#    return result
#    
#p="redivider"
#outcome=is_palindrone(list(p))
#print(outcome)

#-------------- Exercise 9-----------#
# Exercise 9.1
#def has_no_e(word):
#    if 'e' not in word:
#        return True
#    else:
#        return False
#        
#def uses_all(word,letters):
#    if(set(word)==set(letters)):
#        return True
#    else:
#        return False
#        
#fin=open('words.txt')
#for line in fin:
#    word=line.strip()
#    isThereaE=has_no_e(word)
#    if (isThereaE== True):
#        print(word)
#    else:
#        pass

#----------------- Exercise 10-----------_#
#--------- 10.2
#def cumSum(arr):
#    cumSummation=0
#    cumList=[]
#    cumList.append(arr[0])
#    arr.pop(0)
#    for currentVal in arr:
#        cumSummation=cumList[-1]+currentVal
#        cumList.append(cumSummation)
#    return cumList
#
#arr=[1,2,3]
#result=cumSum(arr)
#print(result)    
#Also x[1:-1] returns the elemetns between the first and the last    

#-------

#--------- Exercise 11--------------#
# 1. All mutuable types are global (if declaed in main)and hence can be changed in any function
# You don't need to explicityly declare it like below
#--------1-------
# been_called is a GLOBAL VARIABLE. However the 'been_called' inside the function
# is created as a local varibable. It does not know about the gloabl version. To change
# the global value declare 'global been_called' and then it would work
#been_called = False
#def example2():
#    been_called = True 

#---- 11.1-----#
# 1. If key does not exists, then it will add it with the given value
# If it exists it will do nothing
# 2. The setdefault returns the value associated with that. So if it exists, then you can append the list directly
#def invert_dict(d):
#    inverse = dict()
#    for key in d:
#        val = d[key]
#        inverse.setdefault(val,[]).append(key)# If not exists create a list. If exists then append to teh list
#    return inverse
 #---------11.3-------
#def ackermann(m, n):
#    d=dict()
#    if (m,n) in d:
#        return d[(m,n)]
#    if m == 0:
#        return n+1
#    if n == 0:
#        return ackermann(m-1, 1)
#    d[(m,n)]=ackermann(m-1, ackermann(m, n-1))
#    return d[(m,n)]
#
#print(ackermann(3, 4))

#--------- Exercise 12--------------#
#from functools import cmp_to_key

#-------12.2-----
#def anagrams(listOfWords):
#    dictionaryOfAnagrams=dict()
#    for word in listOfWords:
#        wordSorted=''.join(sorted(list(word)))
#        if wordSorted not in dictionaryOfAnagrams:
#            dictionaryOfAnagrams[wordSorted]=[word]
#        else:
#            dictionaryOfAnagrams[wordSorted].append(word)
#    return dictionaryOfAnagrams
#      
#words=['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled','retainers', 'ternaries','resmelts', 'smelters', 'termless']
#result=anagrams(words)
#
#def sortComparator(a,b):
#    if(len(a)>len(b)):
#        return 1
#    else:
#        return -1
#
#compareResult=sorted(result.values(),key=cmp_to_key(sortComparator),reverse=True)
#print(compareResult)

#-------12.4----

#def validEnglighWord(word,validWords,result,d):
#    if (word in validWords and len(word)==1):
#        return 1
#    if(word in d):
#        return d[word]
#    for i in range(len(word)):
#        testWord=word[:i]+word[i+1:]
#        if(testWord not in validWords):
#            isValidWord=0
#        else:
#            isValidWord=validEnglighWord(testWord,validWords,result,d)
#            d[word]=isValidWord  
#        result=result|isValidWord
#        
#    return result  
#      
#def testForWords(english,validWords):
#    d=dict()
#    listOfValidWords=[]
#    for word in english:
#        result=0
#        isValid=validEnglighWord(word,validWords,result,d)
#        if(isValid==1):
#            if(len(listOfValidWords)==0):
#                listOfValidWords.append(word)
#            else:
#                if(len(word)>len(listOfValidWords[0])):
#                    listOfValidWords=[word]+listOfValidWords
#                else:
#                    listOfValidWords.append(word)
#        d={}
#    return listOfValidWords    
#
#english=["world","chrisp"]
#validWords=["wrld","wrd","wd","w","chris","cris","cri","cr","c"]
#outcome=testForWords(english,validWords)
#print(outcome)

#************************ READ SECTION B FOR ALGORITHMS ****************#

#-------- Exercise 13---------#
#---- 13.3-- Assigning default values to arguments in functions
# def assignRandomValue(listOfWords,num=10 ) num is given a default value of 10

#---------Exercise 14---------#
# Dealing with Files
#----- Traversing All the files in a directory
#import os
#def printDirectoryNames(directory):
#    for direc in os.listdir(directory):
#        path=os.path.join(directory,direc) #Create a path to that object
#        
#        if(os.path.isfile): # If that object is a file, then terminate as cannot go further
#            print(path)
#        else:
#            printDirectoryNames(path) # Traverse if the path is not a file

#------- Try and Catch--------#
# 1. Similart to If..else statement
# 2. Catching an error allows you to tray again and end gracefully
#try:
#    fin=open('word_exists.txt')
#except:
#    print("Somthing Wrong")

#-------- Databases---------#
# 1. Same as dict as mapping of key to values (Primary Keys)
# 2. They are stored permanently on a disk and can be accessed after
# the programme has terminated
# 3. Accessing objects in database returns byte object which is similar but not
# exactly like byte objects

#import dbm
#db=dbm.open('caption','c')
#db['cheese']="Goes best with wine"
#db['crips']="Goes best with drinks"
#for key in db.keys(): # Can access keys
#    print(key, db[key])
#    
#db.close()

#------Pickling
# 1. Since database only strings, this converts any object to string
#import pickle 
#x=[1,2,3]; p=pickle.dumps(x)
# y=pickle.loads(p); #To unpickle,
#p==x #but they are different objects
#p is x # false are they are differnet objects

#------Importing Python Files------#
# 1. Using if __name__=="main" means that all functions inside this condition
# will only be run, when the that file is ran as a main
# 2. Usually put test methods for that module in the main, so they are not run when module is being used by other files
#import wc # This will not print any of the wc's test methods because they are in 'main'

#-------- Exercises 14----------#
#------ Exercise 14.1
#def sed(pattern,replace,file1,file2):
#    f1=open(file1)
#    f2=open('storeStuff.txt','w') # Open file before entering the for loop
#    for word in f1:
#        if(pattern in word):
#            word=word.replace(pattern,replace)
#        f2.write(word)
#    f2.close()
#
# 
#pattern = 'the'
#replace = 'hooray'
#source = 'trial.txt'
#dest = 'storeStuff.txt'
#sed(pattern, replace, source, dest)

#----------------------THE GOODIES (Chapter 19)-----------------------#


#- 1: Conditional Expression----#
# Allows to replace a conditional statement with a conditional expression if both
# branches contain simple expressions that are either returned or assigned to 
# the same variable

#import math
#x=4
##if x > 0:
##    y = math.log(x)
##else:
##    y = float('nan')
#
## “y gets log-x if x is greater than 0; otherwise it gets NaN"
#y = math.log(x) if x > 0 else float('nan') # Converted to confitional expression
#


#--2: Generator Functions-------------#
# ADVANTAGE: Takes very less memory space compared to lists but longer to evaluate
# 1a. Handling large datasets that can affect the memory space thus optimising memory space*
# 1b. If the list is smaller than the running machine’s available memory, then list 
# comprehensions can be faster to evaluate than the equivalent generator expression
# 2. Create a generator object pointing to the current value instead of the whole list
# 3. 'yield' indicates where a value is sent back to the caller, but unlike 
#     return, you don’t exit the function afterward
# 4a. At 'yield', the state of the function is remembered. So calling 'next()'
#  the previouslt yilded value is increament (ex +1) and then returned
# 4b. When next() is called the code up to yield is executed and the function 
#    is suspended. The next yield starts from where the function was suspended and 
#   continues until the next yield is reached
# 5. Example Functions like sum and in can be performed with generator
# 6. Can iterate over them only once

# NOTE: Using a list comprehension unnecessarily creates a list of the one hundred 
# numbers, in memory, before feeding the list to sum. The generator expression 
# need only produce a single value at a time, as sum iterates over it.


# Creating a generator
#def infinite_sequence():
#    num = 0
#    while True:
#        yield num #Stores the state
#        num += 1

# Creating a generator using comprehension
#x=(num*2 for num in range(5))#  'x' is a generator here as we are using '( )' instead of '[ ]'
#next(x) # Starts with 0 and each time this is called prints the next number
#next(x) # Print 2

#-------- Using ANY and ALL------#
# 1. Structure is similar to just adding a conditional expresseion in the argument of 'any' or 'all'

# any(i<0 for i in x) # Checks if any element in 'x' is negative
# all(i>0 for i in x) # Checks if all elements of 'x' are positive

#----- Accessing Keyword Arguments------#
#def printall(*args, **kwargs):
#    print(args, kwargs)
#
#printall(1, 2.0,'a',-4, third='3')



#-------------- ANALYSIS OF ALGORITHMS-----------------#
# 1. Order of growth matters for bigger problems and not smaller problems
# 2. The computer machine, type of dataset(consider worst case) and size of dataset
#  (essentially the run time or number of operations) define the time complexity
# 2. In Python division takes longer than multi
# 3. O(1): Indexing(accessing an index to do something there) and len()
# Dictionary operations like 'in'
# 4. O(n): String concatenation and other string methods like join, min,max
# Search methods like 'in', 'find', 'count' for lists (not dictionary)
# List methods
# 5 O(nlogn): Sorting
# 6. x[i:j] depends on the size of the output