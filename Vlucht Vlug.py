from os import system, name
import ctypes
import time
import datetime
import keyboard

ctypes.windll.kernel32.SetConsoleTitleW("Vlucht Vlug")
system("mode con: cols=39 lines=18")

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

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

def question21():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question21()

def question20():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question20()

def question19():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question19()

def question18():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question18()

def question17():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question17()

def question16():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question16()

def question15():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question15()

def question14():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question14()

def question13():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question13()

def question12():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question12()

def question11():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question11()

def question10():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question10()

def question9():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question9()

def question8():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(".")
    print("───────────────────────────────────────")
    print("A    .")
    print("B    .")
    print("C    .")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        #question
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question8()

def question7():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je bent het land binnen gelaten en zit\nnu in een asielzoekerscentrum. Om een\neigen huis te krijgen heb je\ngeld nodig.\nHoe ga je dat regelen?")
    print("───────────────────────────────────────")
    print("A    Zoek een baan")
    print("B    Overval een winkel")
    print("C    Doe een opleiding")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question9()
    elif answerup == "B":
        clear()
        print("\033[40;91mJe wordt gepakt en krijgt\neen gevangenisstraf.\nWacht 30 seconden.\n\033[40;33m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██   ███ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m   █████  ██  █ ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██ █  ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ███   ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ███████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██             ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██            ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  █████   \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████       ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██           ██   \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██          ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████    █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██  ██      \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██             ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██             ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████     ████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██   ██ ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██  ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██   ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████      ██  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████    █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██             ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██             ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████     ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ █████    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████     ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██          ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██          ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m ███████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m       ██ ██   ███ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ██  █ ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ██ █  ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██       ███   ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████    ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ███████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██         ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  █████   \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████    ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██         ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██        ██   \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██      █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████     ██      \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████    ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████      ██ ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██  ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██   ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████      ██  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██      █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████          ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████    █████    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██       ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████ ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m    ██     ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m █████    ██   ███ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██  █ ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ██ █  ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m    ██    ███   ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ████████  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██  ███████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██      ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   █████   \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██      ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██     ██   \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████     ██    \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████    █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███  ██      \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██ ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██ ██    ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████   ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███ ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██ ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████     ████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███   ██ ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██  ██  ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██ ██   ██  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██ ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████       ██  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██   █████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ███████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███       ██ \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██  ██████  \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██ ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██ ██       \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        print("             DE GEVANGENIS")
        print("═══╦═══╦═══╦═══╦═══╦═══╦══╦═════════╦══")
        print(f"   ║   ║   ║   ║   ║   ║  ║ CEL {cel} ║")
        print("   ║   ║   ║   ║   ║   ║  ╚╦═══╦═══╦╝")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║ ┌─╨───╨───╨───╨───╨─┐ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████     ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██   ███ █████    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██  █ ██    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ██ █  ██    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m ███   ██    ██    \033[40;33m│ ║   ║")
        print("   ║   ║ │\033[40;91m  ██████  ████████ \033[40;33m│ ║   ║")
        print("   ║   ║ └─╥───╥───╥───╥───╥─┘ ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("   ║   ║   ║   ║   ║   ║   ║   ║   ║")
        print("═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══")
        time.sleep(1)
        clear()
        question7()
    elif answerup == "C":
        clear()
        question10()
    else:
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question7()

def question6():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Het was een warme reis, maar gelukkig\nhad je een fles water bij je.\nJe bent in een dorpje uit een\nander land terechtgekomen.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Vraag de weg naar een grote stad")
    print("B    Blijf in het dorpje")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question8()
    elif answerup == "B":
        clear()
        print("\033[40;91mJe werd terug gestuurd omdat je\nillegaal in het land verbleef.\n\033[40;33m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    else:
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question6()

def question5():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Het was een warme reis, maar gelukkig\nkon je water uit cactussen halen\nmet je zakmes. Je bent in een dorpje\nuit een ander land terechtgekomen.\nWat nu?")
    print("───────────────────────────────────────")
    print("A    Vraag de weg naar een grote stad")
    print("B    Blijf in het dorpje")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question8()
    elif answerup == "B":
        clear()
        print("\033[40;91mJe werd terug gestuurd omdat je\nillegaal in het land verbleef.\n\033[40;33m")
        t = 5
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()
    else:
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question5()

def question4():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Waar ga je heen?")
    print("───────────────────────────────────────")
    print("A    Zandwoestijn")
    print("B    Buurland")
    print("C    Overzees land")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        if str(*inventorylist) == "Zakmes":
            clear()
            question5()
        elif str(*inventorylist) == "Paspoort" or str(*inventorylist) == "":
            clear()
            print("\033[40;91mJe droogde uit.\n\033[40;33m")
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
            print("\033[40;91mJe mocht het land niet in wegens\nwapenbezit.\n\033[40;33m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            clear()
            question4()
        elif str(*inventorylist) == "Paspoort" or str(*inventorylist) == "":
            clear()
            question7()
        else:
            clear()
            print("\033[40;91mJe mocht het land niet in omdat\nje geen paspoort had.\n\033[40;33m")
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
            print("\033[40;91mJe stak per ongeluk de rubberboot lek\nmet je zakmes.\n\033[40;33m")
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
            question7()
    else:
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question4()

def question3():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Na een paar weken wordt je\nhet land uitgezet.\nWaar ga je heen?")
    print("───────────────────────────────────────")
    print("A    Zandwoestijn")
    print("B    Buurland")
    print("C    Overzees land")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        print("\033[40;91mJe droogde uit.\n\033[40;33m")
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
        question7()
    elif answerup == "C":
        clear()
        question7()
    else:
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question3()

def question2():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Je hebt nog tijd om één ding\nmee te nemen.\nWat neem je mee?")
    print("───────────────────────────────────────")
    print("A    Zakmes")
    print("B    Paspoort")
    print("C    Fles water")
    answer = input(">" + "\033[40;36m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        clear()
        question2()

def question1():
    print("\033[40;0mNaam: " + str(*playernamelist))
    print("Rugzak: " + str(*inventorylist))
    print("Woning: " + str(*housinglist))
    print("Werk: " + str(*worklist))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Een vijandig land neemt jouw land over.\nWat ga je doen?")
    print("───────────────────────────────────────")
    print("A    Vluchten")
    print("B    Vechten")
    print("C    Overgeven")
    answer = input(">" + "\033[40;36m")
    answerup = answer.upper()
    if answerup == "A":
        clear()
        question2()
    elif answerup == "B":
        clear()
        print("\033[40;91mJe kon het niet winnen.\n\033[40;33m")
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
        print("\033[40;31mTyp alleen de letters A, B of C!\n\033[40;33m")
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
    print("\033[40;0mHallo vreemdeling! Wat is je naam?")
    playername = input("Naam: " + "\033[40;36m")
    
    characterslist = ["!", "¡", "%", "*", "(", "‘", ")", "’", "=", "+", "×", "÷", "\t", "®", "[", "{", "«", "]", "}", "»", "\\", "|", "¬", "¦", "§", ";", ":", "¶", "°", "'", '"', "©", ",", "<", ".", ">", "/", "?", "¿", "  "]
    checkplayername = [char for char in characterslist if char in playername]
    
    for c in checkplayername:
        if c in characterslist:
            print("\033[40;31mJe naam mag niet het volgende bevatten:\n- Leestekens\n- Aanhalingstekens\n- Haakjes\n- Symbolen\n- Herhalende spaties\n\033[40;33m")
            t = 5
            while t != 0:
                print(t)
                time.sleep(1)
                t -= 1
                print("\033[A\033[A")
            startinfo()
    
    if playername == "":
        print("\033[40;31mJe naam mag niet niks zijn!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif playername == " ":
        print("\033[40;31mJe naam mag niet een spatie zijn!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif len(playername) == 33 or (len(playername) - 33) % 39 == 0:
        print("\033[40;31m\033[AJe naam mag niet langer dan\n32 karakters zijn!\n\033[40;33m")
        t = 3
        while t != 0:
            print(t)
            time.sleep(1)
            t -= 1
            print("\033[A\033[A")
        startinfo()
    elif len(playername) > 32:
        print("\033[40;31mJe naam mag niet langer dan\n32 karakters zijn!\n\033[40;33m")
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
    print("\033[40;0m" + f"\nHallo {playername}.")
    
    time.sleep(3)
    clear()
    print("In dit verhaal ben jij een vluchteling.\n\nDoor meerkeuzevragen te beantwoorden\nen misschien een paar minigames te\nvoltooien, neem je verschillende paden\nnaar verschillende eindes.\n\nEr zijn zes eindes die goed of slecht\nkunnen zijn, dus genoeg verhalen om\nte beleven.\n\nVeel plezier!\n\033[40;33m")
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
    question1()

class spacebarvar:
    svar = False
    
def spacebarvartrue():
    spacebarvar.svar = True

def startscreen():
    if spacebarvar.svar == False:
        keyboard.on_press_key("return", lambda _:spacebarvartrue())
        # ⁰¹²³⁴⁵⁶⁷⁸⁹⁻ᵅᵝ·
        version = "⁰·⁶·¹⁻ᵝ"
        print("\033[40;36m" + r"   _    __ __              __     __  ")
        print(r"  | |  / // /__  __ _____ / /_   / /_ ")
        print(r"  | | / // // / / // ___// __ \ / __/ ")
        print(r"  | |/ // // /_/ // /__ / / / // /_   ")
        print(r"  |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"   _    __ __              " + "\033[40;33m" + "__ " + "\033[40;36m" + r"__ __   ")
        print(r"  | |  / // /__  __ ____ _ " + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \\ \  ")
        print(r"  | | / // // / / // __ `/ " + "\033[40;33m" + " \ \\" + "\033[40;36m" + r"\ \\ \ ")
        print(r"  | |/ // // /_/ // /_/ /  " + "\033[40;33m" + " / /" + "\033[40;36m" + r"/ // / ")
        print(r"  |___//_/ \__,_/ \__, /   " + "\033[40;33m" + "/_/" + "\033[40;36m" + r"/_//_/  ")
        print(r"                 /____/               ")
        print(" ╔═══════════════════════════════════╗")
        print(" ║ << DRUK OP ENTER OM TE STARTEN >> ║")
        print(" ╚═══════════════════════════════════╝")
        print("\033[40;90m\n\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + "\033[40;0m")
        time.sleep(0.3)
        clear()
        print("\033[40;36m" + r"   _    __ __              __     __  ")
        print(r"  | |  / // /__  __ _____ / /_   / /_ ")
        print(r"  | | / // // / / // ___// __ \ / __/ ")
        print(r"  | |/ // // /_/ // /__ / / / // /_   ")
        print(r"  |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"   _    __ __              __ " + "\033[40;33m" + "__ " + "\033[40;36m" + r"__   ")
        print("  | |  / // /__  __ ____ _ \ \\" + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \  ")
        print("  | | / // // / / // __ `/  \ \\" + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \ ")
        print(r"  | |/ // // /_/ // /_/ /   / /" + "\033[40;33m" + "/ /" + "\033[40;36m" + r"/ / ")
        print(r"  |___//_/ \__,_/ \__, /   /_/" + "\033[40;33m" + "/_/" + "\033[40;36m" + r"/_/  ")
        print(r"                 /____/               ")
        print(" ╔═══════════════════════════════════╗")
        print(" ║\033[40;96m << DRUK OP ENTER OM TE STARTEN >> \033[40;36m║")
        print(" ╚═══════════════════════════════════╝")
        print("\033[40;90m\n\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + "\033[40;0m")
        time.sleep(0.3)
        clear()
        print("\033[40;36m" + r"   _    __ __              __     __  ")
        print(r"  | |  / // /__  __ _____ / /_   / /_ ")
        print(r"  | | / // // / / // ___// __ \ / __/ ")
        print(r"  | |/ // // /_/ // /__ / / / // /_   ")
        print(r"  |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"   _    __ __              __ __ " + "\033[40;33m" + "__   ")
        print("\033[40;36m" + "  | |  / // /__  __ ____ _ \ \\\ \\" + "\033[40;33m" + "\ \  ")
        print("\033[40;36m" + "  | | / // // / / // __ `/  \ \\\ \\" + "\033[40;33m" + "\ \ ")
        print("\033[40;36m" + r"  | |/ // // /_/ // /_/ /   / // /" + "\033[40;33m" + "/ / ")
        print("\033[40;36m" + r"  |___//_/ \__,_/ \__, /   /_//_/" + "\033[40;33m" + "/_/  ")
        print("\033[40;36m" + r"                 /____/               ")
        print(" ╔═══════════════════════════════════╗")
        print(" ║ << DRUK OP ENTER OM TE STARTEN >> ║")
        print(" ╚═══════════════════════════════════╝")
        print("\033[40;90m\n\n ᴹⁱᵗᶜʰᵉˡ ᴷˡⁱʲⁿ                 " + version + "\033[40;0m")
        time.sleep(0.3)
        clear()
        startscreen()
    else:
        clear()
        clearinput = input()
        startinfo()
    
startscreen()