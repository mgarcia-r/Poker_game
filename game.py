from deck import Deck, Card

class Hand:
    def __init__(self,deck):
        """
        Method that creates and deals a 5 card hand
        :param deck: the poker deck
        """
        cards=[]
        for i in range(5):
            cards.append(deck.deal())
        self._cards=cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Method that checks if a hand is a flush or not by comparing all the cards in the hand with the first
        :return: True if it is a flush and False if it is not a flush
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Goes over each hand and returns the amount of matches
        :return: number of matches
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if a hand has 1 pair
        :return: TRUE if it has 1 pair, FALSE if it doesn't have 1 pair
        """
        if self.num_matches==2: #One pair is 2 matches
            return True
        return False

    @property
    def is_2pair(self):
        """
        Checks if a hand has 2 pairs
        :return: TRUE if it has 2 pairs, FALSE if it doesn't have 2 pairs
        """
        if self.num_matches == 4:  # One pair is 2 matches
            return True
        return False

    @property
    def is_trips(self):
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Checks if a hand is a full house, if it has 8 matches
        :return: TRUE if full house, FALSE if else
        """
        if self.num_matches == 8:
            return True
        else:
            return False







matches=0
count=0
while matches<1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count+=1
    if hand.is_full_house:
        #print(hand)
        matches+=1
        #break

print(f"The probability of 2 pairs is {100*matches/count}%")




