from CardClass import *
import DeckHandler
import BotInterface
import random

def Game(BotPlaying=False):
    Deck = []
    
    for i in range(13):
        Deck.append(CardClass("Clubs", i+1))
        Deck.append(CardClass("Spades", i+1))
        Deck.append(CardClass("Diamonds", i+1))
        Deck.append(CardClass("Hearts", i+1))
        
    #for i in Deck:
    #    print(i.Suit, i.TrueValue, i.BJValue)
    
    Deck = DeckHandler.ShuffleDeck(Deck)
    
    Hand = []
    CardsToDraw = 1
    for i in range(CardsToDraw):
        ToHand, Deck = DeckHandler.DrawTop(Deck)
        Hand.append(ToHand)
        
    #print("HAND")
    #for i in Hand:
    #    print(i.Suit, i.TrueValue, i.BJValue)
        
    #print("DECK")
    #for i in Deck:
    #    print(i.Suit, i.TrueValue, i.BJValue)    
    
    GameOn = True
    HandValue = 0
    while GameOn:
        HandValue = 0
        for i in Hand:
            HandValue += i.BJValue
        if HandValue > 21:
            GameOn = False
            print("Over 21, Bust, card value:", HandValue)
            return HandValue
        
        for i in Hand:
            print(i.Suit, i.BJValue)
        
        if BotPlaying: 
            #global BotCommand
            if BotInterface.BotDrawLimit % 1 == 0:
                if HandValue < BotInterface.BotDrawLimit: Action = "DRAW"
                else: Action = "NODRAW"
            else:
                RandNum = random.randint(0,1)
                if (RandNum > (BotInterface.BotDrawLimit % 1)) and (HandValue < BotInterface.BotDrawLimit): Action = "DRAW"
                else: Action = "NODRAW"
        else: Action = input(">>> ").upper()
        if Action == "DRAW":
            ToHand, Deck = DeckHandler.DrawTop(Deck)
            Hand.append(ToHand)
        if Action == "NODRAW":
            GameOn = False
            print("No card drawn.")
            if HandValue > 21: print("Over 21, Bust, card value:", HandValue)
            else: print("21 or under, Win, card value:", HandValue)
            break
    
    return HandValue
            