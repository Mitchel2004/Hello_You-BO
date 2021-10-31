import os
import ctypes
import threading
import time
import datetime
import keyboard
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
    
    scored = str(scorenumber.score) + " " * (16 - len(str(scorenumber.score)))
    
    if len(str(scorenumber.score)) > 16:
        scored = str(scorenumber.score)[:15] + "+"
    else:
        pass
    
    answered = str(answerednumber.questionsanswered) + " " * (16 - len(str(answerednumber.questionsanswered)))
    
    if len(str(answerednumber.questionsanswered)) > 16:
        answered = str(answerednumber.questionsanswered) + "+"
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question20()

def question19():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question19()

def question18():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question18()

def question17():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
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

def question15():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question15()

def question14():
    answerednumber.questionsanswered += 1
    print("\033[0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input("> \033[38;2;0;128;128m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
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
        #question
    else:
        print("\033[38;2;192;0;0mTyp alleen de letters A, B of C!\n\033[38;2;192;192;0m")
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
    t = 1
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
    
#startmusic("Sneaky Snitch - Kevin MacLeod.mp3")
startscreen()

# Muziek:
# Sneaky Snitch door Kevin MacLeod
# Link: https://incompetech.filmmusic.io/song/4384-sneaky-snitch
# Licentie: https://filmmusic.io/standard-license