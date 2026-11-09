import mouse
import time
from pathlib import Path

dur = 0
multiplier = 1
print_actions = 0

def interpreter():
    filetorun = Path(__file__).resolve().parent / "Projects" / input("file to run: ").strip()
    print(filetorun)
    try:
        with open(filetorun) as file:
            instructions = [line.strip() for line in file]
    except:
        print("file could not be found in projects folder")
        print("")
    else:
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
                mouse.drag(x, y, (int(data)), y, absolute=True, duration=dur)
            elif controller == "Y":
                if print_actions == "1":
                    print("Move to Y " + str(int(data)))
                x = mouse.get_position()[0]
                y = mouse.get_position()[1]
                mouse.drag(x, y, x, (int(data)), absolute=True, duration=dur)
            elif controller == "L":
                if print_actions == "1":
                    print("Left by " + str(int(data) * multiplier))
                mouse.drag(0, 0, (int(data) * (multiplier * -1)), 0, absolute=False, duration=dur)
            elif controller == "R":
                if print_actions == "1":
                    print("Right by " + str(int(data) * multiplier))
                mouse.drag(0, 0, (int(data) * (multiplier * 1)), 0, absolute=False, duration=dur)
            elif controller == "U":
                if print_actions == "1":
                    print("Up by " + str(int(data) * multiplier))
                mouse.drag(0, 0, 0, (int(data) * (multiplier * 1)), absolute=False, duration=dur)
            elif controller == "D":
                if print_actions == "1":
                    print("Down by " + str(int(data) * multiplier))
                mouse.drag(0, 0, 0, (int(data) * (multiplier * -1)), absolute=False, duration=dur)
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
                    print("unknown command")
    terminal()

def configmenu():
    print("")
    print("1. pixel multiplier")
    print("2. print actions?")
    print("")
    settingchange = input("select a setting to change - ")
    if settingchange == "1":
        multiplier = input("configure pixel multiplier: ")
    elif settingchange == "2":
        print_actions = input("print actions [0/1]: ")
    else:
        print("setting not recognised. Please input a valid number")
    print("")

def helpmenu():
    print("")
    print("exit - exit CurScript")
    print("help - show the help menu")
    print("learn - a brief explanation on how to write CurScript")
    print("run [filename] - runs a CurScript file")
    print("config - open the settings menu")
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
    print("M[message] - Send a message to the user")
    print("")
    print("If you want to see these commands in action, run default.curscript")
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
    else:
        print("")
        print("command not recognised - input 'help' for a list of commands")
        print("")
        terminal()

print("CurScript 1.0.0")
print("Created by Toyranna")
print("")
print("input 'help' for instructions on how to use this app")
print("input 'learn' for instructions on how to write CurScript")
print("")
terminal()