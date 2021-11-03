import os
import ctypes
import threading
import time
import datetime
import keyboard
import random
from pygame import mixer

ctypes.windll.kernel32.SetConsoleTitleW("Vlucht Vlug")
os.system("mode con: cols=39 lines=18")

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def startmusic(musicFileName):
    mixer.init()
    mixer.music.load(musicFileName)
    mixer.music.play()

today = datetime.date.today()
birthday = datetime.date(2004, 5, 18)

thisyear = datetime.date(today.year, birthday.month, birthday.day)
nextyear = datetime.date(today.year + 1, birthday.month, birthday.day)
birthdaydaysthisyear = (thisyear - today).days
birthdaydaysnextyear = (nextyear - today).days

if birthdaydaysthisyear > 0:
    if len(str(birthdaydaysthisyear)) < 3:
        minuslen = 3 - len(str(birthdaydaysthisyear))
        fillzero = "0" * minuslen
        cel = fillzero + str(birthdaydaysthisyear)
    else:
        cel = str(birthdaydaysthisyear)
elif birthdaydaysthisyear == 0:
    if today.year % 4 == 3:
        cel = "366"
    else:   
        cel = "365"
else:
    if len(str(birthdaydaysnextyear)) < 3:
        minuslen = 3 - len(str(birthdaydaysnextyear))
        fillzero = "0" * minuslen
        cel = fillzero + str(birthdaydaysnextyear)
    else:
        cel = str(birthdaydaysnextyear)

playernamelist = []
inventorylist = []
housinglist = []
worklist = []

restaurantitems = ["Rode wijn       ", "Bier       ", "Koffie       ", "Tomatensoep       ", "Salade       ", "Spaghetti       ", "Biefstuk       ", "Eendenborst       ", "Sorbetijs       ", "Cheesecake       "]

class scorenumber:
    score = 0

class timenumber:
    tnum = 0

class stoptimervar:
    stvar = False

def stoptimertrue():
    stoptimervar.stvar = True

def timer():
    while stoptimervar.stvar == False:
        time.sleep(1)
        timenumber.tnum += 1
        
        if timenumber.tnum > 86400:
            print("\033[0m")
            clear()
            os._exit(0)
        else:
            pass

class answerednumber:
    questionsanswered = 0

class stopvar:
    svar = False
    
def stopvartrue():
    stopvar.svar = True

def end6():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;192;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bedrijf is failliet gegaan vanwege\nslechte boekhouding. Je hebt nog\ngenoeg geld om te leven, maar het\nis zwaar.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;255;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bedrijf is failliet gegaan vanwege\nslechte boekhouding. Je hebt nog\ngenoeg geld om te leven, maar het\nis zwaar.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end6()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def end5():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;0;192;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bedrijf is groot geworden en\nje wordt langzaam een miljonair.\nJe hebt een heel hoog inkomen en\ngenoeg geld voor een villa.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;0;255;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bedrijf is groot geworden en\nje wordt langzaam een miljonair.\nJe hebt een heel hoog inkomen en\ngenoeg geld voor een villa.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end5()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def end4():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;192;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt geen baan meer en je mag geen\nhuis kopen zonder baan als vluchteling.\nJe bent nu dakloos.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;255;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt geen baan meer en je mag geen\nhuis kopen zonder baan als vluchteling.\nJe bent nu dakloos.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end4()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def end3():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;192;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bent gepakt en krijgt een\nlevenslange gevangenisstraf wegens\ndrugsgebruik en het stelen van geld\nuit de kassa.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;255;0;0mOei " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe bent gepakt en krijgt een\nlevenslange gevangenisstraf wegens\ndrugsgebruik en het stelen van geld\nuit de kassa.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end3()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def end2():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;0;192;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt een hoog inkomen en\ngenoeg geld voor een groot huis.\n\nJe bent geen vluchteling, maar een\nvrij rijke burger.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;0;255;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt een hoog inkomen en\ngenoeg geld voor een groot huis.\n\nJe bent geen vluchteling, maar een\nvrij rijke burger.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end2()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def end1():
    stoptimertrue()
    
    sec = timenumber.tnum % 60
    
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    else:
        pass
    
    secdivide = timenumber.tnum / 60
    min = int(secdivide // 1)
    
    if len(str(min)) == 1:
        min = "0" + str(min)
    else:
        pass
    
    if int(min) > 59:
        newmin = min % 60
        
        if len(str(newmin)) == 1:
            newmin = "0" + str(newmin)
        else:
            pass
        
        mindivide = min / 60
        hour = int(mindivide // 1)
        
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        else:
            pass
        
        hms = str(hour) + ":" + str(newmin) + ":" + str(sec) + "         "
    else:
        hms = str(min) + ":" + str(sec) + "            "
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered)[:15] + "+"
    else:
        pass
    
    scored = round((86400 - timenumber.tnum) / answerednumber.questionsanswered)
    
    scored = str(scored) + " " * (16 - len(str(scored)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    if stopvar.svar == False:
        keyboard.on_press_key("return", lambda _:stopvartrue())
        
        print("\033[38;2;0;192;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt een gemiddeld inkomen en\ngenoeg geld voor je eigen huis.\n\nJe bent geen vluchteling, maar een\ngewone burger.\n")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print(f"■             SCORE: {scored} " + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"    GESPEELDE TIJD: {hms}■")
        print(f"■ VRAGEN BEANTWOORD: {answered} " + "\033[38;2;192;192;0m■")
        print("■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        print("\033[38;2;0;255;0mGefeliciteerd " + str(*playernamelist) + "!\n")
        print("\033[38;2;192;192;0mJe hebt een gemiddeld inkomen en\ngenoeg geld voor je eigen huis.\n\nJe bent geen vluchteling, maar een\ngewone burger.\n")
        print("\033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f"             SCORE: {scored} ■")
        print(f"■    GESPEELDE TIJD: {hms}" + "\033[38;2;192;192;0m■")
        print("■\033[38;2;0;0;255m" + f" VRAGEN BEANTWOORD: {answered} ■")
        print("■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■ \033[38;2;0;0;255m■ \033[38;2;192;192;0m■")
        print("\033[38;2;64;64;64m\nDRUK OP ENTER OM AF TE SLUITEN...")
        time.sleep(0.5)
        clear()
        end1()
    else:
        print("\033[0m")
        clear()
        clearinput = input()
        clear()
        os._exit(0)

def question21():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Omdat je drugs heb gebruikt, heb je\nonbewust een lot van de loterij\ngekocht.\nGa je de uitslag bekijken?")
    print("───────────────────────────────────────")
    print("A    Ja")
    print("B    Nee")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        end2()
    elif answerup == "B":
        clear()
        end1()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question21()

def question20():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Er word je nog meer aangeboden.\nNeem je het aan?")
    print("───────────────────────────────────────")
    print("A    Ja")
    print("B    Nee")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        end3()
    elif answerup == "B":
        clear()
        question21()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question20()

class othernewquestionstartvar:
    onqsvar = False
    
def othernewquestionstartvartrue():
    othernewquestionstartvar.onqsvar = True

def otherquestion19():
    if othernewquestionstartvar.onqsvar == False:
        keyboard.on_press_key("return", lambda _:othernewquestionstartvartrue())
        
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je hebt helaas niet alles onthouden\nen je krijgt een waarschuwing van\nje baas. Na drie waarschuwingen\nword je ontslagen.\nProbeer het opnieuw.")
        print("───────────────────────────────────────")
        print("Druk op Enter om te starten...")
        time.sleep(1)
        clear()
        otherquestion19()
    else:
        random.shuffle(restaurantitems)
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je hebt helaas niet alles onthouden\nen je krijgt een waarschuwing van\nje baas. Na drie waarschuwingen\nword je ontslagen.\nProbeer het opnieuw.")
        print("───────────────────────────────────────")
        time.sleep(0.5)
        i = 0
        while i != 3:
            print(restaurantitems[i])
            time.sleep(1)
            i += 1
            print("\033[A\033[A")
        print("Wat wilde de klanten hebben?")
        clearinput = input()
        print("\033[A\033[A")
        item1 = input("1> \n2> \n3> \033[A\033[A\033[38;2;0;128;128m")
        item2 = input("\033[0m2> \033[38;2;0;128;128m")
        item3 = input("\033[0m3> \033[38;2;0;128;128m")
        itemcap1 = item1.capitalize()
        itemcap2 = item2.capitalize()
        itemcap3 = item3.capitalize()
        if itemcap1 + "       " == restaurantitems[0] and itemcap2 + "       " == restaurantitems[1] and itemcap3 + "       " == restaurantitems[2]:
            print("\033[38;2;0;192;0mGoed gedaan!\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            end2()
        else:
            print("\033[38;2;255;0;0mJe had helaas niet alles goed.\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            end4()

class newquestionstartvar:
    nqsvar = False
    
def newquestionstartvartrue():
    newquestionstartvar.nqsvar = True

def question19():
    if newquestionstartvar.nqsvar == False:
        keyboard.on_press_key("return", lambda _:newquestionstartvartrue())
        
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je hebt helaas niet alles onthouden\nen je krijgt een waarschuwing van\nje baas. Na drie waarschuwingen\nword je ontslagen.\nProbeer het opnieuw.")
        print("───────────────────────────────────────")
        print("Druk op Enter om te starten...")
        time.sleep(1)
        clear()
        question19()
    else:
        random.shuffle(restaurantitems)
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je hebt helaas niet alles onthouden\nen je krijgt een waarschuwing van\nje baas. Na drie waarschuwingen\nword je ontslagen.\nProbeer het opnieuw.")
        print("───────────────────────────────────────")
        time.sleep(0.5)
        i = 0
        while i != 3:
            print(restaurantitems[i])
            time.sleep(1)
            i += 1
            print("\033[A\033[A")
        print("Wat wilde de klanten hebben?")
        clearinput = input()
        print("\033[A\033[A")
        item1 = input("1> \n2> \n3> \033[A\033[A\033[38;2;0;128;128m")
        item2 = input("\033[0m2> \033[38;2;0;128;128m")
        item3 = input("\033[0m3> \033[38;2;0;128;128m")
        itemcap1 = item1.capitalize()
        itemcap2 = item2.capitalize()
        itemcap3 = item3.capitalize()
        if itemcap1 + "       " == restaurantitems[0] and itemcap2 + "       " == restaurantitems[1] and itemcap3 + "       " == restaurantitems[2]:
            print("\033[38;2;0;192;0mGoed gedaan!\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            end2()
        else:
            print("\033[38;2;255;0;0mJe had helaas niet alles goed.\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            otherquestion19()

def question18():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je moet voor je eigen bedrijf je eigen\nboekhouding doen.\nLos de volgende sommen op:")
    print("───────────────────────────────────────")
    answer1 = input("        7 × 8 = \n    666 − 597 = \n48 ÷ 2(3 + 9) = \033[A\033[A\033[38;2;0;128;128m")
    answer2 = input("\033[0m    666 − 597 = \033[38;2;0;128;128m")
    answer3 = input("\033[0m48 ÷ 2(3 + 9) = \033[38;2;0;128;128m")
    if answer1 == "56" and answer2 == "69" and answer3 == "288":
        print("\033[38;2;0;192;0mGoed gedaan!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        answerednumber.questionsanswered += 1
        clear()
        end5()
    else:
        print("\033[38;2;255;0;0mJe had helaas niet alles goed.\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        end6()

def question17():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je baan komt waarschijnlijk te\nvervallen, maar je krijgt een kans om\nschoonmaker te worden.\nGa je akkoord?")
    print("───────────────────────────────────────")
    print("A    Ja")
    print("B    Nee")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        end1()
    elif answerup == "B":
        clear()
        end4()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question17()

def question16():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je gebruikt het geld uit de kassa.\nHoeveel koop je?")
    print("───────────────────────────────────────")
    print("A    Weinig")
    print("B    Iets meer")
    print("C    Veel")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        end1()
    elif answerup == "B":
        clear()
        question20()
    elif answerup == "C":
        housinglist.pop(0)
        worklist.pop(0)
        clear()
        print("\033[38;2;255;0;0mJe wordt terug naar je oude\nland gestuurd omdat je gepakt was\nmet veel drugs.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question16()

class questionstartvar:
    qsvar = False
    
def questionstartvartrue():
    questionstartvar.qsvar = True

def question15():
    if questionstartvar.qsvar == False:
        keyboard.on_press_key("return", lambda _:questionstartvartrue())
        
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je bent aangenomen en kan meteen\nbeginnen. Een paar klanten vertellen\nwat ze willen hebben.\nJij moet onthouden wat ze willen.")
        print("───────────────────────────────────────")
        print("Druk op Enter om te starten...")
        time.sleep(1)
        clear()
        question15()
    else:
        random.shuffle(restaurantitems)
        print("\033[0mNaam: " + str(*playernamelist))
        print("Rugzak: " + str(*inventorylist))
        print("Woning: " + str(*housinglist))
        print("Werk: " + str(*worklist))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Je bent aangenomen en kan meteen\nbeginnen. Een paar klanten vertellen\nwat ze willen hebben.\nJij moet onthouden wat ze willen.")
        print("───────────────────────────────────────")
        time.sleep(0.5)
        i = 0
        while i != 3:
            print(restaurantitems[i])
            time.sleep(1)
            i += 1
            print("\033[A\033[A")
        print("Wat wilde de klanten hebben?")
        clearinput = input()
        print("\033[A\033[A")
        item1 = input("1> \n2> \n3> \033[A\033[A\033[38;2;0;128;128m")
        item2 = input("\033[0m2> \033[38;2;0;128;128m")
        item3 = input("\033[0m3> \033[38;2;0;128;128m")
        itemcap1 = item1.capitalize()
        itemcap2 = item2.capitalize()
        itemcap3 = item3.capitalize()
        if itemcap1 + "       " == restaurantitems[0] and itemcap2 + "       " == restaurantitems[1] and itemcap3 + "       " == restaurantitems[2]:
            print("\033[38;2;0;192;0mGoed gedaan!\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            end2()
        else:
            print("\033[38;2;255;0;0mJe had helaas niet alles goed.\n\033[38;2;192;192;0m")
            t = 3
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            answerednumber.questionsanswered += 1
            clear()
            question19()

def question14():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je bent een klein bedrijf gestart,\nmaar je krijgt te horen dat een\nfamilielid nog in het land zit waar\nje van vluchtte.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Ga het familielid halen")
    print("B    Focus op je eigen bedrijf")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        housinglist.pop(0)
        worklist.pop(0)
        clear()
        print("\033[38;2;255;0;0mHet lukt om bij je familielid te komen,\nmaar nu ben je alles weer kwijt.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    elif answerup == "B":
        clear()
        question18()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question14()

def question13():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("De man werd gepakt, en omdat jij\nde politie had gebeld krijg je een\nloonsverhoging. Je hebt nu genoeg geld\nvoor je eigen huis.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Koop een huis")
    print("B    Blijf doorsparen")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        end1()
    elif answerup == "B":
        clear()
        question17()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question13()

def question12():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Het werk begint saai te worden, maar\nop een dag bied een vreemde man\nje drugs aan.\nNeem je het aan?")
    print("───────────────────────────────────────")
    print("A    Ja")
    print("B    Nee")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question16()
    elif answerup == "B":
        clear()
        question17()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question12()

def question11():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je doet je werk zó goed, dat een\ngroot duur restaurant je een baan\naanbied.\nNeem je het aan?")
    print("───────────────────────────────────────")
    print("A    Ja")
    print("B    Nee")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question15()
    elif answerup == "B":
        clear()
        question12()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question11()

def question10():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je start een opleiding elektricien\nen slaagt na een paar jaar.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Start je eigen bedrijf")
    print("B    Werk bij een groot bedrijf")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        worklist.append("Eigen bedrijf")
        clear()
        question14()
    elif answerup == "B":
        clear()
        end1()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question10()

def question9():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je bent aangenomen bij een supermarkt.\nTijdens werk zie je een man appels\nonder zijn shirt stoppen en de winkel\nuitlopen.\nWat doe je?")
    print("───────────────────────────────────────")
    print("A    Bel de politie")
    print("B    Doe niks")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question13()
    elif answerup == "B":
        clear()
        question17()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question9()

def question8():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je wordt naar de grote stad gewezen\nen daar krijg je een paspoort en een\nklein appartementje. Je moet een\nbaan vinden om het te kunnen betalen.\nWat ga je doen?")
    print("───────────────────────────────────────")
    print("A    Restaurant medewerker")
    print("B    McRonald's kassamedewerker")
    print("C    Vakkenvuller")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        worklist.append("Restaurant medewerker")
        clear()
        question11()
    elif answerup == "B":
        worklist.append("McRonald's kassamedewerker")
        clear()
        question12()
    elif answerup == "C":
        worklist.append("Vakkenvuller")
        clear()
        question9()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question8()

def question7():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je bent het land binnen gelaten en zit\nnu in een asielzoekerscentrum. Om een\neigen huis te krijgen heb je\ngeld nodig.\nHoe ga je dat regelen?")
    print("───────────────────────────────────────")
    print("A    Zoek een baan")
    print("B    Overval een winkel")
    print("C    Doe een opleiding")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        worklist.append("Vakkenvuller")
        clear()
        question9()
    elif answerup == "B":
        inventorylist.pop(0)
        clear()
        print("\033[38;2;255;0;0mJe wordt gepakt en krijgt\neen gevangenisstraf.\nWacht 30 seconden.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██   ███ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m   █████  ██  █ ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██ █  ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ███   ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ███████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██             ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██            ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  █████   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████       ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██           ██   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██          ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████    █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██  ██      \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██             ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██             ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████     ████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██   ██ ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██  ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██   ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████      ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████    █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██             ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██             ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████     ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ █████    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████     ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██          ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██          ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m       ██ ██   ███ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ██  █ ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ██ █  ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██       ███   ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████    ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ███████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██         ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  █████   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████    ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██         ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██        ██   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██      █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████     ██      \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████    ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████      ██ ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██  ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██   ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████      ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██      █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████          ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████    █████    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██       ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████ ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██     ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m █████    ██   ███ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██  █ ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ██ █  ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m    ██    ███   ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ████████  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██  ███████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██      ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   █████   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██      ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██     ██   \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████     ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████    █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███  ██      \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██ ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██ ██    ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████   ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███ ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██ ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████     ████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███   ██ ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██  ██  ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██ ██   ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██ ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████       ██  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██   █████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ███████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███       ██ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██  ██████  \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██ ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██ ██       \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("\033[38;2;192;192;0m             DE GEVANGENIS             ")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║  ")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝  ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████     ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██   ███ █████    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██  █ ██    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ██ █  ██    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m ███   ██    ██    \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ │\033[38;2;224;96;0m  ██████  ████████ \033[38;2;192;192;0m│ ║   ║   ")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║   ")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        question7()
    elif answerup == "C":
        clear()
        question10()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question7()

def question6():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Het was een warme reis, maar gelukkig\nhad je een fles water bij je.\nJe bent in een dorpje uit een\nander land terechtgekomen.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Vraag de weg naar een grote stad")
    print("B    Blijf in het dorpje")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        housinglist.append("Appartementje")
        clear()
        question8()
    elif answerup == "B":
        clear()
        print("\033[38;2;255;0;0mJe werd terug gestuurd omdat je\nillegaal in het land verbleef.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question6()

def question5():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Het was een warme reis, maar gelukkig\nkon je water uit cactussen halen\nmet je zakmes. Je bent in een dorpje\nuit een ander land terechtgekomen.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Vraag de weg naar een grote stad")
    print("B    Blijf in het dorpje")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        housinglist.append("Appartementje")
        clear()
        question8()
    elif answerup == "B":
        clear()
        print("\033[38;2;255;0;0mJe werd terug gestuurd omdat je\nillegaal in het land verbleef.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A of B!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question5()

def question4():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Waar ga je heen?")
    print("───────────────────────────────────────")
    print("A    Zandwoestijn")
    print("B    Buurland")
    print("C    Overzees land")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        if str(*inventorylist) == "Zakmes":
            clear()
            question5()
        elif str(*inventorylist) == "Paspoort" or str(*inventorylist) == "":
            clear()
            print("\033[38;2;255;0;0mJe droogde uit.\n\033[38;2;192;192;0m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            clear()
            question4()
        else:
            clear()
            question6()
    elif answerup == "B":
        if str(*inventorylist) == "Zakmes":
            clear()
            print("\033[38;2;255;0;0mJe mocht het land niet in wegens\nwapenbezit.\n\033[38;2;192;192;0m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            clear()
            question4()
        elif str(*inventorylist) == "Paspoort" or str(*inventorylist) == "":
            housinglist.append("Asielzoekerscentrum")
            clear()
            question7()
        else:
            clear()
            print("\033[38;2;255;0;0mJe mocht het land niet in omdat\nje geen paspoort had.\n\033[38;2;192;192;0m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            clear()
            question4()
    elif answerup == "C":
        if str(*inventorylist) == "Zakmes":
            clear()
            print("\033[38;2;255;0;0mJe stak per ongeluk de rubberboot lek\nmet je zakmes.\n\033[38;2;192;192;0m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            clear()
            question4()
        else:
            housinglist.append("Asielzoekerscentrum")
            clear()
            question7()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()

def question3():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Na een paar weken wordt je\nhet land uitgezet.\nWaar ga je heen?")
    print("───────────────────────────────────────")
    print("A    Zandwoestijn")
    print("B    Buurland")
    print("C    Overzees land")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        print("\033[38;2;255;0;0mJe droogde uit.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    elif answerup == "B":
        housinglist.append("Asielzoekerscentrum")
        clear()
        question7()
    elif answerup == "C":
        housinglist.append("Asielzoekerscentrum")
        clear()
        question7()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question3()

def question2():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je hebt nog tijd om één ding\nmee te nemen.\nWat neem je mee?")
    print("───────────────────────────────────────")
    print("A    Zakmes")
    print("B    Paspoort")
    print("C    Fles water")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        inventorylist.append("Zakmes")
        clear()
        question4()
    elif answerup == "B":
        inventorylist.append("Paspoort")
        clear()
        question4()
    elif answerup == "C":
        inventorylist.append("Fles water")
        clear()
        question4()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question2()

def question1():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Een vijandig land neemt jouw land over.\nWat ga je doen?")
    print("───────────────────────────────────────")
    print("A    Vluchten")
    print("B    Vechten")
    print("C    Overgeven")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question2()
    elif answerup == "B":
        clear()
        print("\033[38;2;255;0;0mJe kon het niet winnen.\n\033[38;2;192;192;0m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question1()
    elif answerup == "C":
        clear()
        question3()
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question1()

def startinfo():
    clear()
    print("\033[0mHallo vreemdeling! Wat is je naam?")
    playername = input("Naam: \033[38;2;0;128;128m")
    
    characterslist = ["!", "¡", "%", "*", "(", "‘", ")", "’", "=", "+", "×", "÷", "\t", "®", "[", "{", "«", "]", "}", "»", "\\", "|", "¬", "¦", "§", ";", ":", "¶", "°", "'", '"', "©", ",", "<", ".", ">", "/", "?", "¿", "  "]
    checkplayername = [char for char in characterslist if char in playername]
    
    for c in checkplayername:
        if c in characterslist:
            print("\033[38;2;192;0;0mJe naam mag niet het volgende bevatten:\n- Leestekens\n- Aanhalingstekens\n- Haakjes\n- Symbolen\n- Herhalende spaties\n\033[38;2;192;192;0m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            startinfo()
    
    if playername == "":
        print("\033[38;2;192;0;0mJe naam mag niet niks zijn!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif playername == " ":
        print("\033[38;2;192;0;0mJe naam mag niet een spatie zijn!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif len(playername) == 33 or (len(playername) - 33) % 39 == 0:
        print("\033[38;2;192;0;0m\033[AJe naam mag niet langer dan\n24 karakters zijn!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif len(playername) > 24:
        print("\033[38;2;192;0;0mJe naam mag niet langer dan\n24 karakters zijn!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    else:
        pass

    playernamelist.append(playername)
    print("\033[0m" + f"\nHallo {playername}.")
    
    time.sleep(3)
    clear()
    print("In dit verhaal ben jij een vluchteling.\n\nDoor meerkeuzevragen te beantwoorden\nen misschien een paar minigames te\nvoltooien, neem je verschillende paden\nnaar verschillende eindes.\n\nEr zijn zes eindes die goed of slecht\nkunnen zijn, dus genoeg verhalen om\nte beleven.\n\nVeel plezier!\n\033[38;2;192;192;0m")
    t = 15
    while t != 0:
        if str(t)[-1] == 0:
            print(str(t)[0])
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        else:
            print(str(t) + " ")
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
    clear()
    
    timerthread = threading.Thread(target=timer)
    gamethread = threading.Thread(target=question1)
    
    timerthread.start()
    gamethread.start()

class entervar:
    evar = False
    
def entervartrue():
    entervar.evar = True

def startscreen():
    if entervar.evar == False:
        keyboard.on_press_key("return", lambda _:entervartrue())
        # ⁰¹²³⁴⁵⁶⁷⁸⁹⁻ᵅᵝ·
        version = "⁰·⁸·⁰⁻ᵝ"
        print("\033[0m\033[38;2;0;0;255m              WELKOM BIJ:              ")
        print("   _    __ __              __     __   ")
        print("  | |  / // /__  __ _____ / /_   / /_  ")
        print("  | | / // // / / // ___// __ \ / __/  ")
        print("  | |/ // // /_/ // /__ / / / // /_    ")
        print("  |___//_/ \__,_/ \___//_/ /_/ \__/    ")
        print("   _    __ __              \033[38;2;192;192;0m__ \033[38;2;0;0;255m__ __    ")
        print("  | |  / // /__  __ ____ _ \033[38;2;192;192;0m\ \\\033[38;2;0;0;255m" + r"\ \\ \   ")
        print("  | | / // // / / // __ `/ \033[38;2;192;192;0m \ \\\033[38;2;0;0;255m" + r"\ \\ \  ")
        print("  | |/ // // /_/ // /_/ /  \033[38;2;192;192;0m / /\033[38;2;0;0;255m/ // /  ")
        print("  |___//_/ \__,_/ \__, /   \033[38;2;192;192;0m/_/\033[38;2;0;0;255m/_//_/   ")
        print("                 /____/                ")
        print(" ╔═══════════════════════════════════╗ ")
        print(" ║ << DRUK OP ENTER OM TE STARTEN >> ║ ")
        print(" ╚═══════════════════════════════════╝ ")
        print("\033[38;2;64;64;64m\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + " \033[0m")
        time.sleep(0.3)
        clear()
        print("\033[0m\033[38;2;0;0;255m              WELKOM BIJ:              ")
        print("   _    __ __              __     __   ")
        print("  | |  / // /__  __ _____ / /_   / /_  ")
        print("  | | / // // / / // ___// __ \ / __/  ")
        print("  | |/ // // /_/ // /__ / / / // /_    ")
        print("  |___//_/ \__,_/ \___//_/ /_/ \__/    ")
        print("   _    __ __              __ \033[38;2;192;192;0m__ \033[38;2;0;0;255m__    ")
        print("  | |  / // /__  __ ____ _ \ \\\033[38;2;192;192;0m\ \\\033[38;2;0;0;255m\ \   ")
        print("  | | / // // / / // __ `/  \ \\\033[38;2;192;192;0m\ \\\033[38;2;0;0;255m\ \  ")
        print("  | |/ // // /_/ // /_/ /   / /\033[38;2;192;192;0m/ /\033[38;2;0;0;255m/ /  ")
        print("  |___//_/ \__,_/ \__, /   /_/\033[38;2;192;192;0m/_/\033[38;2;0;0;255m/_/   ")
        print("                 /____/                ")
        print(" ╔═══════════════════════════════════╗ ")
        print(" ║\033[38;2;0;192;192m << DRUK OP ENTER OM TE STARTEN >> \033[38;2;0;0;255m║ ")
        print(" ╚═══════════════════════════════════╝ ")
        print("\033[38;2;64;64;64m\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + " \033[0m")
        time.sleep(0.3)
        clear()
        print("\033[0m\033[38;2;0;0;255m              WELKOM BIJ:              ")
        print("   _    __ __              __     __   ")
        print("  | |  / // /__  __ _____ / /_   / /_  ")
        print("  | | / // // / / // ___// __ \ / __/  ")
        print("  | |/ // // /_/ // /__ / / / // /_    ")
        print("  |___//_/ \__,_/ \___//_/ /_/ \__/    ")
        print("   _    __ __              __ __ \033[38;2;192;192;0m__    ")
        print("\033[38;2;0;0;255m  | |  / // /__  __ ____ _ \ \\\ \\\033[38;2;192;192;0m\ \   ")
        print("\033[38;2;0;0;255m  | | / // // / / // __ `/  \ \\\ \\\033[38;2;192;192;0m\ \  ")
        print("\033[38;2;0;0;255m  | |/ // // /_/ // /_/ /   / // /\033[38;2;192;192;0m/ /  ")
        print("\033[38;2;0;0;255m  |___//_/ \__,_/ \__, /   /_//_/\033[38;2;192;192;0m/_/   ")
        print("\033[38;2;0;0;255m                 /____/                ")
        print(" ╔═══════════════════════════════════╗ ")
        print(" ║ << DRUK OP ENTER OM TE STARTEN >> ║ ")
        print(" ╚═══════════════════════════════════╝ ")
        print("\033[38;2;64;64;64m\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + " \033[0m")
        time.sleep(0.3)
        clear()
        startscreen()
    else:
        clear()
        clearinput = input()
        startinfo()
    
startmusic("Sneaky Snitch - Kevin MacLeod.mp3")
startscreen()

# Muziek:
# Sneaky Snitch door Kevin MacLeod
# Link: https://incompetech.filmmusic.io/song/4384-sneaky-snitch
# Licentie: https://filmmusic.io/standard-license