class CardClass():
    def __init__(self, InSuit, InTrueValue):
        self.Suit = InSuit
        self.TrueValue = InTrueValue # 1-13, A-K
        if (self.TrueValue == 11) or (self.TrueValue == 12) or (self.TrueValue == 13):
            self.BJValue = 10
        else:
            self.BJValue = self.TrueValue #Aces are considered 1.
            