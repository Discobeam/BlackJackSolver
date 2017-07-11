from Game import *
import BotInterface
AllResults = []
CurrentResults = []
Attempts = 10**7

BotInterface.BotCommand = "DRAW"
BotInterface.BotContinueGame = True

#BOT VARS START

PrevRunDataFile = open("TenMillionAttemptsRun.txt", mode='r')
PrevRunData = PrevRunDataFile.readlines()

BotInterface.BotDrawLimit = float(PrevRunData[0].rstrip("\n"))
DiffToApply = float(PrevRunData[1]) #Adjust DrawLimit by prerecorded amount each time

#BOT VARS END
FirstRun = True
for e in range(10):
    for i in range(Attempts):
        CurrentResults.append(Game(True))
        print("NG")
        
    NewList = []
    for Result in CurrentResults:
        NewList.append(Result)
        
    AllResults.append(NewList)
    
    if FirstRun: BotInterface.BotDrawLimit += DiffToApply
    else: 
        CurrentTotalPoints = 0
        PreviousTotalPoints = 0
        
        for CurrentList in AllResults[-1]:
            if CurrentList <= 21: CurrentTotalPoints += CurrentList
            
        for PrevList in AllResults[-2]:
            if PrevList <= 21: PreviousTotalPoints += PrevList
                
        print(CurrentTotalPoints)
        print(PreviousTotalPoints)
        if CurrentTotalPoints > PreviousTotalPoints: #If it's getting better
            BotInterface.BotDrawLimit += DiffToApply
        else: #If it's getting worse
            DiffToApply /= 2 
            BotInterface.BotDrawLimit -= DiffToApply
            
    LogFile = open("TenMillionAttemptsRun.txt", mode="w") #MillionAttemptsRun
    LogFile.write(str(BotInterface.BotDrawLimit) + '\n')
    LogFile.write(str(DiffToApply))
    
    CurrentResults = []
    
    FirstRun = False