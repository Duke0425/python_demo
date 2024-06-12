from collections import namedtuple
from random import choice

Card = namedtuple('cards', ['suit', 'rank'])


class FrenchCards:
    suits = "Club Diamond Heart Spade".split()
    ranks = [i for i in range(2, 11)] + list("JQKA")

    def __init__(self) -> None:
        self._cards = [Card(s,r) for r in self.ranks 
                                 for s in self.suits]
    
    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self):
        return len(self._cards)


frenchCards = FrenchCards()
length = len(frenchCards)

frenchCards[0]
frenchCards[-1]
choice(frenchCards) # random choice

suitValues = dict(Club=0, Diamond=1, Heart=2, Spade=3)

def spade_hight(card):
    rank_value = FrenchCards.ranks.index(card.rank)
    return rank_value * len(suitValues) + suitValues[card.suit]


# sort cards
for card in sorted(frenchCards, key=spade_hight):
    print(card)
