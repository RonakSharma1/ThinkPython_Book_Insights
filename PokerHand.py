"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.rank={}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.rank[card.rank]= self.rank.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        
        self.suit_hist()
        for val in self.rank.values():
            if val >= 2:
                return True
        return False
        
    def has_twopair(self):
        self.suit_hist()
        counter=0
        for val in self.rank.values():
            if val >= 2:
                counter+=1
                if(counter==2):
                    return True
        return False
        
    def classify(self):
        self.count={'F':0,'T':0,'P':0}
        if(self.has_flush()):
            self.count['F']+=1
            print("Flush")
        elif(self.has_twopair()):
            self.count['T']+=1
            print("Two Pair")
        elif(self.has_twopair()):
            self.count['P']+=1
            print("Pair")
        else:
            None
        print(self.count)
        
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        hand.classify()
        print('')

