from random import shuffle

def ShuffleDeck(InDeck):
    ToShuffle = InDeck
    shuffle(ToShuffle)
    return ToShuffle

def DrawTop(InDeck):
    ToHand = InDeck[0]
    InDeck.pop(0)
    return ToHand, InDeck