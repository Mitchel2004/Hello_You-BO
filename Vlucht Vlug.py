from os import system, name
import ctypes
import time
import keyboard
import re

ctypes.windll.kernel32.SetConsoleTitleW("Vlucht Vlug")
system("mode con: cols=37 lines=14")

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")        



def startinfo():
    clear()
    print("\033[40;0m" + "Hallo vreemdeling! Wat is je naam?")
    playername = input("Naam:" + "\033[40;36m")
    print("\033[40;0m" + f"\nHallo{playername}.")
    time.sleep(3)
    clear()
    print("In dit verhaal ben jij\neen vluchteling.\nDoor meerkeuzevragen te beantwoorden\nkan je verschillende paden nemen en\nverschillende eindes krijgen.\nDe vier verschillende eindes kunnen\ngoed of slecht zijn,\ndus kies voorzichtig.\nVeel succes.\n")
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

class spacebarvar:
    svar = False
    
def spacebarvartrue():
    spacebarvar.svar = True

def startscreen():
    if spacebarvar.svar == False:
        keyboard.on_press_key(" ", lambda _:spacebarvartrue())
        
        print("\033[40;36m" + r"  _    __ __              __     __  ")
        print(r" | |  / // /__  __ _____ / /_   / /_ ")
        print(r" | | / // // / / // ___// __ \ / __/ ")
        print(r" | |/ // // /_/ // /__ / / / // /_   ")
        print(r" |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"  _    __ __              " + "\033[40;33m" + "__ " + "\033[40;36m" + r"__ __   ")
        print(r" | |  / // /__  __ ____ _ " + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \\ \  ")
        print(r" | | / // // / / // __ `/ " + "\033[40;33m" + " \ \\" + "\033[40;36m" + r"\ \\ \ ")
        print(r" | |/ // // /_/ // /_/ /  " + "\033[40;33m" + " / /" + "\033[40;36m" + r"/ // / ")
        print(r" |___//_/ \__,_/ \__, /   " + "\033[40;33m" + "/_/" + "\033[40;36m" + r"/_//_/  ")
        print(r"                /____/               ")
        print("\n DRUK OP DE SPATIEBALK OM TE STARTEN" + "\033[40;0m")
        time.sleep(0.2)
        clear()
        print("\033[40;36m" + r"  _    __ __              __     __  ")
        print(r" | |  / // /__  __ _____ / /_   / /_ ")
        print(r" | | / // // / / // ___// __ \ / __/ ")
        print(r" | |/ // // /_/ // /__ / / / // /_   ")
        print(r" |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"  _    __ __              __ " + "\033[40;33m" + "__ " + "\033[40;36m" + r"__   ")
        print(" | |  / // /__  __ ____ _ \ \\" + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \  ")
        print(" | | / // // / / // __ `/  \ \\" + "\033[40;33m" + "\ \\" + "\033[40;36m" + r"\ \ ")
        print(r" | |/ // // /_/ // /_/ /   / /" + "\033[40;33m" + "/ /" + "\033[40;36m" + r"/ / ")
        print(r" |___//_/ \__,_/ \__, /   /_/" + "\033[40;33m" + "/_/" + "\033[40;36m" + r"/_/  ")
        print(r"                /____/               ")
        print("\033[40;96m" + "\n DRUK OP DE SPATIEBALK OM TE STARTEN" + "\033[40;0m")
        time.sleep(0.2)
        clear()
        print("\033[40;36m" + r"  _    __ __              __     __  ")
        print(r" | |  / // /__  __ _____ / /_   / /_ ")
        print(r" | | / // // / / // ___// __ \ / __/ ")
        print(r" | |/ // // /_/ // /__ / / / // /_   ")
        print(r" |___//_/ \__,_/ \___//_/ /_/ \__/   ")
        print(r"  _    __ __              __ __ " + "\033[40;33m" + "__   ")
        print("\033[40;36m" + " | |  / // /__  __ ____ _ \ \\\ \\" + "\033[40;33m" + "\ \  ")
        print("\033[40;36m" + " | | / // // / / // __ `/  \ \\\ \\" + "\033[40;33m" + "\ \ ")
        print("\033[40;36m" + r" | |/ // // /_/ // /_/ /   / // /" + "\033[40;33m" + "/ / ")
        print("\033[40;36m" + r" |___//_/ \__,_/ \__, /   /_//_/" + "\033[40;33m" + "/_/  ")
        print("\033[40;36m" + r"                /____/               ")
        print("\n DRUK OP DE SPATIEBALK OM TE STARTEN" + "\033[40;0m")
        time.sleep(0.2)
        clear()
        startscreen()
    else:
        startinfo()
    
startscreen()