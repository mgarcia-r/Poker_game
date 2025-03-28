import random
class Card:
    RANKS=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    SUITS=["♣","♦","♥","♠"] #clubs, diamonds, hearts, spades
    def __init__(self,rank,suit):
        """
        Method that creates a card instance by checking if rank and suit are valid, meaning if they are within the lists RANKS and SUITS
        :param rank: a rank
        :param suit: a suit
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank=rank
        self._suit=suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self._rank}{self._suit}"

    # For printing a LIST of cards held within a container (list, dictionary, tuple) we need to use repr
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """
        Checks if two cards are equal by seeing if they have the same rank
        :param other: card 2
        :return: -
        """
        return self.rank==other.rank

    #To check if a card is greater/lesser than another we need to compare their POSITIONS in the list RANKS
    def __lt__(self, other):
        """
        Checks if a card is lesser than another by comparing their position in the list RANKS
        :param other: card 2
        :return: -
        """
        return self.RANKS.index(self.rank)<self.RANKS.index(other.rank)

    def __gt__(self, other):
        """
        Checks if a card is greater than another by comparing their position in the list RANKS
        :param other: card 2
        :return: -
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        _cards=[]
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank,suit))
        self._cards=_cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


if __name__=="__main__":
    c1= Card("A","♠") #card created
    print(c1)
    print(c1.suit,c1.rank)
    deck=Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
