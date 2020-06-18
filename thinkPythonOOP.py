#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:18:10 2020

@author: ronaksharma
"""
#----------- Basics of Object Oriented-------------#
# Go the next Section for better stuff and the summary

#----------------EXERCISE 15----------------------------------#
#class Points:
#    """
#    Attributes as x and y coordinates
#    """
#    def calcDistnace(point1,point2):
#        distance=(point1.x-point2.x)+(point1.y-point2.y)
#        print(distance)
##
#class Rectangle:
#    """
#    Atributes as width, height and corner
#    """
#def move_Rectangle(rec,dx,dy):
#    rec.corner.x+=dx
#    rec.corner.y+=dy
# 
#blank=Points()
## Declaring Pointts#
#blank.x=0
#blank.y=0
#blank2=Points()
#blank2.x=4
#blank2.y=8
##Points.calcDistnace(blank,blank2)
#
#
#box=Rectangle()
#box.width = 100.0
#box.height = 200.0
#box.corner=Points() # Box object has an attribute called corner. This happens to be a type of object in Point Class
#box.corner.x=10
#box.corner.y=-10
#dx,dy=10,20
#move_Rectangle(box,dx,dy)
##print(box.corner.x,box.corner.y)

#class Circle:
#    """
#    Attributes are centre and radius
#    """
#def point_in_circle(circleObject, pointObject):
#    temp1=(pointObject.x -circleObject.centre.x)**2
#    temp2=(pointObject.y -circleObject.centre.y)**2
#    if((temp1+temp2 - (circleObject.radius)**2) <= 0):
#        return True
#    else:
#        return False
#
#rnd=Circle()
#rnd.radius=5
#rnd.centre= Points()
#rnd.centre.x=0
#rnd.centre.y=0  
#print(point_in_circle(rnd,blank))

#--------------------------------------------------#
# 1. return (x, y, z) > (a,b,c): Check simultaneouslt and if returns TRUE if it is
# 2. Programs that use pure functions are faster to develop and less 
# error-prone than programs that use modifiers
# 3. Assert is used to raise an error and exit the programme. If condition is false
# ex- assert if(1>2); This will raise an erro
# 4. Similarly 'raise' is used but that focuses on raising an error,, when condition are met

#---------------- Object Oriented Programming--------------------#
# SET 1
# 1. Can declare attributes that have not been declared in the class yetå
# 1. Object are mutable, so chaning their value in a function changes their
# values throughout like global varibales. This was the case with lists
# 2. Comparing two objects '==' does not compare their value but if they are the same
# 3. To check 'p' instace of class Point; isinstance(p, Point) 
# 4. To check if 'x' is an attr. of 'p' ; hasattr(p, 'x')

# SET 2
# 1. 'self' here refers to an object in Python essentially
# 1. When you declare (self), you can just call that method as an instance to the object
# created. This object should have the attributes defined in the method as shown
# 2. It is possible to pass one object as 'self' i.e. call using it and the other as an argument
# 3. Can create a new object of the same class within the method of this class
# 4. __str__ returns a string representation of an object only when 
# object is printed i.e. print(object). If this function does not exits and you print an object
# you will get a weird print
# 4. __add___ method is called each time two objects of class Time are subjected to 
# '+' sign. They don't need to addded necesarrily, but object1+object2 will call this function
# From this method, you can also call other methods like self.increment() if a condition is met.
# Ex- Type based dispatch where the methods are called based on the type of argument passed into them.
# This makes method efficient as you run different logic depending on the object type
# 5. print(timeNow+timeObject3) calls both '__add__' and '__str__' as they deal with objects
# 6. To check if this is an object: 'isinstance(other, Time)
# 7. To check type; type(object) is str/int/tuple/list/dict etc
# 8. Use pylint as a statistical code analysis tool
# 9. Avoid using mutable objects as default value
#class Time:
#    
#    def __str__(self):
#        return "{0} is the time now {1}".format(self.hour,self.minute)
#        
#    def __add__(self,anotherObject):
#        if isinstance(anotherObject,Time): # Checks if this an object
#            seconds=self.hour+anotherObject.hour
#            anotherObject.minute=-1000+seconds
#            return anotherObject
#        elif(type(anotherObject) is str): #If the argument is not obejct then run this
#            return "Damnn {0}".format(anotherObject)
#        else:
#            return -1000*anotherObject
#    
#    def timePrint(time): # Not so good way
#        print(time.hour,time.minute)
#        
#    def timePrintV2(self):
#        print(self.hour,self.minute)
#        
#    def time_to_int(self):
#        minutes = self.hour * 60 + self.minute
#        return minutes
#        
#    def increment(self,object2):
#        timeNew=Time() # Creating a new object inside the class
#        seconds=object2.hours
#        timeNew.hour=seconds
#        return (self.hour+seconds,timeNew)
#
#timeNow=Time()
#timeObject2=Time()
#timeObject3=Time()
#timeObject3.hour=100
#timeObject2.hours=1000
#timeObject2.minute=-2
#timeNow.hour=20
#timeNow.minute=100
#timeNow.timePrint() # 'timeNow' object gets assigned to the first parameter i.e. self
#timeNow.timePrintV2() # shifts the responsibility from function to the objects
##print(timeNow.time_to_int())
#x,y=timeNow.increment(timeObject2) # Passing one object as a 'self' and the other as an argument
##print(x,y.hour)
#print(timeNow) # This invokes the __str__ method initiliasiation
#print(timeNow+"amazing") # '+' invokes the __add__ and then print invokes '_srt_' as return is a object
#print(timeNow+100)  # Invokes a different method based on the object type

# Exercise 17.2
# 1. Don't use mutable objects as default value. Replace default value of the
# list to None as this wa
#class Kangaroo:
#    """A Kangaroo is a marsupial."""
#    
#    def __init__(self, name, contents=None):
#
#        self.name = name
#        if contents == None:
#            contents = []
#        self.pouch_contents = contents
#
#    def __str__(self):
#        return str(self.pouch_contents)
#
#    def put_in_pouch(self, item):
#
#        self.pouch_contents.append(item)
#
#
#kanga = Kangaroo('Kanga')
#kanga.put_in_pouch('wallet')
#kanga.put_in_pouch('car keys')
#roo = Kangaroo('Roo')
#kanga.put_in_pouch(roo)

#------------------- INHERITANCE--------------------#
# 1. SMART: Indexing here defines the encoding done instead of a dictionary
# 2. suit_names and rank_names: Class attributes as inside class and outside method
# ACCESS: Card.suit_names as card is class object [FIXED]
# 3. rank and suit: Instance attribute as associated with a particular instance
# ACCESS: self.rank where self is rank of a particular instance (NOT FIXED)
# 4. To access the __str__ function, you can also use str(object) that does the job
# 5. 'self.cards.sort' in Class 'deck', uses the __lt__ method to sort. Since we
# are sorting 'card objects' and we already defined __lt__ , it uses that to sort
# So this way we can change the default 'sort' method used in classes

#import random
#class deck:
#    
#    def __init__(self):
#        self.cards=[]
#        for suit in range(4):
#            for rank in range(14):
#                self.cards.append(card(suit,rank)) # Calling another Class inisde this
#                
#    def __str__(self):
#        res=[]
#        for nameOfCard in self.cards:
#            res.append(str(nameOfCard)) # IMPORTANT: Calling the other class's function
#        return '\n'.join(res)
#        
#    def popCard(self):
#        return self.cards.pop()
#        
#    def pushCard(self,cardToAdd):
#        self.cards.append(cardToAdd)
#        
#    def shuffle(self):
#        random.shuffle(self.cards)
#        
#    def sortCards(self):
#        self.cards.sort()
#    
#    def dealHands(self,numberOfHands,cardsPerHand):
#        handObjects=[]
#        handFinalObjects=[]
#        for i in range(numberOfHands):
#            for j in range(cardsPerHand):
#                handObjects.append(card(random.choice(card.suit_names),random.choice(card.rank_names)))
#            handFinalObjects.append(Hand(handObjects,'Hand {0}'.format(i)))
#            handObjects=[]
#        return handFinalObjects
#        
#    def move_cards(self, hand, num):
#        for i in range(num):
#            hand.add_card(self.pop_card())        
#
#class card:
#    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
#    
#    def __init__(self,suit=0,rank=2):
#        self.suit=suit
#        self.rank=rank
#        
#    def __lt__(self,cardNumber2): # __lt__ : a is 'less than'b
#        tuple1=self.suit,self.rank
#        tuple2=cardNumber2.suit,cardNumber2.rank
#        return tuple1<tuple2
#        
#    def __str__(self):
#        output="Suit is {0} and Rank is {1}"
#        return output.format(card.suit_names[self.suit],card.rank_names[self.rank])
#
#class Hand(deck):
#    def __init__(self,cards,label=''):
#        self.cards=cards
#        self.label=label
       

##card1=card(2,6)
##card2=card(2,10)
##print(card1)
##output=card1.__lt__(card2) # Inside function comaprision. Can create a function outside class to do this and pass the two objects
##print(output)
##deckOfCards=deck()
##deckOfCards.sortCards()
##print(deckOfCards)
#
##--------- Amazing implementation of Inheritance----------#
#deckOfHand=deck() # parent class object created
#cardToAdd=deckOfHand.popCard() # parent card pops a card
#firstHand=Hand('First Hand') # Creates an object of child class
#firstHand.pushCard(cardToAdd) # Uses the 'pushCard' from parent to add a card
#print(firstHand)
##---------------------------#


#----------- Exercise 18.2---------------#
#deckObject=deck()
#listOfHands=deckObject.dealHands(2,10)
#for hands in listOfHands:
#    for cardInT in hands.cards:
#        print(cardInT.suit,cardInT.rank)
#    print("\n")

# Exercise 18.3: Check Card.py and PokerHand.py
#---------------------------------------------------------------#