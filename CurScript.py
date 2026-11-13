import mouse
import time
from pathlib import Path
from colorama import Fore, Back, Style
dur = 0
multiplier = 1
print_actions = 0

def interpreter():
    global dur
    filetorun = Path(__file__).resolve().parent / "Projects" / (input("file to run: ") + ".curscript").strip()
    if print_actions == "1":
        print(filetorun)
    try:
        with open(filetorun) as file:
            instructions = [line.strip() for line in file]
    except:
        print(Fore.RED + "error: file could not be found in projects folder")
        print(Fore.RESET + "")
    else:
        print("")
        unknowns = 0
        if print_actions == "1":
            print(instructions)
        for cmd in instructions:
            if not cmd:
                continue
        
            controller = cmd[0]
            data = cmd[1:].strip()
        
            if controller == "X":
                if print_actions == "1":
                    print("Move to X " + str(int(data)))
                x = mouse.get_position()[0]
                y = mouse.get_position()[1]
                mouse.move((int(data)), y, absolute=True, duration=dur)
            elif controller == "Y":
                if print_actions == "1":
                    print("Move to Y " + str(int(data)))
                x = mouse.get_position()[0]
                y = mouse.get_position()[1]
                mouse.move(x, (int(data)), absolute=True, duration=dur)
            elif controller == "S":
                if print_actions == "1":
                    print("Scroll by " + str(int(data)))
                mouse.wheel(delta=int(data))
            elif controller == "L":
                if print_actions == "1":
                    print("Left by " + str(int(data) * multiplier))
                mouse.move((float(data)) * (multiplier * -1), 0, absolute=False, duration=dur)
            elif controller == "R":
                if print_actions == "1":
                    print("Right by " + str(int(data) * multiplier))
                mouse.move((float(data)) * (multiplier * 1), 0, absolute=False, duration=dur)
            elif controller == "U":
                if print_actions == "1":
                    print("Up by " + str(int(data) * multiplier))
                mouse.move(0, (float(data)) * (multiplier * -1), absolute=False, duration=dur)
            elif controller == "D":
                if print_actions == "1":
                    print("Down by " + str(int(data) * multiplier))
                mouse.move(0, (float(data)) * (multiplier * 1), absolute=False, duration=dur)
            elif controller == "W":
                if print_actions == "1":
                    print("Wait for " + str(float(data)))
                time.sleep(float(data))
            elif controller == "T":
                if print_actions == "1":
                    print("Set the duration of movements to " + str(float(data)))
                dur = float(data)
            elif controller == "M":
                print(data)
            elif controller == "C":
                if data == "R":
                    mouse.click('right')
                    if print_actions == "1":
                        print("right click")
                if data == "L":
                    mouse.click('left')
                    if print_actions == "1":
                        print("left click")
                if data == "M":
                    mouse.click('middle')
                    if print_actions == "1":
                        print("middle click")
            else:
                if print_actions == "1":
                    print(Fore.RED + "unknown command" + Fore.RESET)
                    unknowns += 1
    if print_actions == "1" and unknowns > 0:
        print(Fore.RED + str(unknowns) + Fore.RESET + " unknown commands were found in the script")
    dur = 0
    terminal()

def findmymouse():
    print("")
    print("right click to print your current mouse position")
    while not mouse.is_pressed("right"):
        time.sleep(0.1)
    print(Fore.GREEN + str(mouse.get_position()) + Fore.RESET)
    print("")
    terminal()

def configmenu():
    global print_actions
    global multiplier
    print("")
    print("1. pixel multiplier")
    print("2. print actions?")
    print("")
    settingchange = input("select a setting to change - ")
    if settingchange == "1":
        multiplier = float(input("configure pixel multiplier: "))
    elif settingchange == "2":
        print_actions = input("configure print actions? [0/1]: ")
    else:
        print(Fore.RED + "setting not recognised. Please input a valid number" + Fore.RESET)
    print("")

def helpmenu():
    print("")
    print("exit - exit CurScript")
    print("help - show the help menu")
    print("learn - a brief explanation on how to write CurScript")
    print("run - runs a CurScript file")
    print("config - open the settings menu")
    print("find - lets you find the position of your mouse")
    print("")
    
def learnmenu():
    print("")
    print("CurScript files are a bunch of different commands written on new lines")
    print("Here are all the commands you can use:")
    print("")
    print("L[num] - Move left by [num] pixels")
    print("R[num] - Move right by [num] pixels")
    print("U[num] - Move up by [num] pixels")
    print("D[num] - Move down by [num] pixels")    
    print("W[sec] - Wait for [sec] seconds")
    print("T[sec] - Set the duration of every mouse movement (0 by default)")
    print("X[num] - Go to [num] on the X axis")
    print("Y[num] - Go to [num on the Y axis")
    print("S[num] - Scroll [num] lines on the vertical axis")
    print("CL - Left click")
    print("CR - Right click")
    print("CM - Middle click")
    print("M[message] - Send a message to the user")
    print("")
    print("If you want to see these commands in action, run the demo file")
    print("")
    
def terminal():
    command = input("> ")

    if command == "help":
        helpmenu()
        terminal()
    elif command == "learn":
        learnmenu()
        terminal()
    elif command == "exit":
        print("exiting")
    elif command == "config":
        configmenu()
        terminal()
    elif command == "run":
        interpreter()
    elif command == "find":
        findmymouse()
    else:
        print("")
        print(Fore.RED + "command not recognised - input 'help' for a list of commands" + Fore.RESET)
        print("")
        terminal()

print("CurScript 1.0.3")
print("")
print("input 'help' for instructions on how to use this app")
print("input 'learn' for instructions on how to write CurScript")
print("")
terminal()